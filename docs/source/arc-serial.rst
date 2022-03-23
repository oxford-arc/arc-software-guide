Efficiently Running Serial Software
===================================

Introduction
------------

Processing workloads often involve serial applications (i.e. single-threaded, single processes), which run on a single core. Jobs like this should preferably be
run on HTC (not ARC); the scheduler on HTC is optimised for small jobs, as is the hardware; ARC is optimised to prefer large parallel applications. HTC is the better
cluster to use for serial applications.

This guide gives tips on how to design a job script for a serial application. The assumption is the workload involves a large number of similar but independent runs of the same application with different input parameters.

Using job arrays
----------------

In the scenario of a workload with a large number of independent runs, packing several runs inside a job works well with job arrays. Using job arrays, a number
of jobs can be started with a single submission command and a single submission script. The job array index can be used within the submission script to identify
the parameters each process works with (input or output files, command line parameters, etc.).

To give an example, assume ``serialapp`` has to run a parameter sweep, with values ranging from ``1.01`` to ``1.96`` with a step of ``0.0`` All the processing can
be carried out by submitting one job with the following job script::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --job-name=test
  #SBATCH --time=00:30:00

  RUN_PARAM=$(printf "1.%02d\n" $SLURM_ARRAY_TASK_ID)
  
  serialapp $RUN_PARAM
  

The job can be submitted using the command:

  sbatch --array=1-96

The variable SLURM_ARRAY_TASK_ID is the job array index (set by SLURM when an array job is submitted) and runs from 1 to 96, in accordance with the
submission command above. It could also be used to, for example, run a specific line out of a file, or identify an input file.

There are other ways to control the input parameters per task; very common is to list them in a file and read one line per task out of that file
(corresponding to the task ID). 

For example; say serialapp requires input parameters more like::

  serialapp -a X -b Y -c Z

and you need to run 5 copies of it with different values of X, Y and Z. You could generate a file called "job_parameters" listing all the parameters
for each run one one line::

-a 1 -b 2 -c 3
-a 2 -b 4 -c 6
-a 3 -b 6 -c 9
-a 4 -b 8 -c 12
-a 5 -b 10 -c 15

and then submit a 5 task array, with each task reading the line corresponding to it's task ID from the parameter file::

  #SBATCH --nodes=1
  #SBATCH --job-name=test
  #SBATCH --time=00:30:00

  RUN_PARAM=$(sed -n ${SLURM_ARRAY_TASK_ID}p job_parameters)

  serialapp $RUN_PARAM

This job could be submitted using the command::

  sbatch --array=1-5
