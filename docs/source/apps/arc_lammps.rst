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

First ensure you are using an interactive session on a compute node::
   
   srun -p interactive --time=02:00:00 --pty /bin/bash

We have a set of build scripts which you can use to build LAMMPS with most of the packages, and its own Anaconda 3 environment. To obtain a copy of these scripts::

  cd $DATA
  mkdir scripts ; cd scripts
  cp -r /apps/common/examples/LAMMPS/2022.07/* .

By default our build script will create the following directories::
  
  $DATA/LAMMPS-env    (Python environment and installation location)
  $DATA/LAMMPS-build  (Build files)
  
If you would like to use different directories, you will need to change the ``$DATA/scripts/LAMMPS-config.sh`` file. Specifically the following two lines::

  export LAMMPS_INSTALL=$DATA/LAMMPS-env
  export LAMMPS_BUILD=$DATA/LAMMPS-build
  
To run the build of LAMMPS::

  cd $DATA/scripts
  sh LAMMPS-build.sh
  
Once the build completes you can test the LAMMPS build by submitting the test job in the ``scripts`` folder as follows::

  sbatch LAMMPS-test.sh
  
The text in the generated SLURM output file ``slurm-nnnnnn.out`` should include the following type of information::

   Testing Python interface...(quick)
   LAMMPS (23 Jun 2022)
     using 1 OpenMP thread(s) per MPI task
   Total wall time: 0:00:00
   
Followed by::

    Testing dipole example run...
    LAMMPS (23 Jun 2022)
       using 1 OpenMP thread(s) per MPI task
    WARNING: Atom style hybrid defines both, per-type and per-atom masses; both must be set, but only per-atom masses will be used (src/atom_vec_hybrid.cpp:133)
    
    ...
    ...
    ...

    Lattice spacing in x,y,z = 1.6903085 1.6903085 1.6903085
    Created orthogonal box = (0 0 -0.84515425) to (16.903085 16.903085 0.84515425)
    6 by 8 by 1 MPI processor grid

    Per MPI rank memory allocation (min/avg/max) = 5.055 | 5.055 | 5.055 Mbytes
       Step          Temp          E_pair         c_erot         TotEng         Press
             0   0             -2.1909822      0             -2.1909822     -2.5750971
    ...
    ...
    ...

    Performance: 23142333.912 tau/day, 53570.217 timesteps/s
    99.3% CPU use with 48 MPI tasks x 1 OpenMP threads
    
    ...
    ...
    ...

    Total # of neighbors = 1650
    Ave neighs/atom = 8.25
    Neighbor list builds = 684
    Dangerous builds = 0
    Total wall time: 0:00:00
 
  
.. note::   
   If you need to change the packages installed you can edit the build script ``$DATA/scripts/LAMMPS-build.sh`` and re-run it.


  

  
