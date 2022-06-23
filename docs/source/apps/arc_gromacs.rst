GROMACS
-------

**Introduction**

GROMACS is a versatile package for molecular dynamics simulations, which solves the Newtonian equations of motion for systems with hundreds to millions of particles.  GROMACS has been primarily designed for biochemical molecules (such as proteins, lipids and nucleic acids) but has also been used for research on non-biological systems, e.g. polymers.  This is a CPU only build, containing both MPI and threadMPI builds. 

CPU Version::

       GROMACS/2020.4-foss-2020a

GPU versions::

        GROMACS/2020-fosscuda-2019b
        GROMACS/2020.4-foss-2020a-PLUMED-2.6.2
       

The guide shows how to

- prepare a GROMACS job submission script and
- submit the GROMACS job.

**GROMACS on ARC clusters**

Several versions of GROMACS are installed on the ARC clusters, mostly with only single precision support.  GROMACS is managed through the ``module`` utility; use ``module spider gromacs`` to see the modules available, and also use ``module`` to load the appropriate GROMACS version.

**Running a GROMACS job on multi node cluster** 

Here is an example of a submission script GROMACS job on ARC::

  #!/bin/bash 
  
  #SBATCH --nodes=4 
  #SBATCH --ntasks-per-node=48 
  #SBATCH --time=08:00:00 
  #SBATCH --partition=short
  #SBATCH --clusters=arc 

  module purge 
  module load GROMACS/2020.4-foss-2020a  

  mpirun gmx_mpi mdrun -s nsteps800.tpr -deffnm nc2-cubic-md -ntomp 1 -dlb yes -noconfout -npme 64 

Also, here is an example of using a GPU for GROMACS on the htc cluster::  

  #!/bin/bash

  #SBATCH --cluster=htc
  #SBATCH --partition=medium
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1
  #SBATCH --cpus-per-task=5
  #SBATCH --mem=377000
  #SBATCH --gres=gpu:1
  #SBATCH --time=01:00:00

  module purge 
  module load GROMACS/2020.4-fosscuda-2019b 

  mpirun gmx_mpi mdrun -s nsteps800.tpr -deffnm nc2-cubic-md -ntomp 1 -dlb yes -noconfout -npme 64
 
