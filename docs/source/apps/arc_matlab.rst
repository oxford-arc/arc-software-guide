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

Exploiting trivial parallelism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An easy way to exploit multi-core systems is to split the workflow into parts that can be processed completely independently.  The typical example in this category is a parameter sweep, where the same Matlab script is run a large number of times using different inputs; these runs are indepent from each other and can be carried out concurrently.  Thus, the entire workflow can be scheduled in jobs that group 8 independent runs to match the 8 cores available per compute node.  This strategy is best coupled with the use of the Matlab mcc compiler in order to avoid an excessive use of licenses.

A simple example is found in the the ``/apps/common/examples/matlab/mcc`` directory which you can copy to your own area as follows::

  cp -r /apps/common/examples/matlab $DATA/
  cd $DATA/matlab/mcc

The file ``oscillator.m`` is a Matlab script that computes the solution of a damped oscillator of unit mass (using the Matlab ode45 solver) and outputs the maximum oscillation in that solution.  The script is prepared for use as a standalone deployed executable using the Matlab function isdeployed.

To deploy the script as a standalone application, load the modules for Matlab and for the Intel-compilers, e.g.::

  module load MATLAB/R2021b intel/2020a
 
Then, compile the script using mcc and the command::

  mcc -v \
    -R -nojvm \
    -R -singleCompThread \
    -f ./mbuildopts.sh \
    -m oscillator.m
 

This command makes use of the options in the file ``mbuildopts.sh`` provided alongside the Matlab script and customised for the Intel compilers. If no option file is passed through the option -f, mcc uses the default options file, which uses the Gnu compilers gcc and g++; in principle, using the Intel compilers can lead to a faster executable.

The deployed executable is compiled to run using a single thread via the option -singleCompThread.  This is important as a number of process are to run concurrently on the same multi-core system.

The mcc compilation creates an executable called oscillator.  In addition to this, the process generates the files mccExcludedFiles.log and readme.txt, which can be safely discarded.  Also, the wrapper script ``run_oscillator.sh`` is generated; this can be used to launch the executable oscillator into execution as it ensures the correct environment (paths to shared libraries and other environment variables) is set before execution.  The ARC Matlab module updates all the necessary variables, and the executable oscillator can be launched directly, so using ``run_oscillator.sh`` is unecessary.

The submission script ``run_slurm.sh`` gives an example of how the deployed executable can be used to launch concurrent processes within the same job.  On the clusters, the script requests a single compute node ``#SBATCH --nodes=1`` ``#SBATCH --ntasks-per-node=8`` so that 8 cores are available for processing.  8 separate processes are started with different parameters, such that the 8 processes compute a parameter sweep.  The contents of ``run_slurm.sh`` is as follows::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=8
  #SBATCH --partition=devel
  #SBATCH --time=00:10:00
  #SBATCH --job-name=oscillator

  module purge
  module load MATLAB/R2021b intel/2020a


  # start 8 processes in the background
  ./oscillator 0.01 0.3 > result1 &
  ./oscillator 0.02 0.3 > result2 &
  ./oscillator 0.03 0.3 > result3 &
  ./oscillator 0.04 0.3 > result4 &
  ./oscillator 0.05 0.3 > result5 &
  ./oscillator 0.06 0.3 > result6 &
  ./oscillator 0.07 0.3 > result7 &
  ./oscillator 0.08 0.3 > result8 &

  # wait for all processes to finish (this is important!)
  wait

With the run parameters (representing the damping coefficient and the stiffness) passed on as command line arguments.  The processes are started in the background (using the symbol &), such that the second process can start before the first finishes, and so on.  At the end of the script, a synchronisation point is necessary, which is implemented using a "wait" loop which "listens" for any processes called oscillator; without this synchronisation, the job launches the ``oscillator`` processes into background execution and finishes, without waiting for the processes to complete.  

Each process prints the result (maximum oscillation) to the standard output; there is now way to "return" a numeric result from a standalone executable.  It is easy to preserve the results after the job runs by redirecting the output to the files result*.

Finally, the use of ``mcc`` can be avoided altogether and Matlab can be run directly.  For example, the first processing line in the script could be::

  matlab -nojvm -singleCompThread -r "oscillator(0.01, 0.3); exit" > result1 &
 
However, deployed executables do not require Matlab licenses to run, which can make an important economy, especially in the case of a large number of concurrent processes (such as a parameter sweep).

Multi-threaded MEX programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yet another way to exploit multi-core systems is via multi-threaded Mex programming.  Mex (Matlab EXecutable) files are dynamically linked subroutines compiled from C, C++ or Fortran source code that can be run from within Matlab in the same way as M-files or built-in functions.  These guidelines assume knowledge of serial Mex programming and provide an example of how to augment serial execution with multi-threading through OpenMP.  Coupled with OpenMP multi-threading, Mex files become a powerful method to accelerate key parts of a Matlab program.

The main reason to write Mex files in C or Fortran (thus abandoning the high-level abstracted Matlab programming) is to gain speed of execution in computationally intensive operations that otherwise become a bottleneck in an application.  Typically, this is done to replace a function that is identified through profiling as being slow and/or called a large number of times.  Nevertheless, this programming effort is rewarded to various degrees, with the greatest relative benefits normally met when a Mex replaces a Matlab script (M-file).  At the other extreme, Matlab operations that rely on performance libraries like FFTW (e.g. fftn) or BLAS/LAPACK (e.g. solution of a dense linear systems, A\b), which are highly optimised have nothing or very little to benefit from Mex programming.  The best source for learning Mex programming is the Mathworks webpages.

The functionality necessary for building Mex files is provided by the Matlab C, C++ or Fortran APIs.  The main component of a Mex source code is the external gateway function mexFunction, which manages the transfer of data between Mex files and the Matlab environment.  This can be combined with C or Fortran routines or any external library in a manner similar to any other source code.  (Note: the API provides a Fortran gateway function too but practice shows it is trickier to compile pure Fortran Mex code than pure C or C++; the easiest way forward for Fortran programmers is to use the C gateway function to invoke the Fortran routines, which are compiled separately using a Fortran compiler.)  The Mex gateway function is compiled using the Matlab mex utility, which invokes a backend compiler (such as gcc) and manages the linking stage with the Matlab Mex API libraries.  The compiler and compiler flags are configurable and the options can be stored in an options file.

An example can be found in the ``/apps/common/examples/matlab/mex`` directory which you can copy to your own area as follows::

  cp -r /apps/common/examples/matlab $DATA/
  cd $DATA/matlab/mex

This re-implements the BLAS axpy function, which adds the input matrix y to the input matrix x multiplied by the scalar a.  This example is purely illustrative and its utility does not stretch beyond this guide.  Matlab uses the threaded MKL implementation of axpy directly and this function is chosen for this example only because it is very simple to program and to understand.

The directory contains the C files ``axpy.c`` (which contains the gateway function) and ``axpy_kernel.c`` (which performs the a*x+y operation).  The main function ``axpy.c`` contains various checks on the input data and the function ``axpy_kernel.c`` contains OpenMP directive for threading the loop over the array index.  The directory also contains the Mex option files ``mexOpts.sh`` that is modified to use the Intel C compiler and to trigger AVX and SSE vectorisation.  Lastly, a simple ``makefile`` is also provided.

To generate the Mex file, use the commands::

  module load matlab/R2021b intel/2020a
  make
  
This generates the file ``axpy.mexa64`` which can be run directly from Matlab.  To test the function axpy thus generated, you can load an interactive session and start Matlab.  At the Matlab prompt, enter the commands::

  M = 60000; N = 30000;
  x = rand(M,N); y = rand(M,N); a = rand();
  tic; z = axpy(a, x,y, 1); toc;
  tic; z = axpy(a, x,y, 2); toc;
  tic; z = axpy(a, x,y, 4); toc;
  
The first two lines generate some data sets to work on.  The third line and after run the newly built function axpy using a, x and y as arguments as well as the number of OpenMP threads to use in the computation.  The threading is done in the computational function ``axpy_kernel.c`` and its effect can be seen in a reduction in the computational time when going from 2 threads to 4. Remember this is illustrative, a decrease of computational time is unlikely beyond 8 threads (there are several reasons for this).

The accuracy of the results can be checked against Matlab's own operations with the command::

  norm(z - (a*x + y), 'fro')

which should produce a number of the order of machine eps.
  
