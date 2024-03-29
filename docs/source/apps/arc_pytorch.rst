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
  # It will create a PyTorch 2.0.1 environment GPU enabled with CUDA 11.7
  #
  module load Anaconda3/2022.10
  # Change the following to specify the location for the environment:
  #
  export CONPREFIX=$DATA/arc_pytorch
  #
  conda create --prefix $CONPREFIX
  conda activate $CONPREFIX
  #
  # Base PyTorch install
  #
  conda install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
  #

You can add more packages to this script. You can then execute the script from an interactive session - e.g. assuming you have saved the file as ``arc_env_build.sh``::
 
   [user@htc-login01 ~]$ srun -i interactive --pty /bin/bash
   srun: CPU resource required, checking settings/requirements...
   [user@htc-g040 ~]$ sh ./arc_env_build.sh

To use the environment from a batch submission script, after the resource definition ``#SBATCH`` lines add::

   module load Anaconda3/2022.10
   export CONPREFIX=$DATA/arc_pytorch
   conda activate $CONPREFIX

  ...your python command here...

..note..:

  You MUST deactivate any active conda environment from your shell BEFORE running the ``sbatch`` command to submit your job - otherwise your job may fail. 



  

