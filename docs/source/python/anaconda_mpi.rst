Using MPI with Anaconda
-----------------------
 
The ``mpi4py`` package bundled with, or installed by Anaconda may not work correctly on the ARC cluster. 
The ``mpi4py`` code should be linked to an ARC compiled MPI library on the system - in order to do this in your virtual environment run the following commands:

From the login node, start an interactive session on a compute node - this is important for testing later::

  srun --nodes=1 --ntasks-per-node=4 --partition=interactive --pty /bin/bash

First load the appropriate modules and create your virtual environment::

  module purge
  module load foss/2024a
  module load Anaconda3/2024.02-1

In this example we are using Anaconda3 2020.11 and using OpenMPI 4.0.3 which comes as part of the ``foss/2024a`` toolchain. 

Next we build our virtual environment, and activate it (if you already have your own environment you could use this instead, and simply activate it)::

  conda create --prefix $DATA/mpienv 
  source activate $DATA/mpienv

Now that we have an activated Anaconda virtual environment we can download and install ``mpi4py``, in this case version 3.1.3::

  wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-3.1.4.tar.gz
  tar -zxf mpi4py-3.1.4.tar.gz
  
  cd mpi4py-3.1.4
  python setup.py build --mpicc=`which mpicc` 
  python setup.py install 
  python setup.py clean
 

Assuming the build above completes successfully we can now test the ``mpi4py`` installation.

First create a file called mpihello.py containing the following Python code::

  from mpi4py import MPI
  comm = MPI.COMM_WORLD
  name=MPI.Get_processor_name()
  print("hello world")
  print(("name:",name,"my rank is",comm.rank))

As we are connected to an interactive node, and have four cores allocated (as per the original ``srun`` command) we can test this code as follows::

  mpirun python mpihello.py
 
Note: we must run Python with the ``mpirun`` wrapper in order to execute MPI code. The output from the above command should be::

  hello world
  ('name:', 'arc-c304', 'my rank is', 0)
  hello world
  ('name:', 'arc-c304', 'my rank is', 1)
  hello world
  ('name:', 'arc-c304', 'my rank is', 2)
  hello world
  ('name:', 'arc-c304', 'my rank is', 3)
 
In the above each allocated core has run the code and outputted the string "hello world" and given its hostname and MPI rank.

For a more real world example, we will take the same hello world code and run it in a batch script on multiple nodes in the development partition,
the example submission script is as follows, it should be located in the same directory as ``mpihello.py`` and named ``runmpi.sh`` ::

  #!/bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=4
  #SBATCH --partition=devel
  #SBATCH --job-name=PyHello
  #SBATCH --time=00:10:00

  module purge
  module load Anaconda3/2024.02-1

  module load foss/2024a

  source activate $DATA/mpienv

  mpirun python ./mpihello.py
 

Note: There is no need to specify the number of tasks to the ``mpirun`` command. All ARC built MPI libraries are SLURM aware and are able to determine the task count.

Here you can see we have asked for two development nodes, with four MPI tasks on each node (a total of eight MPI tasks). Note we have also loaded BOTH the
Anaconda3 and foss/2020a modules as used in the mpi4py build.

To submit the job, use the SLURM sbatch command::

  sbatch runmpi.sh

Once the  job completes, the SLURM output file should contain the following information from the job::

  hello world
  ('name:', 'arc-c303', 'my rank is', 4)
  hello world
  ('name:', 'arc-c303', 'my rank is', 5)
  hello world
  ('name:', 'arc-c302', 'my rank is', 0)
  hello world
  ('name:', 'arc-c302', 'my rank is', 1)
  hello world
  ('name:', 'arc-c302', 'my rank is', 2)
  hello world
  ('name:', 'arc-c302', 'my rank is', 3)
  hello world
  ('name:', 'arc-c303', 'my rank is', 6)
  hello world
  ('name:', 'arc-c303', 'my rank is', 7)
 

It can be seen from the above that the MPI processes are running on two hosts: ``arc-c302`` and ``arc-c303`` and there are four MPI ranks per host, 
as specified in the submission script.
