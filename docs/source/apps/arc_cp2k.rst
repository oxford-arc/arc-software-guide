CP2K
----

**Introduction**

CP2K is a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, 
and biological systems. CP2K provides a general framework for different modeling methods such as DFT using the mixed Gaussian and plane waves approaches GPW and GAPW. 
Supported theory levels include DFTB, LDA, GGA, MP2, RPA, semi-empirical methods (AM1, PM3, PM6, RM1, MNDO, …), and classical force fields (AMBER, CHARMM, …). CP2K can do 
simulations of molecular dynamics, metadynamics, Monte Carlo, Ehrenfest dynamics, vibrational analysis, core level spectroscopy, energy minimization, and transition state
optimization using NEB or dimer method.


**Module information**::

  module spider CP2K 
  
  ----------------------------------------------------------------------------
  CP2K:
  ----------------------------------------------------------------------------
      Versions:
        CP2K/6.1-foss-2019a
        CP2K/6.1-foss-2019b
        CP2K/6.1-foss-2020a
        CP2K/6.1-intel-2020a
        CP2K/7.1-intel-2020a
        CP2K/7.1-intel-2020b
        CP2K/8.1-foss-2020a
        CP2K/8.2-foss-2021a
        CP2K/9.1-foss-2022a
        CP2K/2023.1-foss-2023a
        
**Example submission script (version 6.1 thru 2023.1) MPI only**::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=12:00:00
  #SBATCH --partition=short
  #SBATCH --job-name=CP2K-Test

  module load CP2K/2023.1-foss-2023a
  export OMP_NUM_THREADS=1

  mpirun cp2k.popt input.inp 

** Example submission script (version 2026.1 onwards) Hybrid OpenMP/MPI**::

  #!/bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=1
  #SBATCH --cpus-per-task=48
  #SBATCH --time=12:00:00
  #SBATCH --partition=short
  #SBATCH --constraint="cpu_gen:Cascade_Lake"
  #SBATCH --job-name=CP2K-Test

  source /apps/system/software/CP2K/cp2k-2026.1/tools/toolchain/install/setup
  export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

  mpirun cp2k.psmp input.inp 


.. note::  
  In the above example scripts ``input.inp`` should be substituted for the appropriate name of your input file, and the number of nodes and tasks per
  node should be set accordingly. Additionally for the Hybrid OpenMP/MPI example, the CPUs per task value will need to be set. 
  
 
