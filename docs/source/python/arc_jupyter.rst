Using Jupyter Notebooks on ARC
------------------------------

**Interactive Notebook example**
 
The following example shows how to connect to a Jupyter notebook session running on ARC. The example shows the best practice method of running
the Jupyter session on an interactive node.

.. note::
 We make the assumption that you are already connected to the university network or VPN. We also strongly recommend using MobaXterm as the SSH
 client if using Windows for this activity.

1) First we need to log in to an ARC login node, for this example we are using ``arc-login.arc.ox.ac.uk`` and start an interactive session using
the standard ``srun`` command::

  srun --nodes=1 --ntasks-per-node=4 --partition=interactive --pty /bin/bash
 
Once the ``srun`` allocation is started on the interactive node (for example: ``arc-c304``) you will get a command prompt and can load the Anaconda module
and start Jupyter with the options shown below::

  module load Anaconda3/2021.11
  jupyter notebook --no-browser --ip=*
  
.. note::
 It is essential to use Anaconda3 version 2021.11 or newer for notebooks to work on ARC
 
The response from Jupyter will be of the following form::

  [W 16:01:05.472 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
  [W 2022-03-24 16:01:05.689 LabApp] 'ip' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
  [W 2022-03-24 16:01:05.689 LabApp] 'ip' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
  [W 2022-03-24 16:01:05.689 LabApp] 'ip' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
  [I 2022-03-24 16:01:05.695 LabApp] JupyterLab extension loaded from /apps/system/easybuild/software/Anaconda3/2021.11/lib/python3.9/site-packages/jupyterlab
  [I 2022-03-24 16:01:05.695 LabApp] JupyterLab application directory is /apps/system/easybuild/software/Anaconda3/2021.11/share/jupyter/lab
  [I 16:01:05.699 NotebookApp] Serving notebooks from local directory: /home/ouit0554
  [I 16:01:05.699 NotebookApp] Jupyter Notebook 6.4.5 is running at:
  [I 16:01:05.699 NotebookApp] http://arc-c305:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf
  [I 16:01:05.699 NotebookApp]  or http://127.0.0.1:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf
  [I 16:01:05.699 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
  [C 16:01:05.704 NotebookApp]

      To access the notebook, open this file in a browser:
          file:///home/ouit0554/.local/share/jupyter/runtime/nbserver-2598622-open.html
      Or copy and paste one of these URLs:
         http://arc-c305:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf
      or http://127.0.0.1:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf

.. note::
  In the above output, the last few lines contain key information. You will use the information from the last two lines to make a connection to the jupyter server. 
  
  In our example above we can see (from the penultimate line) that the server is running on node arc-c305 and the port is 8888::
   http://arc-c305:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf
  
  We are also given a URL for accessing the notebook in your local browser (on the last line). For example::
   http://127.0.0.1:8888/?token=1f4df891d02d913a7b926203a978c0b3060113c1607527bf
  
  These values **will** be different for each run and you must make a note of them.

You can now minimise (but do not close) your SSH window to the interactive session above.

We now need to tunnel the Jupyter port we have just created to your local desktop. 

Open new terminal window on your local machine...

The format of the command we need to run to make the tunnel is as follows, but you will need to make changes::
 
  ssh -L 8888:arc-c305:8888 ouit0554@arc-login.arc.ox.ac.uk
 
In the above you will need to substitute the server node and port number from the above information and also use your username before the @ character in the connection
to ``arc-login.arc.ox.ac.uk``
 
For clarity here is an explanation of the fields in the above command::
 
  ssh -L [local port]:[remote host]:[remote port] [ARC username]@arc-login.arc.ox.ac.uk
  
You will be asked to enter your ARC password, and once authenticated the tunnel will be set up and you should be able to use the URL from the original Jupyter output 
on your local browser to connect to the server running on ARC.

.. note::
  It is possible that when making the connection above you receive a "port in use" error on your local machine. In which case you should change the first port number
  in the SSH command, and also change this in the web URL.
  
  



