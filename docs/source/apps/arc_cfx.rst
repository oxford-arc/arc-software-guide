ANSYS CFX
---------

**Introduction**
 
ANSYS CFX's advanced physics modeling capabilities help engineers solve the most complex challenges in turbomachinery applications.
This powerful software has been extensively validated and is renowned for its robustness and accuracy. 

**Module Information**::
 

  module spider ANSYS

  -----------------------------------------------------------------------
    ANSYS: ANSYS/2024R2
  -----------------------------------------------------------------------


**Example Submission Script**
 
The example submission script below is suitable for running on the ARC cluster::

  #!/bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:15:00
  #SBATCH --job-name=CFXExample
  #SBATCH --partition=short

  module load ANSYS/2024R2

  MPI_HOSTS=$(scontrol show hostnames $SLURM_JOB_NODELIST | tr "\n" "," | sed 's/.$//')

  cfx5solve -def /apps/common/benchmarks/ANSYS/CFX-bench/perf_Airfoil_50M_R16.def \
         -double -part-large \
         -part $SLURM_NTASKS -batch -parallel -par-host-list $MPI_HOSTS \
         -start-method "Open MPI Distributed Parallel"

 
.. note::
  This example is customised for the standard ANSYS CFX benchmark Airfoil 50M and uses the OpenMPI libraries built for ARC.
 
 
 
