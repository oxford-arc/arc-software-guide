Gaussian
--------

**Introduction**

Gaussian is a commercial computational chemistry software for modelling electronic structures. Gaussian provides state-of-the-art capabilities for electronic structure modeling. Gaussian 16 is licensed for a wide variety of computer systems. All versions of Gaussian 16 contain every scientific/modeling feature, and none imposes any artificial limitations on calculations other than your computing resources and patience. 

The guide shows how to:

- prepare a Gaussian job submission script and
- submit and run a Gaussian job.

**Module information**::

 module spider gaussian

     Versions:
        Gaussian/03.E.01-ARCUS-B
        Gaussian/09.D.01-ARCUS-B
        Gaussian/16.A.03-ARCUS-B

        Gaussian/16.C.01
 
The modules with the suffix ``-ARCUS-B`` are the built from the legacy ARCUS-B system, using PGI 16.5 compiler and Atlas. The other modules are built natively on ARC.
 
Note: While the use of Gaussian is free for University researchers, the ARC team has to enable users to run Gaussian on an individual basis; if you are planning to run Gaussian, let the ARC team know, otherwise you will see the message permission denied when tryiing to run Gaussian commands in a submission script. 


**Gaussian on the ARC systems**

Gaussian 03 , Gaussian 09 and Gaussian 16 are available on all the ARC systems and were built from source.  They can be loaded using one of the following commands::

  module load Gaussian/16.A.03-ARCUS-B
  module load Gaussian/09.D.01-ARCUS_B
  module load Gaussian/03.E.01-ARCUS-B
  module load Gaussian/16.C.01
 

Gaussian is a multi-threaded application and users are advised to take advantage of this feature as it leads to a faster execution.  Running Gaussian multi-threaded is controlled from the header of the Gaussian com input files.

**Running a Gaussian job**

Here is an example of how to run the valinomycin test (part of the Gaussian distribution) on a cluster node.

First, load the Gaussian 09 module::

  module load Gaussian/16.A.03-ARCUS-B

Then, edit the file test397.com to set the number of threads.  This should be set to match the availability of cores per compute node, which in the case of ARC is 48.

  %NProcShared=48 
 
An example submission script would look as follows - create a file named ``run-g16.sh`` containing::

  #! /bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=01:00:00
  #SBATCH --job-name=testGaussian
  #SBATCH --partition=short

  module load Gaussian/16.A.03-ARCUS-B

  g16 < test397.com > test397.log
 

The script requires one node, launches Gaussian 16 taking the input from the file ``test397.com`` and redirects the standard output to the file ``test397.log``.

To launch into execution, issue the command::

  sbatch run-g16.sh                                                                                                                                                                  

 

**Gaussview**

The Gaussview software is also installed on the ARC clusters for convenience. You should use one the interactive nodes to run Gaussview. However, we recommend that the desktop version of Gaussview is used to prepare input for Gaussian, as running graphical applications across the network is less efficient. The Department of Chemistry has a site licence for Gaussview and can be contacted for details at the following email address: help@itsupport.chem.ox.ac.uk
