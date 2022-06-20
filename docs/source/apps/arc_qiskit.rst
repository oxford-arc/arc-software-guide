Qiskit
------

**Introduction**
 
Qiskit [quiss-kit] is an open-source SDK for working with quantum computers at the level of pulses, circuits, and application modules.

**Module Information**::
 
 module spider Qiskit

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Qiskit: Qiskit/0.23.1-foss-2020a-Python-3.8.2
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
      Qiskit is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.


 

If you need to use a newer version of Qiskit than that installed centrally on the cluster via modules, you may build a Python virtual environment and install it locally in your $DATA area.

**Example Virtual Environment Build**

 srun -p interactive --pty /bin/bash
 
 module purge
 module load Anaconda3/2022.05
 conda create -y --prefix $DATA/qiskit-env --copy python=3.9
 source activate $DATA/qiskit-env
 
 pip install qiskit


**Example Submission Script**
 

The example submission script below is suitable for running on the ARC cluster ::

  #!/bin/bash

  #SBATCH --partition=devel
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=FluentTest

  module purge
  module load Anaconda3/2022.05
  
  source activate $DATA/qiskit-env
  
  python (your python script here)
  
  
