Apptainer (Singularity)
-----------------------

.. note::
  This guide is designed to help you get started using Singularity containers on ARC. It is not designed to be a full tutorial for how to use Singularity. 
  However, a set of basic tutorials can be found here: `Singularity Basics - Video Tutorial <https://www.youtube.com/playlist?list=PL052H4iYGzysewYEelldGPOgKRJkxd5zp>`_ 
  
  Singularity is now known as Apptainer - so on later versions of operating system (e.g. Ubuntu 20.04 onwards) you will need to use the command ``apptainer`` 
  rather than ``singularity``
  
**Building a basic container**

The following Singularity definition file configures and builds a container image based on Ubuntu which simply provides an executable installation of the R 
statistical language::

  Bootstrap: docker
  From: ubuntu:22.04

  %post
  # Recommended R installation from cran.r-project.org:
  #
     apt update -y -qq
     apt install -y wget gpg-agent
     apt install -y --no-install-recommends software-properties-common dirmngr
     wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
     add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
  # fix locale
     apt-get install -y locales
     echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
     locale-gen && update-locale LANG=en_US.UTF-8

  # Install r-base
     apt install -y --no-install-recommends r-base

  %runscript
     export LANG=en_US.UTF-8
     export LC_ALL=en_US.UTF-8
     R

To build an image from the above definition file, you need to run singularity on your own workstation (a machine where you have ``sudo`` rights) - you cannot build singularity images on the ARC machines.

**Running a basic container**

So, assuming you have saved the above file as ``r_test.def``, from your linux workstation you should run::

   sudo singularity build /tmp/r_test.simg r_test.def
   
Once the build has completed, you will find that it has built the image file ``/tmp/r_test.simg``

To test this on your workstation run::

      $ singularity run /tmp/r_test.simg

      R version 4.2.2 Patched (2022-11-10 r83330) -- "Innocent and Trusting"
      Copyright (C) 2022 The R Foundation for Statistical Computing
      Platform: x86_64-pc-linux-gnu (64-bit)

      R is free software and comes with ABSOLUTELY NO WARRANTY.
      You are welcome to redistribute it under certain conditions.
      Type 'license()' or 'licence()' for distribution details.

      Natural language support but running in an English locale

      R is a collaborative project with many contributors.
      Type 'contributors()' for more information and
      'citation()' on how to cite R or R packages in publications.

      Type 'demo()' for some demos, 'help()' for on-line help, or
      'help.start()' for an HTML browser interface to help.
      Type 'q()' to quit R.

      [Previously saved workspace restored]

      >
      
The image file ``r_test.def`` generated in the above example, may be copied to the ARC systems and run in the same way.

We have already built this container image, and you can run it on ARC as follows::

   singularity run /apps/common/examples/singularity/containers/r_test.simg


**Directory Binding**

You can bind directories from the ARC environment into your container. 

For example to bind your ARC ``$DATA`` directory into the container as ``/arc_data`` - and set the environment variable ``$DATA`` inside the container to point to 
``/arc_data`` you can use the following options::

   singularity run -B $DATA:/arc_data --env DATA=/arc_data /apps/common/examples/singularity/containers/bind_test.simg

.. note::
   By default Singularity is aware of ``$HOME`` so you do not need to bind this directory.
   
The container image ``bind_test.simg`` used in the above example, was built using the following definition file::

  Bootstrap: docker
  From: ubuntu:22.04

  %post
      apt-get -y update
      apt-get clean

  %runscript
     echo "If you've mounted $HOME it contains:"
     ls $HOME
     echo "If you've mounted $DATA it contains:"
     ls $DATA
     
**Using Singularity with MPI code**

To use singularity with MPI requires that the container image has been built with MPI support as part of its definition. Preferably the MPI type should match that 
being used on the host system (ARC).

To run an MPI container on ARC you simply need to run singularity from the ``mpirun`` wrapper. For example the following will run a pre-built MPI test container on 
ARC::

   #!/bin/bash

   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=4
   #SBATCH --cpus-per-task=2
   #SBATCH --time=00:10:00
   #SBATCH --partition=devel

   module load OpenMPI/4.1.4-GCC-12.2.0

   mpirun singularity run /apps/common/examples/singularity/containers/mpi_test.simg
   
Once submitted with the ``sbatch`` command the output from the above script should look something like the following::

   Hello world from processor arc-c302, rank 0 out of 8 processors
   Hello world from processor arc-c302, rank 1 out of 8 processors
   Hello world from processor arc-c302, rank 2 out of 8 processors
   Hello world from processor arc-c302, rank 3 out of 8 processors
   Hello world from processor arc-c303, rank 7 out of 8 processors
   Hello world from processor arc-c303, rank 6 out of 8 processors
   Hello world from processor arc-c303, rank 4 out of 8 processors
   Hello world from processor arc-c303, rank 5 out of 8 processors

The same container also has another command ``mpisize`` which is useful for debugging MPI resources. This may be run as follows::

   #!/bin/bash

   #SBATCH --nodes=2
   #SBATCH --ntasks-per-node=4
   #SBATCH --cpus-per-task=2
   #SBATCH --time=00:10:00
   #SBATCH --partition=devel

   module load OpenMPI/4.1.4-GCC-12.2.0

   mpirun --map-by numa:pe=${SLURM_CPUS_PER_TASK} singularity exec /apps/common/examples/singularity/containers/mpi_test.simg  /opt/mpisize
   
Here we are using the ``exec`` singularity command to run a specific program ``/opt/mpisize`` inside the container. We also add some options to ``mpirun`` to ensure
the CPU thread binding is correct.

The output from the above script should look something like the following::

   Allocated core list { 0 1 }
   Allocated core list { 4 5 }
   Allocated core list { 2 3 }
   Allocated core list { 6 7 }
   Allocated core list { 6 7 }
   Allocated core list { 0 1 }
   Allocated core list { 4 5 }
   Allocated core list { 2 3 }
   I am MPI task 0, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 1, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 3, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 2, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 5, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 6, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 4, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   I am MPI task 7, the total MPI Size is 8, and there are 2 core(s) allocated to *this* MPI task.
   

**Using GPUs with containers**

Singularity containers may be used with GPU nodes. For this the ``--nv`` flag is used. The ``--nv`` flag will:

 - Ensure that the /dev/nvidiaX device entries are available inside the container, so that the GPU cards in the host are accessible.

 - Locate and bind the basic CUDA libraries from the host into the container, so that they are available to the container, and match the kernel GPU driver on the host.

 - Set the LD_LIBRARY_PATH inside the container so that the bound-in version of the CUDA libraries are used by applications run inside the container.

As an interactive example, we can run the following from ``hpc-login`` on an interactive GPU node::
   
    srun -p interactive --gres=gpu:1 --pty /bin/bash
    srun: GPU gres requested, checking settings/requirements...
    srun: job 2072540 queued and waiting for resources
    srun: job 2072540 has been allocated resources
    
    singularity exec --nv /apps/common/examples/singularity/containers/tensorflow-20.02-tf1-py3.sif python -c 'import tensorflow as tf; print("Num GPUs Available: 
    ",len(tf.config.experimental.list_physical_devices("GPU")))'
    
    2023-03-01 15:26:22.464915: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.2
    2023-03-01 15:26:28.437732: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcuda.so.1
    2023-03-01 15:26:28.456277: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1639] Found device 0 with properties:
    name: Tesla V100-SXM2-16GB major: 7 minor: 0 memoryClockRate(GHz): 1.53
    pciBusID: 0000:1d:00.0
    2023-03-01 15:26:28.456302: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudart.so.10.2
    2023-03-01 15:26:28.695652: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcublas.so.10
    2023-03-01 15:26:28.824502: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcufft.so.10
    2023-03-01 15:26:29.101684: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcurand.so.10
    2023-03-01 15:26:29.294168: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusolver.so.10
    2023-03-01 15:26:29.390364: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcusparse.so.10
    2023-03-01 15:26:29.727534: I tensorflow/stream_executor/platform/default/dso_loader.cc:44] Successfully opened dynamic library libcudnn.so.7
    2023-03-01 15:26:29.728266: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1767] Adding visible gpu devices: 0
    Num GPUs Available:  1




  
     




