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


**Non-interactive Matlab Sessions**

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
The < redirection operator ensures that Matlab runs the script ``main.m`` while the > operator re-directs the standard output
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
   


**Example Virtual Environment Build**::

 


**Example Submission Script**
 

The example submission script below is suitable for running on the ARC cluster ::

  #!/bin/bash

  #SBATCH --partition=devel
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=QiskitTest

  module purge
  module load Anaconda3/2022.05
  
  source activate $DATA/qiskit-env
  
  python (your python script here)
  
