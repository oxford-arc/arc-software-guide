Creating Python Virtual Environments on ARC/HPC Clusters
=========================================================

This guide explains how to create and use Python virtual environments on
ARC/HPC systems using **Mamba**, **Anaconda 3**, and **Python 3**.

Legacy **Python 2 / Anaconda 2** instructions are included at the end
for users who still require them.

1. Start from a SLURM Interactive Session
=========================================

You must create Conda or Mamba environments from a SLURM interactive
session.

Start an interactive shell before installing packages or building
environments:

.. code-block:: bash

   srun -p interactive --pty /bin/bash

.. warning::

   Do not run Conda or Mamba installations on login nodes.

Package solving and installation may use large amounts of memory and can
fail on login nodes due to memory limits or compatibility issues.

2. Why Your Virtual Environment Must Be in ``$DATA``
====================================================

On a multi-user HPC cluster, centrally installed Python, Anaconda, and
Mamba software is shared by many users and is usually read-only.

If you attempt to install packages into the shared installation, or into
a location you do not own, you may see errors such as:

.. code-block:: text

   Permission denied

You should therefore create your own virtual environment in your
``$DATA`` area.

Your ``$DATA`` area:

- is user-writable,
- is intended for larger software environments and datasets,
- is more suitable than ``$HOME`` for Conda-style environments.

Conda environments and package caches can become very large over time.

Important
---------

If you omit the ``--prefix`` option, Conda or Mamba may create
environments in a default location such as:

.. code-block:: bash

   $HOME/.conda/envs

This can eventually cause your ``$HOME`` directory to exceed quota
limits, which may prevent jobs or shell sessions from working correctly.

.. important::

   Always create environments under ``$DATA``.

3. Check Available Modules
==========================

First, check which software modules are available:

.. code-block:: bash

   module spider mamba
   module spider anaconda

Load the appropriate module provided on your system.

For example, if a Mamba module is available:

.. code-block:: bash

   module load Mamba

If no separate Mamba module exists, load Anaconda 3:

.. code-block:: bash

   module load Anaconda3

4. Creating a Python 3 Environment with Mamba
=============================================

Step 1 — Define the Environment Location
----------------------------------------

Create an environment path in your ``$DATA`` area:

.. code-block:: bash

   export CONPREFIX=$DATA/myenv

Step 2 — Create the Environment
-------------------------------

Example using Python 3.11:

.. code-block:: bash

   mamba create --prefix $CONPREFIX python=3.11

Step 3 — Activate the Environment
---------------------------------

.. code-block:: bash

   conda activate $CONPREFIX

If ``conda activate`` causes issues in batch scripts, use:

.. code-block:: bash

   source activate $CONPREFIX

Step 4 — Install Packages
-------------------------

Install packages with Mamba where possible:

.. code-block:: bash

   mamba install numpy

If a package is unavailable through Conda/Mamba, use ``pip``:

.. code-block:: bash

   pip install numpy

.. note::

   Prefer ``mamba install`` or ``conda install`` whenever possible, as
   this helps maintain package compatibility.

5. Creating a Python 3 Environment with Anaconda 3
==================================================

Load the Anaconda 3 module:

.. code-block:: bash

   module load Anaconda3

Create an environment in ``$DATA``:

.. code-block:: bash

   export CONPREFIX=$DATA/myenv
   conda create --prefix $CONPREFIX python=3

Activate the environment:

.. code-block:: bash

   source activate $CONPREFIX

or:

.. code-block:: bash

   conda activate $CONPREFIX

Install packages:

.. code-block:: bash

   conda install numpy

or, if necessary:

.. code-block:: bash

   pip install numpy

6. Notes About ``conda init``
=============================

Conda may display messages suggesting that you run:

.. code-block:: bash

   conda init

.. warning::

   Avoid running ``conda init`` on HPC systems.

``conda init`` modifies your ``~/.bashrc`` file and can sometimes cause
problems in SLURM batch jobs.

If activation issues occur in batch scripts, use:

.. code-block:: bash

   source activate $CONPREFIX

instead.

7. Recommended Workflow
=======================

.. code-block:: text

   Login Node
       │
       ▼
   Start Interactive Session
       │
       ▼
   Load Module (Mamba / Anaconda3)
       │
       ▼
   Create Environment in $DATA
       │
       ▼
   Activate Environment
       │
       ▼
   Install Packages
       │
       ▼
   Use Environment in SLURM Jobs

8. Build Script Example
=======================

For reproducibility, it is often better to create a small build script
rather than entering commands manually.

Create a file called ``build_env.sh``:

.. code-block:: bash

   #!/bin/bash

   # Start this script from a SLURM interactive session,
   # not from a login node.

   # Load the required software stack.
   # Use ONE of the following:

   module load Mamba
   # module load Anaconda3

   # Define the environment location.
   export CONPREFIX=$DATA/envname

   # Create the environment.
   mamba create --prefix $CONPREFIX python=3

   # If using Conda instead:
   # conda create --prefix $CONPREFIX python=3

   # Activate the environment.
   source activate $CONPREFIX

   # Install packages.
   mamba install <packagename>

   # Or, if using Conda:
   # conda install <packagename>

Run the script from an interactive session:

.. code-block:: bash

   sh ./build_env.sh

9. Package Cache and ``$HOME`` Quota
====================================

By default, Conda caches packages in:

.. code-block:: bash

   ~/.conda/pkgs

Over time, this directory can become very large and may exceed your
``$HOME`` quota.

Check disk usage:

.. code-block:: bash

   cd ~/.conda
   du -sh pkgs

Example output:

.. code-block:: text

   12G    pkgs

Clean cached packages and tarballs:

.. code-block:: bash

   module load Anaconda3
   conda clean --packages --tarballs

You can re-run:

.. code-block:: bash

   du -sh pkgs

to verify that space has been freed.

10. Using Your Environment in a SLURM Submission Script
=======================================================

Do not rely on environments activated before running ``sbatch``.

Always load modules and activate environments inside the submission
script.

Example Using Anaconda 3
------------------------

.. code-block:: bash

   # After the SBATCH section

   module load Anaconda3/2020.11
   source activate $DATA/myenv

   # Run your code
   python my_script.py

Example Using Mamba
-------------------

.. code-block:: bash

   # After the SBATCH section

   module load Mamba
   source activate $DATA/myenv

   # Run your code
   python my_script.py

11. Important HPC Usage Guidelines
==================================

When using Anaconda, Conda, or Mamba on ARC/HPC systems:

- Do not auto-load environments from ``.bashrc`` or ``.bash_profile``.
- Deactivate environments before submitting jobs with ``sbatch``.
- Load modules and activate environments inside the batch script.
- Create environments in ``$DATA``, not in ``$HOME``.
- Perform installations from interactive compute sessions, not login
  nodes.

12. Using Bioconda
==================

First create a basic Python 3 environment using the instructions above.

Then enable the required channels:

.. code-block:: bash

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge

Install packages with Mamba or Conda.

Example:

.. code-block:: bash

   mamba install bwa

or:

.. code-block:: bash

   conda install bwa

13. Legacy Python 2 / Anaconda 2 Instructions
=============================================

.. warning::

   Python 2 is end-of-life and should only be used for legacy software
   that cannot run under Python 3.

Check available versions:

.. code-block:: bash

   module spider anaconda

Load Anaconda 2 only if required:

.. code-block:: bash

   module load Anaconda2

Create a Python 2.7 environment:

.. code-block:: bash

   export CONPREFIX=$DATA/myenv-py2

   conda create --prefix $CONPREFIX --copy python=2.7

Activate the environment:

.. code-block:: bash

   source activate $CONPREFIX

or:

.. code-block:: bash

   conda activate $CONPREFIX

Install packages:

.. code-block:: bash

   conda install <packagename>

Use these legacy instructions only where Python 2 is unavoidable.

