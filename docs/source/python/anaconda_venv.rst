Creating your own virtual environment
-------------------------------------

First you should decide which version of Python you wish to use, 2 or 3. There are Anaconda modules available for both versions, the current Anaconda
versions can be found by typing::

module spider anaconda

To load the version of Anaconda you want, in this example version 2019.03, use one of the following commands:

Python 2::

  module load Anaconda2

Python 3::

  module load Anaconda3 

or one of the specific Anaconda versions shown by ``module spider``. 

Once the module is loaded you can use the ``conda`` commands to create a virtual environment in your $DATA area. For example to create an environment named
``myenv`` in $DATA we can use the following commands::

  export CONPREFIX=$DATA/myenv

Python 2::

  conda create --prefix $CONPREFIX --copy python=2.7

Python 3::

  conda create --prefix $CONPREFIX --copy python=3.8

Note: Please ignore any messages from conda which instruct you to run "conda init" - this command will add lines to your ~/.bashrc file which could cause
undesirable behaviour in batch files.

You can now use (activate) the environment by running the following command::

  source activate $CONPREFIX

You can then use the ``conda install`` or ``pip`` commands to install packages. We recommend the use of ``conda install`` where possible to maintain package
version consistency in the virtual environment. For example::

  conda install numpy

or::

  pip install numpy

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

