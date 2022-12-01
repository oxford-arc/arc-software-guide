Creating your own virtual environment
-------------------------------------

.. note::
  You must create your conda environments from a SLURM interactive session. So, ensure you have an active interactive session by 
  running::
  
      srun -p interactive --pty /bin/bash
      
  Running conda installations interactively on the login nodes will result in memory errors and other compatibility issues.


You should decide which version of Python you wish to use, 2 or 3. There are Anaconda modules available for both versions, the current 
Anaconda versions can be found by typing::

   module spider anaconda

To load the version of Anaconda you want, in this example we are using the latest version, use one of the following commands:

Python 2::

  module load Anaconda2

Python 3::

  module load Anaconda3 

or one of the specific Anaconda versions shown by ``module spider``. 

Once the module is loaded you can use the ``conda`` commands to create a virtual environment in your **$DATA** area. For example to create an environment named
``myenv`` in **$DATA** we can use the following commands::

  export CONPREFIX=$DATA/myenv

Python 2::

  conda create --prefix $CONPREFIX --copy python=2.7

Python 3::

  conda create --prefix $CONPREFIX 

.. note::
  Please be aware of messages from ``conda`` which instruct you to run ``conda init`` - this command will add lines to your ``~/.bashrc`` file which can in **certain**   
  circumstances cause undesirable behaviour in SLURM batch files. We recommend activating with ``source activate`` if issues occur in batch files.

You can now use (activate) the environment by running one of the following commands::

  source activate $CONPREFIX

or::

  conda activate $CONPREFIX

You can then use the ``conda install`` or ``pip`` commands to install packages. We recommend the use of ``conda install`` where possible to maintain package
version consistency in the virtual environment. For example::

  conda install numpy

or::

  pip install numpy
  
.. warning::
  
  In the above examples we use the ``--prefix`` option to ``conda create`` This is to ensure that the conda virtual environment is placed in ``$DATA``. If you ommit
  this there is a risk that your environment will be placed in the default location which is ``$HOME/.conda/envs`` this will very likely over time cause you to go over 
  quota in your ``$HOME`` area which will cause problems running jobs.
  

Conda Package Cache
-------------------

By default Anaconda will *cache* all packages installed using ``conda install`` into a directory in your ``$HOME`` area named ``~/.conda/pkgs`` before installing them into your virtual environment. Over time this has the potential to put you over quota in ``$HOME``.

If you find yourself over quota in ``$HOME`` check how much space is being used in ``~/.conda/pkgs`` ::
  
  cd ~/.conda
  du -sh pkgs
  
The ``du`` command above may take some time to run. When complete, the command will show how much space is in use in ``pkgs` for example ::

  12G     pkgs
  
In this case 12GB of space is being used by downloaded packages. To tidy up, run the following commands ::

   module load Anaconda3
   conda clean --packages --tarballs
   
You can repeat the ``du`` command above to check that the space has been freed.

Using Anaconda from within a submission script
----------------------------------------------

In order to use your installed virtual environment from a batch script, you will need to load the appropriate Anconda module and activate your environment.
Using values from the above example (and assuming Python version 3, Anaconda 2020/11)::

  # After SBATCH section of script

  module load Anaconda3/2020.11
  source activate $DATA/myenv

  # Your Python commands here...
 

Important Anaconda Information
------------------------------
 

When using Anaconda on the ARC systems, please take note of the following:

- Do not load Anaconda virtual environments automatically on log in from your .bashrc or .bash_profile scripts. These will cause issues to SLURM submitted jobs.

- Ensure you have deactivated the virtual environment BEFORE submitting a SLURM job using sbatch, otherwise you will have issues with packages from your virtual environment not being found.

- You should load all you require from the submission script - as in the submission script example above.

Using Bioconda
--------------

Use the instructions above to create a basic Python Anaconda 2 or 3 virtual environment, then use the following commands
to ensure the bioconda repostories are enabled::

  conda config --add channels defaults
  conda config --add channels bioconda
  conda config --add channels conda-forge
 

Bioconda packages may then be installed by using the ``conda install`` command, for example to install ``bwa``::

  conda install bwa

