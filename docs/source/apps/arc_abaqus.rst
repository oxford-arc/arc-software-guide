Abaqus
------

**Introduction**
 
Abaqus is a popular commercial finite element, multi-physics simulation from Simulia.  Abaqus is a parallel application and can run in both MPI and in shared-memory threaded mode.  The parallel execution is triggered and controlled by command line options to the abaqus driver, along with all the other run options.

The steps to run an Abaqus job are: 

- load the Abaqus module;
- create a submission script;
- submit the job.

**Important Note**

Abaqus is **only** available on the ARC legacy partition. This partition provides support for applications which do not support the main ARC nodes which run CentOS 8.

**Module Information**::
 
  module use /apps/common/legacy/modules
  
  module spider abaqus

  ----------------------------------------------------------------------------------------------------------
    ABAQUS:
  ----------------------------------------------------------------------------------------------------------
     Versions:
        ABAQUS/2020
        ABAQUS/2021


**Example Submission Script**
 
The example submission script below is suitable for running on the ARC cluster. This example is customised to ensure Abaqus runs on the **legacy** partition::
  
  #!/bin/bash

  #SBATCH --partition=legacy
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=12:00:00
  #SBATCH --job-name=AbaqusTest

  module use /apps/common/legacy/modules

  module load Abaqus/2021
  module load iimpi/2020a

  . abaqus.sh

  # Fetch an example input file for testing...
  abaqus fetch job=s4b.inp 

  abaqus input=s4b job=test cpus=${SLURM_NTASKS} interactive
 
Please note: The line ``. abaqus.sh`` in the above script is **important**, it ensures that Abaqus is configured correctly for the ARC environment by creating a file
named ``abaqus_v6.env`` in the job directory. It also creates a scratch directory for temporary Abaqus files. The example above also loads the ``iimpi/2020a`` module
which we use to override the older MPI libraries supplied.  
