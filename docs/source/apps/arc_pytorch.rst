PyTorch
-------

**Using PyTorch environment modules**

There are many PyTorch modules already installed on ARC.

You can find these using the command::

  module spider PyTorch

Those modules with a CUDA suffix need to be run on the HTC cluster in order to benefit from GPU accelleration. 
Please be aware that you should load the module you intend to use on an interactive session, and it will inform you of the GPU compute capability it has been built for. 
This will ensure that you can specify the correct GPU type in your submission script.

For example (from htc-login)::

  srun -p interactive --pty /bin/bash
  
  module load PyTorch/1.12.0-foss-2022a-CUDA-11.7.0
  Note: This PyTorch module supports GPUs with compute capability features up to 8.6 (e.g. V100, A100, RTX8000)
  it will not work with newer GPU generations. Please ensure you have requested the correct GPU generation. 
  See https://arc-user-guide.readthedocs.io/en/latest/job-scheduling.html#gpu-resources

The above message indicates that this module was built for NVidia compute capability 8.6 so if run on newer GPUs such as A100 and H100 it will error and fall-back to CPU operation.


**Building your own PyTorch conda environment**

If you need to add other packages to the PyTorch environment you may find it easier to build your own Anaconda environment.

A base install of PyTorch would be installed with the following script::

  #! /bin/bash
  #
  # Run this script from an interactive session:
  #
  # srun -p interactive --pty /bin/bash
  #
  #
  # It will create a PyTorch 2.11.0 environment GPU enabled with CUDA 13.0
  #
  module load Anaconda3/2025.06-1
  #
  # Change the following to specify the location for the environment:
  #
  export CONPREFIX=$DATA/arc_pytorch
  #
  conda create --prefix $CONPREFIX
  conda activate $CONPREFIX
  conda install pip
  #
  # Base PyTorch install (using info from pytorch.org)
  #
  pip install torch==2.11.0 torchvision==0.26.0 torchaudio==2.11.0 --index-url https://download.pytorch.org/whl/cu130
  #


You can add more packages to this script. You can then execute the script from an interactive session - e.g. assuming you have saved the file as ``arc_env_build.sh``::
 
   [user@htc-login01 ~]$ srun -p interactive --pty /bin/bash
   srun: CPU resource required, checking settings/requirements...
   [user@htc-g040 ~]$ sh ./arc_env_build.sh

To test this environment, you need to create a session on an interactive GPU node. An easy way to to this is as follows::

   [user@htc-login01 ~]$ srun -M htc -p interactive --gres=gpu:1 --pty /bin/bash
   srun: CPU resource required, checking settings/requirements...
   [user@htc-g048 ~]$ module load Anaconda3/2025.06-1
   [user@htc-g048 ~]$ export CONPREFIX=$DATA/arc_pytorch
   [user@htc-g048 ~]$ conda activate $CONPREFIX

As the PyTorch binary installed by ``pip`` will be built for specific CUDA compute capabilities, when the environment is active you can run 
the following command to ascertain which compute capabilities the environment requires::

  [user@htc-g048 ~]$ python /apps/common/bin/pytorch-gpu-cc.py
  GPU resources with following compute capabilities are not present in the ARC cluster: 12.0
  #SBATCH --constraint="gpu_cc:7.5|gpu_cc:8.0|gpu_cc:8.6|gpu_cc:9.0|gpu_cc:10.0"

The above result lets you know that in this case (your output may differ) PyTorch is built for compute capabilities 7.5, 8.0, 8.6, 9.0, 10.0 and 12. The code warns that ARC do not have any CC 12.0 machines. It then provides you with the correct constraint line to add to your
SLURM submission script.

.. note::

  If you rebuild the environment and update PyTorch, you should re-run the ``pytorch-gpu-cc.py`` script above and update the constraints as 
  appropriate in your submission script. 
  

To use the environment from a batch submission script, after the your resource definition ``#SBATCH`` lines add::

   module load Anaconda3/2025.06-1
   export CONPREFIX=$DATA/arc_pytorch
   conda activate $CONPREFIX

  ...your python command here...

.. note::

  You MUST deactivate any active conda environment from your shell BEFORE running the ``sbatch`` command to submit your job - otherwise your job may fail. 



  

