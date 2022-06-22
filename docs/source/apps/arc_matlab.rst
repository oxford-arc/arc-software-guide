MATLAB
------

**Introduction**
 
MATLAB is a numerical computing and programming environment with a broad range of functionality (matrix manipulation, numerical linear algebra, general-purpose graphics, etc.).  Additionally, specialised application areas (e.g. bioinformatics or financial derivatives) are served by a large number of optional toolboxes

Matlab is installed on the ARC clusters along with all the toolboxes covered by the Oxford University Concurrent license.

The purpose of this example-based tutorial is to guide the user through a few aspects of running efficient Matlab jobs on the ARC resources.  These aspects are

- using the Matlab module,
- running Matlab scripts non-interactively from batch jobs and
- running Matlab jobs on parallel hardware:
- overview of parallel computing in Matlab,
- using the Matlab Parallel Computing toolbox,
- exploiting trivial task parallelism and
- multi-threaded Mex programming.

**Module Information**::
 
 module spider matlab

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  MATLAB:
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     Versions:
        MATLAB/R2019b
        MATLAB/R2020a
        MATLAB/R2020b
        MATLAB/R2021b


Non-interactive Matlab Sessions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During code development on standard machines Matlab is usually run in interactive mode, in this way making full use of its integrated environment. 
By contrast, given the "batch processing" nature of supercomputing resources, the preferred mode of operation for Matlab on our systems is non-interactive. 

One way to run Matlab non-interactively is through

- re-directing the standard input and output when invoking Matlab and 
- invoking Matlab from a submission script, submitted to the queue via the slurm scheduler.

Input and output re-direction is arguably the easiest way of running Matlab non-interactivelly. It is achieved using the Linux operators < and >, with Matlab
taking a code file as an input and writing the output to a file, e.g. ``matlab < myScript.m > myOutput.txt`` The main function/program e.g. ``myScript.m`` should have
the ``exit`` command at the end in order to force Matlab to quit after finishing the execution of the code.  

A simple example illustrating non-interactive Matlab use is found in the ``/apps/common/examples/matlab/seq`` directory which you can copy to your own area as follows::

  cp -r /apps/common/examples/matlab $DATA/
  cd $DATA/matlab/seq
  

In this example, the MATLAB program ``main.m`` sets a linear system with the right-hand side read from a file provided, solves it and saves the result to another file.  A Matlab job is sent to the queue and executed on a backend node using the job scheduler.  

Submission scripts should contain the following line to run the Matlab script::

 matlab -nodisplay -nosplash < main.m > run.log

The flag ``-nodisplay`` instructs Matlab to run without the GUI, while ``-nosplash`` prevents the display of the Matlab logo.
The < redirection operator ensures that Matlab runs your Matlab script, in this case ``main.m`` while the > operator re-directs the standard output
(normally to the terminal) to ``run.log`` file.

For example for the ``seq`` example above, the contents of the SLURM submission script ``run_slurm.sh`` is::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --time=00:05:00
  #SBATCH --job-name=matlab_test
  #SBATCH --partition=devel

  module purge
  module load MATLAB

  matlab -nodisplay -nosplash < main.m > run.log

To submit this to the scheduler::
 
   sbatch run_slurm.sh
   

Running Matlab on parallel hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Overview of parallel computing in Matlab**

Matlab was developed for a long time as a product for single-processor computing, partly because distributed parallelism was incompatible with Matlab's original design principles and partly because the potential market was perceived as too small to justify major development efforts.  However, the advent of multi-core CPUs and the changing nature of Matlab, from the original educational "matrix laboratory" to a complex technical computing environment, prompted a revision of this situation. Matlab now benefits from running on modern parallel hardware in at least two ways.

The first is a built-in feature of Matlab, which "naturally" exploits multi-core processing via the underlying multi-threaded libraries Intel MKL and FFTW.  Thus, linear algebra operations (such as the solution to a linear system A\b or matrix products A*B) and FFT operations (using the function fft) are implicitly multi-threaded and make use of all the cores available on a multi-core system without user intervention or special extra programming.  Some of the vectorised operations in Matlab are also multi-threaded.  However, this type of operations are only a part of Matlab programming and the vast proportion of the Matlab functionality are scripts or functions that can only use a single core.

Second, users can exploit parallel processing through a series of explicit programming techniques.  The following techniques are briefly discussed below, with examples given:

- using the Matlab toolbox Parallel Computing Toolbox;
- trivial parallelism exploited through independent Matlab processes;
- multi-threaded MEX programming.
- Matlab has two toolboxes (licensed separately from the main distribution) that enable explicit parallel programming: the Parallel Computing Toolbox and the Distributed Computing Server.  The Parallel Computing Toolbox is designed for programming  multi-core architectures, while the Distributed Computing Server extends the Matlab's functionality to large resources, such as clusters.

The functionality of the Parallel Computing Toolbox is extended from single cluster node processing to distributed processing across multiple nodes by the Distributed Computing Server.  To learn more about the product, please visit the Distributed Computing Server webpage.

The University has licenses for the Parallel Computing Toolbox and users are encouraged to use it in their jobs run on the ARC hardware.  However, neither the University nor ARC have licenses for the Distributed Computing Engine.  If you need to use this product, please contact the ARC staff to make your interest known.

**Using the Parallel Computing Toolbox**

The Parallel Computing Toolbox offers the programmer a range of high-level parallelism contructs such as parfor (parallel for loops) and distributed arrays, which can be used to parallelise processing.  Matlab scripts enhanced using these contructs can be run on a single multi-core system (such as a node of the ARC clusters), utilising all the cores available for parallel processing.  While this offers scope for faster execution, the programming is not without catches and requires both programming experience and the understanding of the underlying algorithms.  The MathWorks pages are the best introduction to the product.

A simple example of multi-core parallelism via the Parallel Computing Toolbox is provided in the ``/apps/common/examples/matlab/par`` directory which you can copy to your own area as follows::

  cp -r /apps/common/examples/matlab $DATA/
  cd $DATA/matlab/par
  
The program main.m evaluates an expensive function within a for loop and stores the results in an array.  The for loop is parallelised using the parfor construct; a parfor loop behaves like an ordinary for loop on a single-core execution but shares the computational load between several workers (normally, each run on a separate core) in parallel execution.  To make workers available for parallel execution, the command matlabpool is used in main.m; the example illustrates the behaviour of parfor both before and after the workers are initiated.

The example is run in batch mode with the command ``sbatch run_slurm.sh``  The submission file is::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=16
  #SBATCH --time=00:05:00
  #SBATCH --job-name=matlab_test
  #SBATCH --partition=devel


  module purge
  module load MATLAB

  matlab -nodisplay -nosplash < main.m > run.log

Notice once again how MATLAB is instructed to not load the interactive window. The ``ntasks-per-node`` SLURM resource value is set to 16 to request 16 cores for this job.

Note: do not turn java off when lauching MATLAB (i.e. do not invoke ``matlab -nojvm``); matlabpool uses the Java Virtual Machine.

After the job finishes, the CPU times spent executed the loops in ``main.m`` can be found in ``timings.dat`` showing a clear speed-up of the execution in parallel.

