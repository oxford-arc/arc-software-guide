Visual Studio Code (VS Code)
----------------------------

**Introduction**

VS Code is a free, open-source, and highly customizable code editor developed by Microsoft. 
It's known for being lightweight and fast, yet powerful, offering features like debugging, syntax highlighting, intelligent code completion, and Git integration. 
VS Code runs on Windows, macOS, and Linux, and is also available as a web-based editor. 

The guide shows how to create a VSCode connection tunnel to access and interact with ARC storage and compute resources from your local VS Code application.

.. warning::
  Please do not use the **Remote SSH** feature of VS Code to connect to the ARC/HTC login nodes for interactive work. This puts unecessary resource load on machines
  which are not configured for such workloads so will slow down your processing considerably.


**Creating a VS Code tunnel**

First, you need to log in to one of the ARC or HTC login nodes. You should do this from a basic SSH session (i.e. from the a client such as PuTTY or from a terminal command line) 

Once you have logged in, you can create a VS Code tunnel using the following command::

  srun --partition=interactive --nodes=1 --cpus-per-task=4 --mem-per-cpu=4G --time=04:00:00 --pty /apps/common/commercial/VSCode/latest/code tunnel

You will then be prompted to select whether to use a **Microsoft Account** or **GitHub Account** to log into Visual Studio Code. You should select your preference and then follow the instructions. 

An example transcript is shown below::

  [teaching70@arc-login03 ~]$ srun --partition=interactive --nodes=1 --cpus-per-task=4 --mem-per-cpu=4G --time=04:00:00 --pty /apps/common/commercial/VSCode/latest/code tunnel
  srun: job 10115727 queued and waiting for resources
  srun: job 10115727 has been allocated resources
  *
  * Visual Studio Code Server
  *
  * By using the software, you agree to
  * the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
  * the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
  *
  ✔ How would you like to log in to Visual Studio Code? · Microsoft Account
  To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code GW4C46F5A to authenticate.


Once you have verified your account using the web browser, you will be given a link to access the tunnel via the web. You will also be able to access the tunnel directly from within the VS Code application - where it can be found under the **Tunnels** section of **Remote Explorer**

.. note::
   You should ensure you request the required resources for the interactive session in the ``srun`` command shown above. This includes requesting GPU resources if required.
                                     
                                     

