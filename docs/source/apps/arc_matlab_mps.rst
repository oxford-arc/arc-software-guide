Submitting jobs using the MATLAB Parallel Server
================================================

MATLAB Parallel Server (MPS) allows you to create and use parallel pools that can scale to many CPUs more than in a single node. Currently MPS jobs must be submitted 
from a GUI or command line MATLAB session running on one of the ARC Graphical (NX) nodes. 

We have generated a basic cluster profile definition file for each cluster ARC and HTC. 

Importing the cluster profile
=============================

You need to import the ARC or HTC cluster profile into your MATLAB environment and set it as the default before you can submit MPS jobs. 

This only needs doing once. The imported profile will be saved in your MATLAB settings directory.

Importing the profile can be done either by calling MATLAB functions or via the graphical interface. The profiles are stored here::

  /apps/common/commercial/MATLAB/R2022b/cluster/arc_cluster.mlsettings
  /apps/common/commercial/MATLAB/R2022b/cluster/htc_cluster.mlsettings

Import using MATLAB functions
=============================

Run these functions from a MATLAB session::

   arc_profile = parallel.importProfile ('/apps/common/commercial/MATLAB/R2022b/cluster/arc_cluster.mlsettings');
   parallel.defaultClusterProfile ('arc_cluster');

Importing from MATLAB GUI
=========================

To import using the graphical interface:

From the MATLAB Home tab select the ``Parallel`` menu and click ``Create and Manage Clusters....`` The **Cluster Profile Manager** window will open:


.. image:: ../images/arc-cluster1.png
   :width: 800
   :alt: Cluster Window
  
  
Select ``Import`` and from within the ``Import Profiles from file`` window navigate to the ``arc_cluster.mlsettings`` or ``htc_cluster.mlsettings`` files shown
above and select ``Open``

Select the resulting ``arc_cluster`` or ``htc_cluster`` profile and click ``Set as Default``. 

The Cluster Profile Manager window should now look like this: 


MATLAB Cluster Profile Manager screenshot after


After you exit MATLAB, your default cluster profile is saved for future use.
