ORCA
----

**Introduction**

ORCA is a flexible, efficient and easy-to-use general purpose tool for quantum chemistry with specific emphasis on spectroscopic properties of open-shell
molecules. It features a wide variety of standard quantum chemical methods ranging from semiempirical methods to DFT to single- and multireference correlated
ab initio methods. It can also treat environmental and relativistic effects.


**Module information**::

  module spider orca 
  
  ----------------------------------------------------------------------------
  ORCA:
  ----------------------------------------------------------------------------
      Versions:
        ORCA/4.2.1-gompi-2019b
        ORCA/5.0.0-gompi-2019b
        ORCA/5.0.1-gompi-2019b-dba
        ORCA/5.0.2-gompi-2019b-dba
        ORCA/5.0.3-gompi-2021b
        ORCA/5.0.4-gompi-2022a
        ORCA/5.0.4-gompi-2023a
        ORCA/6.0.0-gompi-2023a
        ORCA/6.0.1-gompi-2023b
        ORCA/6.1.0-gompi-2024a

        
**Example submission script**::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=12:00:00
  #SBATCH --partition=short
  #SBATCH --job-name=ORCA-Test

  module load ORCA/6.1.0-gompi-2024a

  # ORCA must be called with full pathname, so we use $EBROOTORCA environment variable to help...
  # Note: Versions after 5.0.3 must use $EBROOTORCA/bin/orca previous version use $EBROOTORCA/orca 
  
  $EBROOTORCA/bin/orca input.inp &> output.out

.. note::  
  In the above example script ``input.inp`` should be substituted for the appropriate name of your input file, and the number of nodes and tasks per
  node should be set accordingly.
  
 
