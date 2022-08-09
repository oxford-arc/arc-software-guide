Accessing Installed Software Applications
=========================================

Environment Modules
-------------------

The Linux operating system makes extensive use of the "working environment", which is a collection of individual environment variables.  
An environment variable is a named object in the Linux shell that contains information used by one or more applications; two of the most used such variables are **$HOME**, 
which defines a user's home directory name, and **$PATH**, which represents a list paths to different executables.  A large number of environment variables are 
already defined when a Linux shell is open but the environment can be customised, either by defining new environment variables relevant to certain applications 
(e.g. software license variables) or by modifying existing ones (e.g. adding a new path to **$PATH**).

``module`` is a Linux utility, which is used to manage of working environment in preparation for running the applications installed on the ARC systems.  
By loading the module for a certain installed application, the environment variables that are relevant for that application are automatically defined or modified.

The ARC/HTC software environment comprises a mixture of commercial applications, software built using the EasyBuild framework and software built using our own local
build recipes. We use the environment modules system (via the ``module`` command) to load applications into the environment on ARC/HTC.

However. because the EasyBuild framework adds many new module components into the module list - the best way to search for an application you require
is by using the ``module spider`` command. 

.. note::
   The ARC cluster login nodes reference a **different** set of modules than the main cluster, so to be sure that the module (or module version) you require is available for use on ARC you should **always** search for modules in an interactive session on a compute node. e.g::
       
       [software@arc-login01 ~]$ srun -p interactive --pty /bin/bash
       srun: CPU resource required, checking settings/requirements...
       
       [software@arc-c304 ~]$ module spider <name>

So, for example, to search for the GROMACS application::

  [software@arc-login01 ~]$ srun -p interactive --pty /bin/bash
  srun: CPU resource required, checking settings/requirements...

  [software@arc-c304 ~]$ module spider gromacs

  ------------------------------------------------------------------------------------------------------------------------------
    GROMACS:
  ------------------------------------------------------------------------------------------------------------------------------
    Description:
      GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for
      systems with hundreds to millions of particles. This is a CPU only build, containing both MPI and threadMPI builds.

     Versions:
        GROMACS/2020-fosscuda-2019b
        GROMACS/2020.4-foss-2020a-PLUMED-2.6.2
        GROMACS/2020.4-foss-2020a

.. note::
   ``module spider`` is NOT case-sensitive for searching, so::

     module spider GROMACS
     module spider gromacs
     module spider Gromacs
  
   ...are all equivalent. However, when loading module using module load you must use the correct case, for example::

     [software@arc-c304 ~]$ module load GROMACS/2020.4-foss-2020a

 
If the software name you are using in "module spider" returns too many options you can use ::

  module -r spider '^name' 
  
for example::

  module -r '^Python'  
  module -r ^R$'
 
You can also build your own software in your home or data directories using one of the compilers provided (which are also available through
the environment modules system). Typically the compiler toolchains, including maths libraries and MPI can be loaded using the modules named
foss (e.g. foss/2020a) for free open-source software (i.e. GCC) or intel (e.g. intel/2020a) for the Intel compiler suite.

If no version is specified, the default version of the software is loaded (usually the latest version)::

  module load GROMACS
  module list GROMACS

  Currently Loaded Modules Matching: GROMACS
    1) GROMACS/2020.4-foss-2020a

Specific versions, other than the default can be loaded by specifying the version::

  module load GROMACS/2020.4-foss-2020a-PLUMED-2.6.2
  module list GROMACS

  Currently Loaded Modules Matching: GROMACS
    1) GROMACS/2020.4-foss-2020a-PLUMED-2.6.2
 

A module can be "unloaded" with the unload option, for example::

  module unload MATLAB/2020b 
 
Building software against installed modules
-------------------------------------------

If you need to compile your own software but would like to use an ARC built module for its libraries/headers. You need to make use of the ``EBROOT`` environment variable which is defined when you load the module. For example: if you need to build against the ``Boost`` libraries you first need to load the module::

   module load Boost/1.79.0-GCC-11.3.0
   
Loading the above will define ``EBROOTBOOST`` - the variable name is always ``EBROOT`` followed by the main module name - this environment variable will contain the path to the Boost software for this specific module::

   echo $EBROOTBOOST
   /apps/system/easybuild/software/Boost/1.79.0-GCC-11.3.0
   
   ls $EBROOTBOOST
   easybuild  include  lib  lib64

So if you need to specify the Boost location to your build, you can supply for example: ``$EBROOTBOOST/include`` for the header files and ``$EBROOTBOOST/lib64`` for the library files. 

