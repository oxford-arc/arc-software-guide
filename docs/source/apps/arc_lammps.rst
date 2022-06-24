LAMMPS
------

**Introduction**

LAMMPS is a classical molecular dynamics code, and an acronymfor Large-scale Atomic/Molecular Massively Parallel Simulator. LAMMPS has
potentials for solid-state materials (metals, semiconductors) and soft matter(biomolecules, polymers) and coarse-grained or mesoscopic systems. It can be
used to model atoms or, more generically, as a parallel particle simulator atthe atomic, meso, or continuum scale. LAMMPS runs on single processors or in
parallel using message-passing techniques and a spatial-decomposition of thesimulation domain. The code is designed to be easy to modify or extend with new
functionality.

The guide shows how to

- prepare a LAMMPS with a Python virtual environment and
- submit a test LAMMPS job.

To use LAMMPS you can either use the pre-installed modules or build your own Python virtual environment.

**Using the pre-installed versions of LAMMPS**:: 

   module spider LAMMPS 

        LAMMPS/3Mar2020-foss-2020a-Python-3.8.2-kokkos-QUIP
        LAMMPS/3Mar2020-foss-2020a-Python-3.8.2-kokkos

And load the appropriate version. For example:: 

        module load LAMMPS/3Mar2020-foss-2020a-Python-3.8.2-kokkos

The above will load LAMMPS into your environment, and the package will be available from within Python.

**Setting up your own virtual environment (Python 3)**

We have a build script which you can use to build LAMMPS with most of the packages, and its own Anaconda 3 environment.

The script will create the following directories::
  
  $DATA/LAMMPS-env    (Python environment and installation location)
  $DATA/LAMMPS-build  (Build files)
  
To use this::

  cd $DATA
  mkdir scripts ; cd scripts
  cp /apps/common/examples/LAMMPS/* .
  sh LAMMPS-build.sh
  

  
