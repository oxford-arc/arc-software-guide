Compiling and Running MPI Software
==================================

Introduction
------------

This guide is intended to give an overview of what is needed to compile and run MPI software on the ARC cluster systems.

The guide shows how to:

- Compile a MPI application,
- Prepare a job submission script and
- Submit the job.


About MPI
---------

MPI stands for Message Passing Interface, an interface standard that defines a number of library routines aimed at the programming of message-passing
(distributed-processing) applications.  The interface specifications were designed by a group of researchers from both academia and industry and cover
bindings for C, C++ and Fortran.

Being standardised, MPI programming leads to highly portable code.  Nevertheless, the MPI standard has many implementations in libraries (both commercial
and open source software), and the quality and performance of MPI libraries can differ significantly.

Any MPI library implementation has a number of tools that help programmers build and run MPI applications.  The main tools are:

compiler utilities and
an application run agent.

Compiler utilities (mpicc, mpiicc, mpicxx, mpif77, mpif90, mpiifort) are used to compile and link MPI programs.
These are not compilers as such but wrappers around back-end compilers (e.g. the GNU or Intel compilers) and are designed to make compiling
and linking against the MPI library easy.

The run agent launches and manages the execution of a MPI executable on distributed computer systems.  This agent is called mpirun or mpiexec,
with mpirun being the most frequently used one.  

MPI on the ARC systems
----------------------

The ARC clusters have two main MPI implementations installed, however this guide is intended to be independent of any particular flavour of MPI. 
The MPI libraries available per cluster system are presented below.

The MPI implementations OpenMPI and Intel-MPI are installed on the clusters ARC and HTC, are optimised and configured to use the InfiniBand interconnect.
Each MPI implementation has several versions installed, and may be used with different compilers.  All installations are managed through the environment
module system.

 

Preparing and Running An Example
--------------------------------

Preparation

Log in to one of the ARC clusters, create a directory in which to do some work and go to it.  The sequence of commands is::

  cd $DATA
  mkdir examples
  cd examples
 

Then, copy the ARC MPI example files to your newly created directory::

  cp /apps/common/examples/mpi/* .
 
Run the command ``ls`` to list the copied files.  Simple C ``cluster_myprog.c`` and Fortran ``cluster_myprog.f`` MPI example codes are provided.
Also, there is a submission script ``slurm.sh``  You can edit and adapt the submission script for the cluster on which you are running the example.

Compiling the application
-------------------------

The compilation and linking of an MPI program is managed by the compiler wrappers ``mpicc`` and ``mpif77`` for GCC and ``mpiicc`` and ``mpiifort`` for Intel -
and performed by the back-end compiler. The MPI wrapper scripts ensure the correct options for MPI operation are supplied to the compiler.

Toolchains
----------

The ARC and HTC systems have a number of compiler, MPI and maths library combinations grouped into toolchains which are versioned every six months 
(a and b versions). These are based upon the EasyBuild standard toolchain definitions to ensure reproducability. For Intel compilers these are named 
intel and for GCC they are named foss (free open-source software). 

For example the ``intel/2020a`` toolchain contains the following components::

  module load intel/2020a
  module list

  Currently Loaded Modules:
    1) GCCcore/9.3.0               3) binutils/2.34-GCCcore-9.3.0   5) impi/2019.7.217-iccifort-2020.1.217   7) imkl/2020.1.217-iimpi-2020a
    2) zlib/1.2.11-GCCcore-9.3.0   4) iccifort/2020.1.217           6) iimpi/2020a                           8) intel/2020a
 

The ``foss/2020a`` toolchain contains::

  module load foss/2020a
  module list

  Currently Loaded Modules:
    1) GCCcore/9.3.0                 4) GCC/9.3.0                      7) libxml2/2.9.10-GCCcore-9.3.0     10) OpenMPI/4.0.3-GCC-9.3.0   13) FFTW/3.3.8-gompi-2020a
    2) zlib/1.2.11-GCCcore-9.3.0     5) numactl/2.0.13-GCCcore-9.3.0   8) libpciaccess/0.16-GCCcore-9.3.0  11) OpenBLAS/0.3.9-GCC-9.3.0  14) ScaLAPACK/2.1.0-gompi-2020a
    3) binutils/2.34-GCCcore-9.3.0   6) XZ/5.2.5-GCCcore-9.3.0         9) hwloc/2.2.0-GCCcore-9.3.0        12) gompi/2020a               15) foss/2020a
 

Important Note for Intel toolchain users: When using the intel toolchain, the MPI build wrappers ``mpicc``, ``mpicxx`` and ``mpifc`` point to the GCC compilers. To
use the Intel compilers you should use the wrappers: ``mpiicc``, ``mpiicpc`` and ``mpiifort`` respectively. If you are using a third-party build which cannot be
easily modified, you can override the behaviour of the ``mpicc``, ``mpicxx`` and ``mpifc`` wrappers to use Intel compilers by setting the following environment
variables::

  export MPICH_CC=icc

  export MPICH_FC=ifort
  export MPICH_F90=ifort
  export MPICH_F77=ifort

  export MPICH_CPP="icc -E"

  export MPICH_CXX=icpc
  export MPICH_CCC=icpc
 
Other toolchains/versions can be made available, a list of EasyBuild supported versions can be found here. Please note that the ARC systems only support ``foss/2018b``
and newer, and intel/2020a and newer - due to operating system compatibility.

Compilation
-----------

After loading your chosen toolchain module, compile one of the source files:

For the ``foss`` toolchain use::

  mpicc cluster_myprog.c -o cluster_myprog

Or (for the Fortran code)::

  mpif77 cluster_myprog.f -o cluster_myprog

 

For the ``intel`` toolchain use::

  mpiicc cluster_myprog.c -o cluster_myprog

Or (for the Fortran code)::

  mpiifort cluster_myprog.f -o cluster_myprog
 
Run the ``ls`` command to verify the executable cluster_myprog was created.

Preparing the submission script
-------------------------------

Edit the submission script provided ``slurm.sh`` to input the details of the job.  The key lines to pay attention to in the script are:

- the request for resources (number of nodes and walltime) 
- the chosen toolchain and
- the mpirun command.

The submission script should look like this for a foss toolchain build::

 #!/bin/bash

 #SBATCH --job-name=myprog
 #SBATCH --time=00:10:00
 #SBATCH --nodes=2
 #SBATCH --ntasks-per-node=8
 #SBATCH --mail-type=BEGIN,END
 #SBATCH --mail-user=my.name@email.com

 module load foss/2020a

 mpirun ./cluster_myprog
 
or for an ``intel`` toolchain build::

 #!/bin/bash 

 #SBATCH --job-name=myprog 
 #SBATCH --time=00:10:00 
 #SBATCH --nodes=2 
 #SBATCH --ntasks-per-node=8 
 #SBATCH --mail-type=BEGIN,END 
 #SBATCH --mail-user=my.name@email.com

 module load intel/2020a 

 mpirun ./cluster_myprog
 

In this example, SLURM is instructed to allocate 2 nodes ``--nodes=2`` for 10 minutes ``--time=00:10:00``  Also, the run is scheduled for 8 MPI processes per node; this maps each MPI process to a physical core, leading to a (generally) optimal run configuration.

N.B. In ARC there are 48 cores per node but in this example we are only using 8 cores per node.

The command line ``mpirun ./cluster_myprog`` runs the executable ``cluster_myprog`` built with the approprate toolchain MPI library.  

Running the application
-----------------------

After having prepared the submission script, submit the job with::

 sbatch slurm.sh

This will print a job number and return control to the Linux prompt at once.  Monitor its execution using the SLURM ``squeue`` command.

Checking the results
--------------------

After the job is run, you should have two email notifications (one for the start of the job, one for its end) and a couple of extra files in your directory.  The SLURM scheduler will create a single output file, slurm-XXXX.out. [where XXXX is the JobId number]

The output file slurm-XXXX.out should contain the output from the execution, which can be seen by doing for example::

 cat slurm-XXXX.out

The output should look like this (the exact execution of processes is out of order due to the parallelisation)::

 Process  2  received  from process  1
 Process  9  received  from process  4
 Process  1  received  from process  0
 Process  15 received  from process  14
 Process  11 received  from process  10
 Process  13 received  from process  12
 Process  4  received  from process  3
 Process  6  received  from process  5
 Process  12 received  from process  11
 Process  10 received  from process  9
 Process  7  received  from process  6
 Process  8  received  from process  7
 Process  0  received  from process  16
 Process  2  received  from process  1
 Process  3  received  from process  2
 Process  5  received  from process  4
 Process  14 received  from process  13

MPI Core Allocation (and OpenMP)
--------------------------------
 
In the above examples we have used the SLURM ``--ntasks-per-node`` option to allocate a single CPU core to each MPI process.  There may be occasions where we want to run fewer MPI processes per node, and use insead OpenMP for the remaining allocated cores. We can do this using the ``--cpus-per-task`` option.

Below is an example submission script (for OpenMPI) which requests two nodes with 1 MPI process each, where each MPI process can use 8 cores (for OpenMP) - so a total allocation of 16 cores::

 #!/bin/bash

 #SBATCH --nodes=2
 #SBATCH --ntasks-per-node=1
 #SBATCH --cpus-per-task=8
 #SBATCH --time=00:10:00
 #SBATCH --partition=devel

 module load mpitest/1.0

 mpirun --map-by numa:pe=${SLURM_CPUS_PER_TASK} mpisize
 

The command from the ``mpitest module``, named mpisize outputs the following information:

 Hello from host "arc-c303". This is MPI task 1, the total MPI Size is 2, and there are 8 CPU core(s) allocated to *this* MPI task, these being { 0 1 2 3 4 5 6 7 }
 Hello from host "arc-c302". This is MPI task 0, the total MPI Size is 2, and there are 8 CPU core(s) allocated to *this* MPI task, these being { 0 1 2 3 4 5 6 7 }
 

From the results above we can see that as expected, two MPI processes ran, one on node ``arc-c302`` and the other on ``arc-303`` and each of these processes were allocaed 8 CPUs.


Note: The mpirun option ``--map-by numa:pe=${SLURM_CPUS_PER_TASK}`` is not required if running with Intel MPI.

 
