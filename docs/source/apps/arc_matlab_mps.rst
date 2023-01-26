Submitting jobs using the MATLAB Parallel Server
================================================

MATLAB Parallel Server (MPS) allows you to create and use parallel pools that can scale to many CPUs more than in a single node. Currently MPS jobs must be submitted 
from a GUI or command line MATLAB session running on one of the ARC Graphical (NX) nodes or a session on an interactive node. You **must not** run MPS from a cluster 
login node.

We have generated a basic cluster profile definition file for each cluster ARC and HTC. 

Importing cluster profiles
==========================

You need to import the ARC or HTC cluster profile into your MATLAB environment and set it as the default before you can submit MPS jobs. 

This only needs doing once. The imported profile will be saved in your MATLAB settings directory.

Importing the profile can be done either by calling MATLAB functions or via the graphical interface. The profiles are stored here (for R2022b)::

  /apps/common/commercial/MATLAB/mps_profiles/R2022b

The profiles are configured for specific partitions or resources, as follows:

**devel partition**::

  /apps/common/commercial/MATLAB/mps_profiles/R2022b/arc_devel.mlsettings
  /apps/common/commercial/MATLAB/mps_profiles/R2022b/htc_devel.mlsettings

Import using MATLAB functions
=============================

Run these functions from a MATLAB session::

   arc_profile = parallel.importProfile ('/apps/common/commercial/MATLAB/mps_profiles/R2022b/arc_devel.mlsettings');
   parallel.defaultClusterProfile ('arc_devel');

Importing from MATLAB GUI
=========================

For these examples we will use the ``arc_devel`` profile.

To import using the graphical interface:

From the MATLAB Home tab select the ``Parallel`` menu and click ``Create and Manage Clusters...`` The **Cluster Profile Manager** window will open:


.. image:: ../images/arc-cluster1.png
   :width: 800
   :alt: Cluster Window
  
  
Select ``Import`` and from within the ``Import Profiles from file`` window navigate to the ``arc_devel.mlsettings`` file described
above and select ``Open``

Select the resulting ``arc_devel`` profile and click ``Set as Default``. 

The Cluster Profile Manager window should now look like this: 

.. image:: ../images/arc-cluster2.png
   :width: 800
   :alt: Cluster Imported

.. note::
   After you exit MATLAB, your default cluster profile is saved for future use.
   
To test the loaded profile, click the ``Validate`` button and the validation process will begin. Once the process completes the screen should look as follows:

.. image:: ../images/arc-cluster3.png
   :width: 800
   :alt: Cluster Validation
   
