Using R-Studio on ARC
---------------------
 
You can use the R-Studio IDE on ARC via an interactive ``X11`` session. This means you will need to connect to ARC via a client running an ``X11`` server such
as MobaXterm for Windows, or XQuartz for Mac.
 
It is necessary to make your SSH connection to the ARC login node with the -X option in order to forward ``X11`` graphics back to your desktop machine - for example::
 
  ssh -X username@arc-login.arc.ox.ac.uk

.. note::
 Mac users may need to use -Y instead of -X if they get security warnings with -X. 

See the **Connecting to ARC Clusters** section of the ARC User Guide for more information.
 
Once connected to a login node, you will need to connect to an interactive session on a compute node::
 
  srun -p interactive --x11 --pty /bin/bash
 
The above line will create an interactive session and ensure that the ``X11`` forwarding is preserved.
 
To run R-Studio you will need to load the appropriate module::
 
  module spider RStudio
 
The above command returns the available versions of R-Studio, for example:
 
---------------------------------------------------------------------------------------------------------------------------------------------------------------
  RStudio: RStudio/2022.02-R-4.2.1-ARC
---------------------------------------------------------------------------------------------------------------------------------------------------------------
 
In the above case, loading the module ``RStudio/2022.02-R.4.2.1-ARC`` will load version 2022.2 of RStudio along with R version 4.2.1 with added ARC libraries.
 
So to begin using the application you will need to type::
 
  module load RStudio/2022.02-R.4.2.1-ARC
  rstudio
 
After a short delay, the R-Studio window should appear on your desktop display.

.. note::
 Mac users may experience problems using the XQuartz X11 server with R-Studio, where the application starts then fails with OpenGL errors. In this case follow the     
 guidance below::
 
  mkdir -p $HOME/.config/RStudio
  touch $HOME/.config/RStudio/desktop.ini

Then edit the file $HOME/.config/RStudio/desktop.ini to contain the following text::

  [General]
  cookies=@Invalid()
  desktop.renderingEngine=software
  general.disableGpuDriverBugWorkarounds=true
  general.ignoreGpuExclusionList=true


The above options ensure that RStudio only uses software graphics rendering rather than OpenGL which seems to give problems with XQuartz.


 
 
