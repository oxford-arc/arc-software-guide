Java
----

**Introduction**

Java is one of the most popular programming languages, particularly for client-server web applications, often preferred over other options for
faster code development, higher code reliability and easy portability.  Although not often used in scientific programming, Java is nevertheless the
language in which some applications are written (e.g. Beast, a Bayesian MCMC analysis application for molecular sequences) or in which researchers
choose to develop their own codes.

**Module information**::

  module spider java 
  
  ----------------------------------------------------------------------------
  Java:
  ----------------------------------------------------------------------------
      Description:
        Java Platform, Standard Edition (Java SE) lets you develop and deploy
        Java applications on desktops and servers. 

       Versions:
          Java/1.7.0_60
          Java/1.8.0_131
          Java/1.8.0_241
          Java/11.0.2

**Multi-threaded Java applications**

Java applications can benefit from faster execution on modern multi-core machines through using multiple execution threads, and Java provides built-in
support for multithreaded programming.  A multithreaded program contains two or more threads (each defining a separate path of execution) that can run concurrently.
Multi-threaded programming in Java is beyond the scope of this guide and users are invited to start with one of the numerous web tutorials available on the matter,
e.g. [this one.](http://docs.oracle.com/javase/tutorial/essential/concurrency/index.html)


**Example submission script**::

  #!/bin/bash

  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=48
  #SBATCH --time=00:10:00
  #SBATCH --job-name=threadedTest

  module purge

  # Use latest Java version
  module load Java

  myApplication -threads ${SLURM_NTASKS} -input myAppInput.txt -output myAppOutput.txt

 
In the above example, "myApplication", "myAppinput" and "myAppOutput" should be appropriate names for your Java application.
 
