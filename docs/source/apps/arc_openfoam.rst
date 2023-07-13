OpenFOAM
------------

**Introduction**

OpenFOAM is a free, open source CFD software package. OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer,
to solid dynamics and electromagnetics.

**Module Information**::
 
   module spider OpenFOAM

   -----------------------------------------------------------------------------------------------------------------
   OpenFOAM
   -----------------------------------------------------------------------------------------------------------------
    Description:
      OpenFOAM is a free, open source CFD software package. OpenFOAM has an extensive range of features to solve anything from complex fluid flows involving chemical reactions, turbulence and heat transfer,
      to solid dynamics and electromagnetics.

     Versions:
        OpenFOAM/v1912-foss-2019b
        OpenFOAM/v2006-foss-2019b
        OpenFOAM/v2006-foss-2020a
        OpenFOAM/v2006-intel-2020a
        OpenFOAM/v2012-foss-2020a
        OpenFOAM/v2106-foss-2021a
        OpenFOAM/v2206-foss-2022a
        OpenFOAM/5.0-20180108-foss-2018b
        OpenFOAM/6-foss-2018b
        OpenFOAM/6-foss-2019b
        OpenFOAM/6-intel-2020a
        OpenFOAM/8-foss-2020a
        OpenFOAM/8-foss-2020b
        OpenFOAM/9-foss-2021a
        OpenFOAM/10-foss-2022a
     Other possible modules matches:
        OpenFOAM-ESI
 

..note::
If you need to use a version of OpenFOAM earlier than version 6 then you will have to use the "legacy" software partition.

**Example Submission Script**
 
The example submission script below is suitable for running on the ARC cluster. This example is customised to enable OpenFOAM to use
4 CPU cores with the standard $FOAM_TUTORIALS/incompressible/simpleFoam/pitzDaily tutorial files::

   #!/bin/bash

   #SBATCH --nodes=1
   #SBATCH --ntasks-per-node=4
   #SBATCH --time=00:10:00
   #SBATCH --partition=devel

   module purge
   module load OpenFOAM/8-foss-2020a

   # Ensure OpenFOAM variables and paths are sourced into environment
   source $FOAM_BASH

   # Prepare case
   echo "Prepare case ..."
   cp -r /apps/common/examples/OpenFOAM/example/pitzDaily .
   cd pitzDaily
   time blockMesh
   # For this example decomposeParDict in pitzDaily/system is set for 4 subdomains.
   decomposePar

   # Run case
   echo "Run case..."
   mpirun simpleFoam -parallel > simpleFoam.out 2>&1

Once successfully run, you will find a directory named ``pitzDaily`` which will contain the case data and the ``simpleFoam.out`` file.   
