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

We provide below an example virtual environment build for version 0.37.0 of Qiskit with an appropriate submission script. If you require a different version, specify the version in the variable ```QUISKIT_VER`` You can find available version numbers here: https://pypi.org/project/qiskit/#history

**Virtual Environment Build Steps**::

 srun -p interactive --pty /bin/bash
 
 module purge
 module load Anaconda3/2022.05
 
 export QISKIT_VER=0.37.0
 conda create -y --prefix $DATA/qiskit-$QISKIT_VER-env --copy python=3.9
 source activate $DATA/qiskit-$QISKIT_VER-env
 
 pip install qiskit==$QISKIT_VER


**Example Submission Script**
 

The example submission script below is suitable for running on the ARC cluster ::

  #!/bin/bash

  #SBATCH --partition=devel
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=QiskitTest

  module purge
  module load Anaconda3/2022.05
  
  export QISKIT_VER=0.37.0
  source activate $DATA/qiskit-$QISKIT_VER-env
  
  python (your python script here)
  
.. warning::
   
   If you activate the virtual environment in the submission script, ensure that when you submit your job that no virtual environment is active. i.e. ensure you run ``conda deactivate`` before running ``sbatch``
  
