Julia
----

**Introduction**

Julia is a high-level, high-performance dynamic programming language for numerical computing


**Module information**::

  module spider julia 
  
  ----------------------------------------------------------------------------
  Julia:
  ----------------------------------------------------------------------------
      Description:
      Julia is a high-level, high-performance dynamic programming language for numerical computing

     Versions:
        Julia/1.5.1-linux-x86_64
        Julia/1.5.3-linux-x86_64
        Julia/1.6.2-linux-x86_64

**Multi-threaded Julia applications**

Julia applications can benefit from faster execution on modern multi-core machines through using multiple execution threads, and Julia provides built-in
support for multithreaded programming.  A multithreaded program contains two or more threads (each defining a separate path of execution) that can run concurrently.

**Example submission script**::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1
  #SBATCH --cpus-per-task=48
  #SBATCH --time=12:00:00
  #SBATCH --job-name=JuliaTest
  #SBATCH --partition=short

  module purge
  module load Julia/1.6.2-linux-x86_64
  julia -p ${SLURM_TASKS_PER_NODE} -t ${SLURM_CPUS_PER_TASK} myInput.jl
   
In the above example, ``myInput.jl`` should be substituted for the appropriate names of your Java application and data files.
 
