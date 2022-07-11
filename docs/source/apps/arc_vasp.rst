VASP
----

**Introduction**

The Vienna Ab initio Simulation Package (VASP) is a computer program for atomic scale
materials modelling, e.g. electronic structure calculations and quantum-mechanical molecular dynamics,
from first principles.

.. warning::
   
   VASP is licensed software and you require a licence to run it. Licensing information can be found here: https://www.vasp.at/
   
   Once you have a valid licence, you need to request access via this form: https://www.arc.ox.ac.uk/restricted-licence-software-applications to request access on ARC.

The guide shows how to:

- prepare a VASP job submission script and
- submit and run a VASP job.

**Module information**::

 module use /apps/common/private/modules
 module spider vasp

     Versions:
        VASP/1.0-info
        VASP/5.4.4-intel2020b
        VASP/6.2.1-foss2020a
        VASP/6.3.2-foss2020a
 
.. note::
   The modules with the suffix ``-info`` should not be loaded.
   

**Running a VASP job**

This example assumes you have the VASP input files in the same directory as the submission script.

An example submission script would look as follows - create a file named ``run-vasp.sh`` containing::

  #!/bin/bash

  #SBATCH --clusters=arc
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=VASP
  #SBATCH --partition=devel

  module purge
  
  module use /apps/common/private/modules
  module load VASP/6.3.2-foss2020a

  mpirun vasp_std
  
The script requires two nodes (48 cores per node) and launches VASP taking the input from the file INCAR

.. note::
   VASP parallelisation is dependent on the simulation you are running see: `VASP Performance Issues <https://www.vasp.at/wiki/index.php/Category:Parallelization`_ for more information. 

To launch into execution, issue the command::

  sbatch run-vasp.sh                                                                                                                                                                  
