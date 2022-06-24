CASTEP
------

**Introduction**

CASTEP is an electronic structure materials modelling code based on density functional theory (DFT), 
with functionality including geometry optimization molecular dynamics, phonons, NMR chemical shifts and much more.

.. warning::
   
   While the use of CASTEP is free for University researchers, you still require a licence to run it. Licensing information can be found here: http://www.castep.org/CASTEP/GettingCASTEP
   
   Once you have a valid licence, you need to request access via this form: https://www.arc.ox.ac.uk/restricted-licence-software-applications to request access on ARC.

The guide shows how to:

- prepare a CASTEP job submission script and
- submit and run a CASTEP job.

**Module information**::

 module use /apps/common/private/modules
 module spider castep

     Versions:
        CASTEP/16.11-info
        CASTEP/16.11-intel-2020a
        CASTEP/21.1.1-foss-2019b
        CASTEP/21.1.1-intel-2021b
        CASTEP/21.11-info
 
.. note::
   The modules with the suffix ``-info`` should not be loaded.
   

**Running a CASTEP job**

Here is an example of how to run the Crambin example (part of the CASTEP benchmarks http://www.castep.org/CASTEP/Crambin ) on a cluster node.

An example submission script would look as follows - create a file named ``run-castep.sh`` containing::

  #!/bin/bash

  #SBATCH --clusters=arc
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=CASTEP
  #SBATCH --partition=devel

  module purge
  
  module use /apps/common/private/modules
  module load CASTEP/21.1.1-intel-2021b


  mpirun castep.mpi crambin
  
The script requires two nodes (48 cores per node) and launches CASTEP taking the input from the file ``crambin.cell``

To launch into execution, issue the command::

  sbatch run-castep.sh                                                                                                                                                                  

