Hello,

This README.txt describes build instruction for Femhub. If you downloaded
a binary, you do not need to do anything, just execute

 ./femhub

from the command line and you are good to go.

$ ./femhub
----------------------------------------------------------------------
| Femhub (FEM Distribution), Version 0.9.3, Release Date: 2009-06-28 |
| Type notebook() for the GUI.                                       |
----------------------------------------------------------------------
In [1]: notebook()

and a browser will start with the web notebook. Visit "http://code.google.com/p/femhub/" and follow the instructions there to do your first calculation.

If you download the sources, please read below on how to build Femhub and work around common issues. 

----------------------------------------------------------------------

-----------------------------------------------------------------------------------

    Sage: Open Source Mathematical Software

       "Creating a Viable Open Source Alternative to 
          Magma, Maple, Mathematica, and Matlab"

    Copyright (C) 2006, 2007, 2008, 2009 William Stein
    Distributed under the terms of the GNU General Public License (GPL) 
                  http://www.sagemath.org

    If you have questions, do not hesitate to email the sage-support list
         http://groups.google.com/group/sage-support

    AUTHORS: There are over 125 people who have contributed code 
    to Sage.  Please see one of the websites above for a list.  In many 
    cases documentation for modules and functions list the authors.

-----------------------------------------------------------------------------------

QUICK INSTRUCTIONS TO BUILD FROM SOURCE (see below for more detailed instructions):
   1. Make sure you have the dependencies and 2GB free disk space.

     LINUX (install these using your package manager):
          gcc, g++, make, m4, perl, ranlib, and tar.

     OSX: XCode.  WARNING: If "gcc -v" outputs 4.0.0, you 
          *must* upgrade XCode (free from Apple), since that
          version of GCC is very broken. 
 
     Microsoft Windows: install cygwin using the setup.exe and in that chose to
         install the following packages:

         gcc4, gfortran, make, m4, perl, openssl-devel, cmake, libX11-devel,
         xextproto, libXext-devel, libXt-devel, libXt, libXext

     NOTE: On some operating systems it might be necessary to install
     gas/as, gld/ld, gnm/nm, but on most these are automatically
     installed when you install the programs listed above.  Only OS X
     >= 10.4.x and certain Linux distributions are 100% supported.
     See below for a complete list.
 
   2. Extract the tarball:
          tar xf femhub-0.9.4-*.tar

   3. cd into the sage directory and type make:
          cd femhub-0.9.4
          make
 
Depending on the speed of your computer, wait between 37 minutes to 1.5 hour. That's it. Everything is automatic and non-interactive.

If you want, you can also download a binary from http://sage.math.washington.edu/home/ondrej/scratch/femhub/, however, if it doesn't work for you, compile from source, that should always work (if not, please report a bug).

SE LINUX:  On Linux if you get this error message: 
  " restore segment prot after reloc: Permission denied "
the problem is probably related to SE Linux:
     http://www.ittvis.com/services/techtip.asp?ttid=3092

OFFICIALLY SUPPORTED PLATFORMS:
    Building of Sage from source is regularly tested on  
    (minimal installs of) the following platforms:

       PROCESSOR       OPERATING SYSTEM
       x86             32-bit Linux -- Debian, Ubuntu, CentOS (=Redhat), Fedora Core, OpenSuse, Mandriva
       x86_64          64-bit Linux -- Debian, Ubuntu, CentOS (=Redhat), Fedora Core, OpenSuse, Mandriva
       ia64 itanium2   64-bit Linux -- Redhat, Suse
       x86             Apple Mac OS X 10.5.x
       ppc             Apple Mac OS X 10.5.x

    Use Sage on Microsoft Windows via VMware.
    We do not always test on OS X 10.4, but Sage should work there fine.

NOTE: If you're using Fortran on a platform without g95 binaries included
      with Sage, e.g., Itanium, you must use a system-wide gfortran.  You 
      have to explicitly tell the build process about the fortran
      compiler and library location.  Do this by typing

          export SAGE_FORTRAN=/exact/path/to/gfortran
          export SAGE_FORTRAN_LIB=/path/to/fortran/libs/libgfortran.so

NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS:
       PROCESSOR       OPERATING SYSTEM
       sparc           Solaris 10 -- works fine (needs custom built gcc toolchain)
       x86_64          Solaris 10 -- must use clisp instead of ecl
       x86_64          Apple Mac OS X 10.5.x (64-bit) -- needs 64-bit gfortran instead of g95

NOT SUPPORTED:
     * FreeBSD
     * Arch Linux
     * Gentoo Linux
     * Microsoft Windows (via Visual Studio C++)
     * Microsoft Windows (via Cygwin)
      
     We like all of the above operating systems, but just haven't had
     the time to make Sage work well on them.  Help wanted!

IMPLEMENTATION: 
     Sage has significant components written in the following
     languages: C/C++, Python, Lisp, and Fortran.  Lisp and 
     Python are built as part of Sage, and Fortran (g95) is
     included (x86 Linux and OS X only), so you do not need 
     them in order to build Sage.

MORE DETAILED INSTRUCTIONS TO BUILD FROM SOURCE:
    1. Make sure you have about 2GB of free disk space.
    2. Linux: Install gcc, g++, m4, ranlib, and make.  
              The build should work fine on SUSE, FC, Ubuntu, etc.  If
              it doesn't, we want to know!
       OS X:  Make sure you have XCode version >= 2.4, i.e., gcc -v
              should output build >= 5363.   If you don't, go to
              http://developer.apple.com/ sign up, and download the 
              free XCode package.  Only OS X >= 10.4 is supported. 
       Windows: Download and install VMware, install linux into it, etc. 
    3. Extract the sage source tarball and cd into a directory
       with no spaces in it.  If you have a machine with 
       4 processors, say, type  
             export MAKE="make -j4"
       To start the build type
             make

       If you want to run the test suite for each 
       individual spkg as it is installed, type
             export SAGE_CHECK="yes"
       before starting the Sage build.  This will 
       run each test suite, and will raise an error 
       if any failures occur. 
    4. Wait about 1 hour to 14 days, depending on your computer (it
       took about 2 weeks to build Sage on the Google G1 Android cell
       phone).
    5. Type ./sage to try it out. 
    6. OPTIONAL: Start sage and run the command 
          install_scripts("/usr/local/bin/")   # change /usr/local/bin/
       Type "install_scripts?" in Sage for more details about
       what this command does.
    7. OPTIONAL: Type "make test" to test all examples in the 
       documentation (over 93,000 lines of input!) -- this takes from 
       30 minutes to several hours.   Don't get too disturbed if there are 
       2-3 failures, but always feel free to e-mail the section of
       test.log that contains errors to this mailing list:
              http://groups.google.com/group/sage-support
       If there are numerous failures, there was a serious problem
       with your build.
    8. OPTIONAL: Documentation: If you want to (try to) build the
       documentation, run "sage -docbuild help" for instructions.
       This requires having latex installed (if you want to build PDFs
       or HTML with PNG images for the math).  Note that the latex
       docs come *pre-built* with Sage, and are in
       SAGE_ROOT/devel/sage/doc/output/html.
    9. OPTIONAL: GAP -- It is highly recommended that you install the 
       optional GAP databases by typing
                            ./sage -optional
       then installing (with ./sage -i) the package whose name
       begins with database_gap.   This will download the package 
       from sage.math.washington.edu and install it.    While you're
       at it you might install other databases of interest to you. 
   10. OPTIONAL: It is recommended that you have both LaTeX
       and the ImageMagick tools (e.g., the "convert" command) installed
       since some plotting functionality benefits from it.

SUPPORTED COMPILERS:
    * Sage builds with GCC >= 3.x and GCC >= 4.1.x.
    * Sage will not build with GCC 2.9.x.
    * WARNING: Don't build with GCC 4.0.0, which is very buggy.
    * Sage has never been built without using GCC compiler. 

RUNNING SAGE:
    1. Try running sage:
          ./sage

    2. Try running an example Sage script:
          ./sage example.sage

RELOCATION:
   You *should* be able to move the sage-x.y.z directory anywhere you
   want.  If you copy the sage script or put a symlink to it, you
   should modify the script to reflect this (as instructed in the top
   of the script).  It is best if the path to Sage does not have any
   spaces in it.

   If you find anything that doesn't work correctly after you moved
   the directory, please email http://groups.google.com/group/sage-support

REDISTRIBUTION:
 Your local Sage install is almost exactly the same as any "developer"
 install.  You can make changes to documentation, source, etc., and
 very easily package up the complete results for redistribution just
 like we do.

   1.You can make your own source tarball (sage-x.y.z.tar) of Sage by
     typing "sage -sdist x.y.z", where the version is whatever you
     want.  The result is placed in SAGE_ROOT/dist.

  2. You can make a binary distribution with the packages you've
     installed included by typing "sage -bdist x.y.z".  The 
     result is placed in the SAGE_ROOT/dist directory.

  3. (Coming soon -- not yet supported)
     To make a binary that will run on the widest range of target
     machines, set the SAGE_FAT_BINARY environment variable to "yes"
     before building Sage:
           $ export SAGE_FAT_BINARY="yes"
           $ make
           $ ./sage -bdist x.y.z-fat


CHANGES TO INCLUDED SOFTWARE: 
    All software included with Sage is copyright by the respective
    authors and released under an open source license that is GPL
    compatible.  See the file COPYING.txt for more details.
    (Note -- jsMath is licensed under the Apache license; Apache 
    claim their license is GPL compatible, but Stallman disagrees.)

    Each spkg in SAGE_ROOT/spkg/standard/ is a bzip'd tarball.  You can 
    extract it with 

           tar jxvf name-*.spkg

    Inside the spkg, there is a file SPKG.txt that details all changes
    made to the given package for inclusion with Sage.  The inclusion
    of such a file detailing changes is specifically required by some
    of the packages included with Sage (e.g., for GAP).

