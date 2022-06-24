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

We have a set of build scripts which you can use to build LAMMPS with most of the packages, and its own Anaconda 3 environment. To obtain a copy of these scripts::

  cd $DATA
  mkdir scripts ; cd scripts
  cp /apps/common/examples/LAMMPS/2022.06/* .

By default our build script will create the following directories::
  
  $DATA/LAMMPS-env    (Python environment and installation location)
  $DATA/LAMMPS-build  (Build files)
  
If you would like to use different directories, you will need to change the ``$DATA/scripts/LAMMPS-config.sh`` file. Specifically the following two lines::

  export LAMMPS_INSTALL=$DATA/LAMMPS-env
  export LAMMPS_BUILD=$DATA/LAMMPS-build
  
To run the build of LAMMPS::

  cd $DATA/scripts
  sh LAMMPS-build.sh
  
Once the build completes you can test the build as follows::

   source $DATA/scripts/LAMMPS-config.sh
   python
   >>> import lammps
   >>> lmp = lammps.lammps()
       LAMMPS (18 Sep 2020)
       using 1 OpenMP thread(s) per MPI task
   >>>
   
If you need to change the packages installed you can edit the build script ``$DATA/scripts/LAMMPS-build.sh`` and re-run it.


  

  
