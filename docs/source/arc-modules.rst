Accessing Installed Software Applications
=========================================

Environment Modules
-------------------

The Linux operating system makes extensive use of the "working environment", which is a collection of individual environment variables.  
An environment variable is a named object in the Linux shell that contains information used by one or more applications; two of the most used such variables are **$HOME**, 
which defines a user's home directory name, and **$PATH**, which represents a list paths to different executables.  A large number of environment variables are 
already defined when a Linux shell is open but the environment can be customised, either by defining new environment variables relevant to certain applications 
(e.g. software license variables) or by modifying existing ones (e.g. adding a new path to **$PATH**).

module is a Linux utility, which is used to manage of working environment in preparation for running the applications installed on the ARC systems.  
By loading the module for a certain installed application, the environment variables that are relevant for that application are automatically defined or modified.

The ARC/HTC software environment comprises a mixture of commercial applications, software built using the EasyBuild framework and software built using our own local
build recipes. We use the environment modules system (via the **module** command) to load applications into the environment on ARC/HTC.

However. because the EasyBuild framework adds many new module components into the module list - the best way to search for an application you require
is by using the module spider command. For example, to search for the GROMACS application::

  module spider gromacs

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

Please note, module spider is NOT case-sensitive for searching, so::

  module spider GROMACS
  module spider gromacs
  module spider Gromacs
  
... are all equivalent. However, when loading module using module load you must use the correct case, for example::

  module load GROMACS/2020.4-foss-2020a

 

Please note: It is important to run the module spider command from an interactive compute session because the ARC/HTC login nodes do not have
all modules available. See example below::

  [software@arc-login01 ~]$  srun -p interactive --pty /bin/bash
  srun: CPU resource required, checking settings/requirements...

  [software@arc-c304 ~]$ module spider GROMACS

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GROMACS:
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Description:
      GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the Newtonian equations of motion for systems with hundreds to millions of particles. This is a CPU only
      build, containing
      both MPI and threadMPI builds.

     Versions:
        GROMACS/2020-fosscuda-2019b
        GROMACS/2020.4-foss-2020a-PLUMED-2.6.2
        GROMACS/2020.4-foss-2020a
        GROMACS/2021-foss-2020b
        GROMACS/2021-foss-2021a-PLUMED-2.7.2

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    For detailed information about a specific "GROMACS" package (including how to load the modules) use the module's full name.
    Note that names that have a trailing (E) are extensions provided by other modules.
    For example:

     $ module spider GROMACS/2021-foss-2021a-PLUMED-2.7.2
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

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
 
