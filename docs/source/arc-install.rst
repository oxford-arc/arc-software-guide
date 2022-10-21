Installing new software applications
====================================

Licensed Software (Commercial or Restricted Use)
------------------------------------------------

There are a number of licensed commercial or restricted use applications already installed on ARC. See our `Restricted Licence Software Applications Form <https://www.arc.ox.ac.uk/restricted-licence-software-applications>`_
for a list.


We can help you install new applications of this type by hosting them centrally and restricting access by project, or you can install them yourself in your
``$DATA`` area following the installation guides provided by the software vendor.

.. warning::

  Do not attempt to run package managers such as ``apt`` or ``yum`` on the ARC systems these will **not** work as they will (by default) attempt to install code into
  protected system directories which you do not have permission to write to. 
  
  If you have such requirements, contact the ARC team via support@arc.ox.ac.uk
    
Open Source Software
--------------------

ARC uses the `EasyBuild framework<http://easybuild.io>`_ to manage central application software installations on the clusters. 

If the package you require is in `this list<https://docs.easybuild.io/en/latest/version-specific/Supported_software.html>`_ we should be able to install this for you reasonably quickly. Use the `ARC Software Installation Request Form <https://www.arc.ox.ac.uk/arc-software-request-page>`_ to request this.

You can also install software in your own ``$DATA`` area using the Easybuild toolchains (compilers and libraries) to satisfy any dependencies that the application may have. If you have any problems contact a member of the ARC team via support@arc.ox.ac.uk

