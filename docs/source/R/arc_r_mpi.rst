Using Rmpi on ARC
-----------------

Example Rmpi script for SLURM
 
The following is a brief example of how to run an Rmpi script on SLURM. This example uses the latest R version R/4.1.2-foss-2021b
 
Create the following script and save it as ``Rmpi-test.R``::
 
  #
  # Rmpi test
  #
  library("Rmpi")
  
  # Spawn (size-1) slaves, one being resevered for master.
  #
  size <- mpi.universe.size()
  mpi.spawn.Rslaves(nslaves = size - 1)

  # Identify each slave process and display a message
  #
  mpi.bcast.cmd(rank <- mpi.comm.rank())
  mpi.bcast.cmd(size <- mpi.comm.size())
  mpi.bcast.cmd(hostname <- mpi.get.processor.name())
  mpi.remote.exec(paste("This is rank", rank, "of", size, "running on node: ", hostname))

  # Close all slaves and finish
  #
  mpi.close.Rslaves(dellog = FALSE)
  mpi.quit()
 
Now create a submission script called ``submit.sh`` containing the following lines::
 
  #! /bin/bash

  #SBATCH --job-name=mpi-test
  #SBATCH --time=00:10:00
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=8
  #SBATCH --output=rmpi.out
  #SBATCH --partition=devel

  module load R/4.1.2-foss-2021b
  mpirun -np 1 R --vanilla -f Rmpi-test.R
  rm *.log
 
The script above requests at total of 16 processes, where 8 are run on each of 2 nodes. The job is sent to the ``devel`` partition 
(hence maximum 10 minute run time) and the job output is sent to a file named ``rmpi.out``
 
To submit this job, use the command::
 
  sbatch submit.sh
 
After a few minutes the job should complete and a file named ``rmpi.out`` should be created in the
submission directory, this should contain the following output::
 

  $ cat rmpi.out

  R version 4.1.2 (2021-11-01) -- "Bird Hippie"
  Copyright (C) 2021 The R Foundation for Statistical Computing
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

  > #
  > # Rmpi test
  > #
  > library("Rmpi")
  >
  > # Spawn (size-1) slaves, one being resevered for master.
  > #
  > size <- mpi.universe.size()
  > mpi.spawn.Rslaves(nslaves = size - 1)
          15 slaves are spawned successfully. 0 failed.
  master  (rank 0 , comm 1) of size 16 is running on: arc-c266
  slave1  (rank 1 , comm 1) of size 16 is running on: arc-c266
  slave2  (rank 2 , comm 1) of size 16 is running on: arc-c266
  slave3  (rank 3 , comm 1) of size 16 is running on: arc-c266
  ... ... ...
  slave14 (rank 14, comm 1) of size 16 is running on: arc-c267
  slave15 (rank 15, comm 1) of size 16 is running on: arc-c267
  >
  > # Identify each slave process and display a message
  > #
  > mpi.bcast.cmd(rank <- mpi.comm.rank())
  > mpi.bcast.cmd(size <- mpi.comm.size())
  > mpi.bcast.cmd(hostname <- mpi.get.processor.name())
  > mpi.remote.exec(paste("This is rank", rank, "of", size, "running on node: ", hostname))
  $slave1
  [1] "This is rank 1 of 16 running on node:  arc-c266"
  $slave2
  [1] "This is rank 2 of 16 running on node:  arc-c266"
  $slave3
  [1] "This is rank 3 of 16 running on node:  arc-c266"
  $slave4
  [1] "This is rank 4 of 16 running on node:  arc-c266"
  $slave5
  [1] "This is rank 5 of 16 running on node:  arc-c266"
  $slave6
  [1] "This is rank 6 of 16 running on node:  arc-c266"
  $slave7
  [1] "This is rank 7 of 16 running on node:  arc-c266"
  $slave8
  [1] "This is rank 8 of 16 running on node:  arc-c267"
  $slave9
  [1] "This is rank 9 of 16 running on node:  arc-c267"
  $slave10
  [1] "This is rank 10 of 16 running on node:  arc-c267"
  $slave11
  [1] "This is rank 11 of 16 running on node:  arc-c267"
  $slave12
  [1] "This is rank 12 of 16 running on node:  arc-c267"
  $slave13
  [1] "This is rank 13 of 16 running on node:  arc-c267"
  $slave14
  [1] "This is rank 14 of 16 running on node:  arc-c267"
  $slave15
  [1] "This is rank 15 of 16 running on node:  arc-c267"
  >
  > # Close all slaves and finish
  > #
  > mpi.close.Rslaves(dellog = FALSE)
  [1] 1
  > mpi.quit()
 
From the above output you can see the slave processes ran correctly with a total of 16 processes across two ARC compute nodes.
