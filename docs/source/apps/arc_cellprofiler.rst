CellProfiler
------------

**Introduction**
 
CellProfiler is a free, open-source software for quantitative analysis of biological images. No prior experience in programming or computer vision is required

**Module Information**::
 
  module use /apps/common/containers/modules
  module spider CellProfiler

 -----------------------------------------------------------------------------------------------
  CellProfiler:
 -----------------------------------------------------------------------------------------------
     Versions:
        CellProfiler/4.2.1
        CellProfiler/4.2.6



**Interactive CellProfiler Sessions**

In order to use the CellProfler application in GUI mode, connect to a graphical NX node using these instructions: `Connecting to ARC NX nodes <https://arc-user-guide.readthedocs.io/en/latest/connecting-to-arc.html#connecting-using-arc-graphical-nodes>`_

Once connected to an NX desktop session, open a Konsole window and type::

  module purge
  module use /apps/common/containers/modules
  module load CellProfiler/4.2.6

  cellprofiler

The CellProfiler application will then start interactively with full GUI access.

**Non-interactive batch CellProfiler jobs**

The following example SLURM submission script runs CellProfiler in batch (headless) mode. In this case, it assumes you
have downloaded the Fruit Fly cells example `ExampleFly <https://cellprofiler.org/examples>` and are submitting this from the extracted
directory. i.e. the directory containing the ''ExampleFly.cppipe'' piprline file and ''images'' directory. 

For example creating a file named ``run_slurm.sh``

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1
  #SBATCH --cpus-per-task=8
  #SBATCH --time=00:05:00
  #SBATCH --job-name=cellprofiler_test
  #SBATCH --partition=devel

  module purge
  module use /apps/common/containers/modules
  module load CellProfiler/4.2.6

  cellprofiler -p ExampleFly.cppipe -c -r -i images -o output

To submit this to the scheduler::
 
   sbatch run_slurm.sh
   

