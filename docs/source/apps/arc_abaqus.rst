Abaqus
------

**Introduction**
 
Abaqus is a popular commercial finite element, multi-physics simulation from Simulia.  Abaqus is a parallel application and can run in both MPI and in shared-memory threaded mode.  The parallel execution is triggered and controlled by command line options to the abaqus driver, along with all the other run options.

The steps to run an Abaqus job are: 

- load the Abaqus module;
- create a submission script;
- submit the job.


.. note::
    The only supported version on ARC is the latest version **Abaqus 2022** This is due to the Intel MPI and compiler support provided by the vendor.

**Module Information**::
   
  module spider Abaqus

  -----------------------------------------------------------------------------
  Abaqus: Abaqus/2022
  -----------------------------------------------------------------------------
    Description:
      Finite Element Analysis software for modeling, visualization and best-in-class implicit and explicit dynamics FEA.



**Example Submission Script**
 
The example submission scripts below are suitable for running on the ARC cluster::
  
  #!/bin/bash

  #SBATCH --clusters=arc
  #SBATCH --partition=devel
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=AbaqusStandard

  module purge
  module load Abaqus/2022
  module load iimpi/2020a

  . abaqus_arcmpi.sh

  abaqus fetch job=s4b.inp
  abaqus job=s4b  \
         input=s4b \
         cpus=${SLURM_NTASKS} \
         interactive

The above is an Abaqus/Standard job running in hybrid MPI mode. The following example runs an Abaqus/Explicit simulation::

 #!/bin/bash

 #SBATCH --clusters=arc
 #SBATCH --partition=devel
 #SBATCH --nodes=2
 #SBATCH --ntasks-per-node=48
 #SBATCH --time=00:10:00
 #SBATCH --job-name=AbaqusExplicit

 module purge
 module load Abaqus/2022
 module load iimpi/2020a


 . abaqus_arcmpi.sh

 abaqus fetch job=knee_bolster
 abaqus fetch job=knee_bolster_ef1
 abaqus fetch job=knee_bolster_ef2
 abaqus fetch job=knee_bolster_ef3

 abaqus job=knee_bolster  \
        input=knee_bolster \
        cpus=${SLURM_NTASKS} \
        interactive


.. note::
    The line ``. abaqus_arcmpi.sh`` in the above scripts is **important**, it ensures that Abaqus is configured correctly for the ARC environment by creating a file
    named ``abaqus_v6.env`` in the job directory. Note: there is a space between the ``.`` and ``abaqus_arcmpi.sh``
    
    It also creates a scratch directory for temporary Abaqus files, and ensures the Intel MPI library is used.
    
    If you wish to make use of user defined Fortran functions, you should add the line::
        
        module load iccifort/2020.1.217
    
    To your submission script after the Abaqus module load. The ``abaqus.sh`` sccript also sets up the environment/options for the ifort compiler.
    
