Loading an R Module
-------------------

To use R on the ARC systems you simply need to load the latest R environment module,  
in this example version 4.1.2 - it can be loaded using the following command::
 
  module load R/4.1.2-foss-2021b-ARC
 
To see all versions of R we have available, use the command ::
 
  module spider R 

The base install has many popular R packages installed. Additionally there are modules available with the -ARC suffix
e.g. ``R/4.1.2-foss-2021b-ARC`` these modules load many more R libraries than the base R installation and contains those libraries
most requested by ARC users. It is possible that you will need access to libraries which are not installed in the base or ARC R modules.
You can install R libraries in an R library repository within your storage area (e.g. $HOME or $DATA) please see below.
 
Please note: Some R libraries depend on the existence of non-R applications or other shared binaries. Attempting to install an R library
with binary dependencies may fail. In this case please contact the ARC team and we will install the dependencies for you centrally. 
