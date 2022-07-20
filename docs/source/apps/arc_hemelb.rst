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

We have a recipe which you can use to build HemeLB (this has been tested with version 0.8)::

  cd $DATA
  
  export HEME_HOME=$DATA/HemeLB/0.8
  
  module load foss/2020a
  module load CMake/3.16.4-GCCcore-9.3.0
  module load ParMETIS/4.0.3-gompi-2020a
  module load Boost/1.72.0-gompi-2020a
  module load Python/2.7.18-GCCcore-9.3.0

  mkdir -p $HEME_HOME/bin
  mkdir -p $HEME_HOME/lib

  wget http://hemelb.org.s3-website.eu-west-2.amazonaws.com/files/hemelb-v0.8.tar.gz

  tar xvf hemelb-v0.8.tar.gz
  cd hemelb-v0.8

  rm -rf CMakeCache.txt

  mkdir bootstrap_build && cd bootstrap_build
  export CXXFLAGS="-I/usr/include/tirpc"
  export LDFLAGS="-ltirpc"

  cmake -DCMAKE_INSTALL_PREFIX=$HEME_HOME ..
  make -j8

  cd ../dependencies/lib
  cp -r * $HEME_HOME/lib/
  
To use the executable you will need to set the following environment variables::
 
   export HEME_HOME=$DATA/HemeLB/0.8
   export PATH=$HEME_HOME/bin:$PATH
   export LD_LIBRARY_PATH=$HEME_HOME:$LD_LIBRARY_PATH
   
**Example submission script**

This example uses the input data found in HemeLB's ``examples/bifurcation/bifurcation_hires`` directory, this is a version using the ARC module::

  #! /bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --partition=devel
  #SBATCH --time=00:10:00

  module load HemeLB/0.8

  mpirun hemelb -in  input.xml -out output
  
The following is a version for a locally built version::

  #! /bin/bash

  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --partition=devel
  #SBATCH --time=00:10:00
  
  module load foss/2020a
  module load ParMETIS/4.0.3-gompi-2020a
  module load Boost/1.72.0-gompi-2020a
  module load Python/2.7.18-GCCcore-9.3.0

  export HEME_HOME=$DATA/HemeLB/0.8
  export PATH=$HEME_HOME/bin:$PATH
  export LD_LIBRARY_PATH=$HEME_HOME:$LD_LIBRARY_PATH
  
  mpirun hemelb -in  input.xml -out output
  
.. note::
   You need to explicitly include the modules that HemeLB requires in this script (the ARC build module loads these automatically)

  
