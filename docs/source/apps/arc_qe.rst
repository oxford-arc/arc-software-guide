Quantum ESPRESSO
----------------

**Introduction**

Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale. 
It is based on density-functional theory, plane waves, and pseudopotentials.

The guide shows how to:

- prepare a QE job submission script and
- submit and run a QE job.

**Module information**::

 module spider quantum

      Versions:
        QuantumESPRESSO/6.5-intel-2020a
        QuantumESPRESSO/6.6-foss-2020b
        QuantumESPRESSO/6.6-intel-2020a
        QuantumESPRESSO/6.7-foss-2020b
        QuantumESPRESSO/6.7-intel-2020a

**Running a VASP job**

This example assumes you have the QE input file ``scf.in`` in the same directory as the submission script.

An example submission script would look as follows - create a file named ``run-qe.sh`` containing::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --mem-per-cpu=8000
  #SBATCH --partition=short
  #SBATCH --time=12:00:00
  #SBATCH --job-name=QE-Test

  module purge
  module load QuantumESPRESSO/6.7-foss-2020b

  mpirun pw.x < scf.in > scf.out

To launch into execution, issue the command::

  sbatch run-qe.sh                                        
