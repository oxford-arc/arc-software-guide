Legacy Application Software
===========================
 
The ARC cluster environment has a number of compute nodes dedicated to running older "legacy" software applications.
These are applications which are unable to run on the newer operating system installed on the main cluster.
These nodes are kept within a "legacy" partition on the cluster.
 
Currently the main cluster is running CentOS 8.1 and the legacy nodes are running CentOS 7.7
 
The following legacy applications are supported:
 
- ANSYS products v18.2, v19.5, v20.2
- Abaqus 2021
 
You can access the legacy software modules by using the command::
 
  module use /apps/common/legacy/modules

You may then use the module avail command to find the application you require.

Example Submission Scripts
--------------------------

Fluent Example::

  #!/bin/bash

  #SBATCH --partition=legacy
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=FluentTest

  module use /apps/common/legacy/modules
  module load fluent/18.2

  srun hostname > hostfile.txt

  fluent 2d -g -ssh -t${SLURM_NTASKS} -pinfiniband -mpi=intel -cnf=hostfile.txt -i cav.inp
 
For Fluent 19.5 change the module load in the above example to::
 
  module load fluent/2019R3
 
For Fluent 20.2 change the module load to::

  module load fluent/2020R2
 

Abaqus Example::
 
  #!/bin/bash

  #SBATCH --partition=legacy
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=12:00:00
  #SBATCH --job-name=AbaqusTest

  module use /apps/common/legacy/modules

  module load Abaqus/2021
  module load iimpi/2020a

  . abaqus.sh

  abaqus fetch job=s4b.inp 
  abaqus input=s4b job=test cpus=${SLURM_NTASKS} interactive
 

Please note: The line ``. abaqus.sh`` in the above script is important, it ensures that Abaqus is configured correctly for the ARC environment
by creating and populating a configuration file named ``abaqus_v6.env`` in the job directory. It also creates a scratch directory for temporary Abaqus files.
The example above also loads the ``iimpi/2020a`` module which we use to override the outdated MPI libraries supplied.

