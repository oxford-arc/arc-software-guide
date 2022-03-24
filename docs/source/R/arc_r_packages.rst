Installing packages into your own R library
-------------------------------------------

As this is an interactive process which may involve building software, it needs to be performed on an interactive node, so first
start an interactive session::
 
  srun -p interactive --pty /bin/bash
 
In order to use your own R library repository, you need to define an environment variable named ``R_LIBS`` containing the path to your
local packages (this will need to be available each time you intend to use your local library, so you may wish to place it in your ``$HOME/.bash_profile`` file) ::
 
  export R_LIBS=~/local/rlibs

Please note: If you do not place the above line in your ``$HOME/.bash_profile`` file, you will need to ensure you include it in your
submission scripts in order for R to find your locally installed libraries.

You can then create this folder (Note: this only needs to be done once)::

  mkdir -p ~/local/rlibs

Once this is done you can start R and run the ``install.packages`` command to install into this local library repository - or indeed follow
the instructions given for a particular package. As an example to install the latest ``devtools`` package::

  [user@arc-c001]$ R

  R version 4.0.2 (2020-06-22) -- "Taking Off Again"
  Copyright (C) 2020 The R Foundation for Statistical Computing
  Platform: x86_64-pc-linux-gnu (64-bit)

  R is free software and comes with ABSOLUTELY NO WARRANTY.
  You are welcome to redistribute it under certain conditions.
  Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

  R is a collaborative project with many contributors.
  Type 'contributors()' for more information and
  'citation()' on how to cite R or R packages in publications.

  Type 'demo()' for some demos, 'help()' for on-line help, or
  'help.start()' for an HTML browser interface to help.
  Type 'q()' to quit R.

  > install.packages("devtools", lib="~/local/rlibs")
 

For packages such as ``BiocManager`` you will need to add the lib location to both the ``BiocManager`` installation and subsequent
``BiocManager::install`` commands for example::

  if (!requireNamespace("BiocManager", quietly = TRUE))
      install.packages("BiocManager", lib="~/local/rlibs")

  BiocManager::install("dada2", version = "3.11", lib="~/local/rlibs")
 
 
You may find you need to use the ``http`` URL protocol rather than ``https`` for some repositories.

Important note: As some R libraries require compilation in order to be installed, it is worth noting that the interactive
nodes share the same CPU architecture as the majority of ARC/HTC compute nodes but not the login nodes. This allows users to
optimise their compiled code to make use of the most recent CPU features. However, if you attempt to load a library built on the
interactive nodes from the login nodes or older compute nodes you may see execution errors such as "Illegal instruction" or 
"Illegal Operand" - these errors are simply warning you that the CPU cannot understand the more recent instructions the compiler has generated. 

To mitigate the above issue:

- If you want to test the library interactively, please ensure you use an interactive node - not a login node for this purpose.

- If you submit a batch job, ensure that you specify::

  #SBATCH --constraint='cpu_gen:Cascade_Lake'

The above will ensure your job runs on a node with the same architecture as the interactive node you used to build the library.

