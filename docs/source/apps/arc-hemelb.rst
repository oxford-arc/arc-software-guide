HemeLB
------

**Introduction**

HemeLB is a high performance lattice-Boltzmann solver optimized for simulating blood flow through sparse geometries, such as those found in the human vasculature.
It is routinely deployed on powerful supercomputers, scaling to hundreds of thousands of cores even for complex geometries . HemeLB has traditionally been used
to model cerebral bloodflow and vascular remodelling in retinas , but is now being applied to simulating the fully coupled human arterial and venous trees.

The guide shows how to

- run HemeLB using a pre-compiled module;
- build HemeLB yourself;
- submit a test HemeLB job.

To use HemeLB you can either use the pre-installed modules or build your own verion in your project ``$DATA`` area.

**Using the pre-installed versions of HemeLB**:: 

   module spider HemeLB 

        HemeLB/0.8
        
And load the appropriate version. For example:: 

        module load HemeLB/0.8

The above will load HemeLB into your environment, and the package will be available to run via ``mpirun``.

**Building your own version of HemeLB from source**

First ensure you are using an interactive session on a compute node::
   
   srun -p interactive --time=02:00:00 --pty /bin/bash

We have a recipe which you can use to build HemeLB with most of the packages::

  cd $DATA
  
  module load foss/2020a
  module load CMake/3.16.4-GCCcore-9.3.0
  module load ParMETIS/4.0.3-gompi-2020a
  module load Boost/1.72.0-gompi-2020a
  module load Python/2.7.18-GCCcore-9.3.0

  mkdir -p $DATA/HemeLB/0.8/bin
  mkdir -p $DATA/HemeLB/0.8/lib

  wget http://hemelb.org.s3-website.eu-west-2.amazonaws.com/files/hemelb-v0.8.tar.gz

  tar xvf hemelb-v0.8.tar.gz
  cd hemelb-v0.8

  rm -rf CMakeCache.txt

  mkdir bootstrap_build && cd bootstrap_build
  export CXXFLAGS="-I/usr/include/tirpc"
  export LDFLAGS="-ltirpc"

  cmake -DCMAKE_INSTALL_PREFIX=$DATA/HemeLB/0.8 ..
  make -j8

  cd ../dependencies/lib
  cp -r * $DATA/HemeLB/0.8/lib/
  
  


  

  
