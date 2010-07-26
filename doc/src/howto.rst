=================================
FEMhub HowTo: Tips for Developers
=================================
Following tips are useful for developers.

Browse Git Repository
----------------------
FEMhub (script and the build system) repository: http://git.hpfem.org/femhub.git

FEMhub Online Lab repository: git clone http://git.hpfem.org/femhub-lab.git

Libfemhub: http://git.hpfem.org/libfemhub.git

Clone Git Repository
--------------------

To clone the repository of FEMhub (script and the build system):
::
  \$ git clone http://git.hpfem.org/git/femhub.git

To clone the repository of FEMhub Online Lab:
::
  \$ git clone http://git.hpfem.org/git/femhub-lab.git

To clone the reopsitory of Libfemhub:
::
  \$ git clone http://git.hpfem.org/git/libfemhub.git


How to Test Patches
-------------------
Let's say that John asks you to pull the branch called ex_fem from git://github.com/andrsd/femhub.git and review.
First, add the remote link to John's repo by saying:
::
  \$ git remote add john git://github.com/john/femhub.git

Then, create in your repo a new local branch where the patches will be tested. Assuming that you are in your master branch, type:
::
  \$ git checkout -b test-john

Then, fetch John's repo by typing:
::
  \$ git fetch john

Next, merge the branch of interest into your local branch:
::
 \$ git merge john/ex_fem


How to Compile FEMhub from Git
-----------------------
To compile from git (as opposed to the tarball):
::
  \$ git clone http://git.hpfem.org/git/femhub.git
  \$ cd femhub
  \$ ./femhub -d
  \$ make


Creating New FEMhub Release
---------------------------
How to create a new release:
::
  \$ git clone http://git.hpfem.org/git/femhub.git
  \$ cd femhub
  \$ cd spkg/standard/
  \$ ./download_packages
  \$ vim sage_scripts/sage-banner  # edit the version & date in the banner
  \$ git ci -a -m "FEMhub version bumped to 0.9.9"
  \$ git tag femhub-0.9.9
  \$ git push --tags spilka:/home/git/repos/femhub.git master
  \$ cd ../../..
  \$ cp -a femhub femhub-0.9.9
  \$ tar cf femhub-0.9.1.tar femhub-0.9.9


Binary Distribution
-------------------
Unpack the tarball of source code, and rename it (for example, to femhub-0.9.9-ubuntu64 or any platform for which you would like to release the binary). Then build it on that corresponding platform following the instructions above. Immidiately after the build is complete create .tar.gz of that directory. This is the binary version of FEMhub for the particular platform.


Windows
-------
In cygwin, do
::
  make
  local/bin/sage-win-copy

and run femhub by double-cclicking on the `femhub-windows` (bat) file in the root directory. If "http" doesn't work on windows, clone from: git://github.com/certik/femhub.git


Creating FEMhub Package
-----------------------
If you have developed new codes to add new functionality to FEMhub you might want to create a package instead of a regular patch.

FEMhub packages are .tar.bz2 files but they have the extension .spkg to avoid confusion. You can see FEMhub standard packages if go to FEMhub top directory and do 
::
  \$ cd spkg/standard

You can extract an spkg by typing
::
  \$ tar -jxvf packagename-version.spkg

After you extract you will see a script file named ``spkg-install`` which contains the install script. Besides that you may usually see a directory ``src/``

The script ``spkg-install`` is run during installation of the FEMhub package. You can modify spkg-install according to your need.

You may follow the following steps to create a new FEMhub spkg package:

1. First create a directory like this:
::
  \$ mkdir mypackage-version # first the name of your package and then version
Then inside that directory put the script ``spkg-install``, and also create a directory ``src/``. Then put all your source codes within that ``src`` directory. Please see a sample of ``spkg-install`` script below.

2. Then you can create the package by typing:
::
  \$ cd ../    # go out of the mypackage-version directory you just created
  \$ tar cjf mypackage-version.spkg mypackage-version

After you create mypackage-version.spkg you can install it in FEMhub easily. To do so go to FEMhub top directory and type
::
  \$ ./femhub -i path/to/mypackage-version.spkg

A sample ``spkg-install`` script
::
  if [ "$SAGE_LOCAL" = "" ]; then
     echo "SAGE_LOCAL undefined ... exiting";
     echo "Maybe run 'sage -sh'?"
     exit 1
  fi

  PACKAGE_NAME=hermes

  PY_VER=`python -c "import sys;print '%d.%d' % sys.version_info[:2]"`
  echo "Detected Python version: $PY_VER"

  cmake -DCMAKE_INSTALL_PREFIX="$SAGE_LOCAL" \
      -DPYTHON_INCLUDE_PATH="$SAGE_LOCAL/include/python$PY_VER" \
      -DPYTHON_LIBRARY="$SAGE_LOCAL/lib/python2.6/config/libpython2.6.dll.a" \
    .
  if [ $? -ne 0 ]; then
     echo "Error configuring $PACKAGE_NAME."
     exit 1
  fi

  make
  if [ $? -ne 0 ]; then
     echo "Error building $PACKAGE_NAME."
     exit 1
  fi

  make install
  if [ $? -ne 0 ]; then
     echo "Error installing $PACKAGE_NAME."
     exit 1
  fi

Installing SPKG Package
-----------------------
You can install any spkg package in femhub directly by typing
::
  \$ ./femhub -i path/to/spkg-package 

You can install the package directly from the internet too. For example, to install FiPy package you can type
::
  \$ ./femhub -i http://femhub.org/stpack/http:/fipy-2.1-51f1360.spkg

Then you can test whether your package worked correctly in FEMhub. You can test your patches without creating spkg tar by following the instructions below.

Testing Your Patches of FEMhub Package
--------------------------------------
You can test your patches of FEMhub packages without creating spkg tarball by following these steps:
::
 \$ cd mypackage-version
 \$ path_to_femhub/femhub -sh # this launches FEMhub shell
 \$ bash spkg-install
  CTRL+D # exits this shell after the previous command completes
