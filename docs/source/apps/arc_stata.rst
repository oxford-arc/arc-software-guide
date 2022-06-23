Stata
-----

**Introduction**

Stata is a commercial statistical package, which provides a complete solution for data analysis, data management, and graphics.  
Stata version 14 is available in the multi-threaded package variant Stata/MP.

Stata/MP is capable of taking advantage of the multiple cores available on the cluster nodes and the product is licensed by ARC to run on a
maximum of 8 cores per job.  The product chooses the number of cores to run on automatically, but this depends on the algorithm used 
(not all methods can run on more than one core) and has an impact on scalability.

The guide shows how to

- load the Stata module;
- prepare a Stata job submission script and
- submit the Stata job.

**Running a Stata job**

First, you need to load the module for the Stata package, making the executables available in the path::

  module load Stata/14

Then, you need to prepare a submission script for the Stata job, which should look something like this::

  #!/bin/bash 

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=8 
  #SBATCH --time=01:00:00 
  #SBATCH --job-name=testStata

  module purge
  module load Stata/14

  stata-mp -s do test.do
 
The script requests a single cluster node (nodes=1) and it is up to Stata/MP to make use of up to the 8 cores it is licensed to run on.  
Assuming you have named the above SLURM script ``run-stata.sh`` the jobs can be sent to the queue with the command::

  sbatch run-stata.sh

The processing is in "batch mode" and all the Stata commands are input from the file ``test.do``  
Below the contents of the example file ``test.do`` is given, which contains commands that make use of the multi-core capability of 
Stata, and can be used for testing purposes::

  clear*
  set rmsg on
  set obs 10000000
  forval n = 1/5 {
  g i`n' = runiform()
  }
  g dv = rbinomial(1,.3)
  memory

  qui logit dv i*

  qui xtmixed dv i*

  *with bootstrap:
  qui bs, reps(2000): logit dv i*
 
