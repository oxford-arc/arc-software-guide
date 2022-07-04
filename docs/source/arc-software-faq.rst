Software FAQs
-------------

 
What software/applications are available on the ARC systems?
A table of some of the software available is given on the Software page.  To obtain a complete list of software available on any particular ARC system,
use the module avail command.

 
What compilers are available on the ARC systems?
The Performance Compilers section of the Software page provides details of currently supported compilers.  ARC currently has Intel C/C++/Fortran compilers
and Portland C/C++/Fortran/CUDA compilers.

 
Do you support application X?
Please check availability of software using this table and/or the module utility.  If you would like us to support applications which are not available yet,
let us know.  Users can also install applications by themselves (in their home directories) if they prefer so, and the ARC staff can assist with this if required.

 
Why do I get "command not found" when I try to run application X?
Applications must be loaded using the module utility.  For example, the command module load intel-compilers loads the Intel compilers, so that executables like icc and ifort are in the path.  Without loading the module, invoking the application leads to a shell error with the message "command not found".

If no version of the module is specified, e.g. as in doing module load intel-compilers, the default is loaded.  You can also load a specific version of a module,
for example module load intel-compilers/2012.

 
How do I run application X as a batch job?
In essence, to run an application, you have to load the appropriate module, prepare a job script for the job scheduler and submit the job to the batch
processing queue. The ARC runs an open-source job scheduler called SLURM Resource Manager.

 
How do I run a MPI application?
mpirun is the command used to start any MPI distributed application on a cluster.  mpirun is one of the utilities that are part of a MPI library and
is responsible for running an application on distributed resources, i.e. launching MPI processes on remote hosts and controlling and managing the communication
between them.  More information can be found on this page, which shows how to compile and run ab MPI application.

 
How do I run an OpenMP application?
OpenMP threaded applications are launched into execution by simply invoking the executable name, without any special launcher.  Depending on the application
and the way it was programmed, the number of execution threads can be set in number of ways.  Typically, the number of OpenMP threads is controlled via the
environment variable OMP_NUM_THREADS, e.g. export OMP_NUM_THREADS=8 sets 8 execution threads.  Nevertheless, there are applications that take this number as
a command line input or read it from an input file.

 
Does my code benefit from hyper-threading?
The proprietary hyper-threading technology (HT) from Intel can be used to boost the performance of most (but not all!) scientific application. For each physical
processor core, the operating system addresses two virtual (or logical) cores through HT, so that the operating system can schedule two concurrent processes or
two threads on the same physical core. Most applications benefit in performance from this technology and where applications see an increase in performance, this
varies from almost no increase to substantial (expecting an increase of 10% is reasonable). For instance, Gromacs can see a increase of up to 16% 
(depending on the problem run). On the other hand Gaussian does not benefit from HT, on the contrary - performance deteriorates slightly. Users are advised
to experiment with their applications to determine if there is a benefit from HT or not
