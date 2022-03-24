ANSYS CFX
---------

**Introduction**
 
ANSYS CFX's advanced physics modeling capabilities help engineers solve the most complex challenges in turbomachinery applications.
This powerful software has been extensively validated and is renowned for its robustness and accuracy. 

**Module Information**::
 

  module spider CFX

  -----------------------------------------------------------------------
    cfx: cfx/2021R2
  -----------------------------------------------------------------------

      This module can be loaded directly: module load cfx/2021R2

     Help:
          Adds Ansys CFX 2021R2 to your PATH environment variable

If you need to use a version of CFX earlier that R2021R2 then you will have to use the "legacy" software partition.
Infomation on legacy applications can be found here.

 
**Example Submission Script**
 
The example submission script below is suitable for running on the ARC cluster::

  #!/bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=CFXExample
  #SBATCH --partition=devel

  module load cfx/2021R2
  module load OpenMPI/4.0.5-GCC-10.2.0

  export CFX5_OPENMPI_DIR=$EBROOTOPENMPI

  MPI_HOSTS=$(scontrol show hostnames $SLURM_JOB_NODELIST | tr "\n" "," | sed 's/.$//')

  cfx5solve -def perf_Airfoil_50M_R16.def \
           -double -part-large \
            -part $SLURM_NTASKS -batch -parallel -par-host-list $MPI_HOSTS \
            -start-method "Open MPI Distributed Parallel"
 
.. note::
  This example is customised for the standard ANSYS CFX benchmark Airfoil 50M and uses the OpenMPI libraries built for ARC.
 
 
 
