TensorFlow
----------

**Introduction**

TensorFlow™ is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, 
while the graph edges represent the multidimensional data arrays (tensors) communicated between them.

TensorFlow was originally developed by researchers and engineers working on the Google Brain Team within Google's Machine Intelligence research organization
for the purposes of conducting machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other
domains as well.

TensorFlow is capable of taking advantage of the GPU nodes in the ARC HTC cluster

The guide shows how to

- prepare a TensorFlow Anaconda virtual environment and
- submit a test TensorFlow job.

To use tensorflow you can either use the pre-installed modules or build your own Python virtual environment.

**Using the pre-installed versions of Tensorflow**:: 

   module spider Tensorflow 

        TensorFlow/1.15.2-fosscuda-2019b-Python-3.7.4
        TensorFlow/2.1.0-foss-2019b-Python-3.7.4
        TensorFlow/2.3.1-foss-2020a-Python-3.8.2
        TensorFlow/2.4.1-fosscuda-2020b

And load the appropriate version. For example:: 

        module load TensorFlow/2.4.1-fosscuda-2020b

The above will load Tensorflow 2.4.1 into your environment, and the package will be available from within Python.

**Setting up your own virtual environment (Python 3)**

Tensorflow is best run on the HTC systems which have GPU nodes. The following commands show how you can set up an Anaconda virtual environment
for TensorFlow. Note: this method will only work on HTC nodes, and the environment build process should be run from an interactive session...::

  srun -p interactive --pty /bin/bash

  module load Anaconda/2020.11
  module load CUDA/11.1.1-GCC-10.2.0
  module load cuDNN/8.0.4.30-CUDA-11.1.1

  export CONPREFIX=$DATA/tensor-env
  mkdir $CONPREFIX 
  conda create --prefix $CONPREFIX --copy python=3.8

  source activate $CONPREFIX
  conda install tensorflow-gpu
 

A bash script for submission to GPU nodes will be something like this::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=1
  #SBATCH --time=00:10:00
  #SBATCH --job-name=tensor
  #SBATCH --cluster=htc
  #SBATCH --gres=gpu:1

  # Useful job diagnostics
  #
  echo "CUDA Devices(s) allocated: $CUDA_VISIBLE_DEVICES"
  nvidia-smi
  #
  source activate $DATA/tensor-env

  python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_s um(tf.random_normal([1000, 1000])))"

.. note::
    The job diagnostic information is useful if you need to contact ARC support if you have problems running your job - so please include it.

.. warning::
    You cannot run TensorFlow in GPU mode directly from the login nodes. This will result in errors - as these systems have no GPUs available, and they are restricted     in memory.
  
  
