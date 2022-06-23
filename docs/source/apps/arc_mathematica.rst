Mathematica
-----------

**Introduction**
 
MATLAB is a numerical computing and programming environment with a broad range of functionality (matrix manipulation, numerical linear algebra, general-purpose graphics, etc.).  Additionally, specialised application areas (e.g. bioinformatics or financial derivatives) are served by a large number of optional toolboxes

Matlab is installed on the ARC clusters along with all the toolboxes covered by the Oxford University Concurrent license.

The purpose of this example-based tutorial is to guide the user through a few aspects of running efficient Matlab jobs on the ARC resources.  These aspects are

- using the Mathematica module,
- running Mathematica scripts non-interactively from batch jobs


**Module Information**::
 
 module spider mathematica

 ------------------------------------------------------------------------------------
  Mathematica:
 ------------------------------------------------------------------------------------
     Versions:
        Mathematica/11.3.0
        Mathematica/12.2.0
        Mathematica/13.0.0


**Mathematica Batch Submission**

The following is an example submission script which runs a Mathematica input file named ``test.m``::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --time=01:00:00
  #SBATCH --job-name=MathTest
  #SBATCH --partition=short

  module purge
  module load Mathematica/13.0.0

  math -noprompt -run '<<test.m'

Assuming this script is named ``run_math.sh`` submit this to the scheduler::
 
   sbatch run_math.sh
   

