Using Singularity (Apptainer) on ARC
------------------------------------

.. note::
  This guide is designed to help you get started using Singularity containers on ARC. It is not designed to be a full tutorial for how to use Singularity. 
  However, a set of basic tutorials can be found here: `Singularity Basics - Video Tutorial <https://www.youtube.com/playlist?list=PL052H4iYGzysewYEelldGPOgKRJkxd5zp>`_ 
  
**Building a basic container**

The following Singularity definition file configures and builds a container image based on Ubuntu which simply provides the an executable installation of the R 
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
     




