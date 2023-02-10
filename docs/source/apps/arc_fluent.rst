ANSYS FLUENT
------------

**Introduction**
 
ANSYS FLUENT software contains the broad physical modeling capabilities needed to model flow, turbulence, heat transfer, and reactions for industrial applications ranging from air flow over an aircraft wing to combustion in a furnace, from bubble columns to oil platforms, from blood flow to semiconductor manufacturing, and from clean room design to wastewater treatment plants.

**Module Information**::
 
 module spider FLUENT

 -----------------------------------------------------------------------
   fluent:
 -----------------------------------------------------------------------
      Versions:
         fluent/2021R2
 

If you need to use a version of FLUENT earlier that R2021R2 then you will have to use the "legacy" software partition.
Infomation on legacy applications can be found here.

**Example Submission Script**
 

The example submission script below is suitable for running on the ARC cluster. This example is customised to ensure FLUENT uses
the ARC supplied OpenMPI libraries instead of those supplied by ANSYS::

  #!/bin/bash

  #SBATCH --partition=devel
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=FluentTest

  module purge
  module load fluent/2021R2
  module load OpenMPI/4.0.5-GCC-10.2.0
  export OPENMPI_ROOT=$EBROOTOPENMPI

  NODELIST="${SLURM_SUBMIT_DIR}/hostlist.${SLURM_JOB_ID}.txt"
  scontrol show hostname ${SLURM_NODELIST} >${NODELIST}

  fluent 2d -g -slurm -t${SLURM_NPROCS} -pinfiniband -mpi=openmpi -cnf=${NODELIST} -i journal.inp

  rm ${NODELIST}

**Running FLUENT interactively (for pre/post processing only)**

In order to pre/post process your data you can run FLUENT on the interactive nodes via an X11 GUI session as follows::

  srun -p interactive --x11 --nodes=1 --ntasks-per-node=48 --mem=128GB --pty /bin/bash
  
.. note::
   If required, you may the resources in the above ``srun`` request. e.g. memory requirements.
  
Once you have been given a resource allocation and a command shell on the interactive node, you can start FLUENT with the GUI::

   module purge
   module load fluent/2021R2
   fluent -pshmem -t${SLURM_NTASKS}
   
  



 
