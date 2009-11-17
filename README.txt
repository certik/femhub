Hello,

This README.txt describes build instruction for Femhub. If you downloaded
a binary, you do not need to do anything, just execute

 ./femhub

from the command line and you are good to go.

$ ./femhub
----------------------------------------------------------------------
| Femhub (FEM Distribution), Version 0.9.8, Release Date: 2009-11-18 |
| Type notebook() for the GUI.                                       |
----------------------------------------------------------------------
In [1]: notebook()

and a browser will start with the web notebook. Visit "http://code.google.com/p/femhub/" and follow the instructions there to do your first calculation.

If you download the sources, please read below on how to build Femhub and work around common issues. 

If you have questions, do not hesitate to email the FEMhub mailing list http://groups.google.com/group/femhub

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
          tar xf femhub-0.9.8-*.tar

   3. cd into the sage directory and type make:
          cd femhub-0.9.8
          make
     You can take advantage of several cores on your computer by executing
          $ export MAKE="make -j9"
     before typing make to compile in parallel on 9 cores.
 
Depending on the speed of your computer, wait between 37 minutes to 1.5 hour. That's it. Everything is automatic and non-interactive.

If you encounter problems, let us know through the FEMhub mailing list: http://groups.google.com/group/femhub

If you want, you can also download a binary from http://sage.math.washington.edu/home/ondrej/scratch/femhub/, however, if it doesn't work for you, compile from source, that should always work (if not, please report a bug).

SE LINUX:  On Linux if you get this error message: 
  " restore segment prot after reloc: Permission denied "
the problem is probably related to SE Linux:
     http://www.ittvis.com/services/techtip.asp?ttid=3092

OFFICIALLY SUPPORTED PLATFORMS:
    Building of FEMhub from source is regularly tested on  
    (minimal installs of) the following platforms:

       PROCESSOR       OPERATING SYSTEM
       x86             32-bit Linux -- Debian, Ubuntu, CentOS (=Redhat), Fedora Core, OpenSuse, Mandriva
       x86_64          64-bit Linux -- Debian, Ubuntu, CentOS (=Redhat), Fedora Core, OpenSuse, Mandriva
       ia64 itanium2   64-bit Linux -- Redhat, Suse
       x86             Apple Mac OS X 10.5.x
       ppc             Apple Mac OS X 10.5.x

    Use FEMhub on Microsoft Windows via VMware.
    We do not always test on OS X 10.4, but FEMhub should work there fine.

NOTE: If you're using Fortran on a platform without g95 binaries included
      with FEMhub, e.g., Itanium, you must use a system-wide gfortran.  You 
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
     the time to make FEMhub work well on them.  Help wanted!

IMPLEMENTATION: 
     FEMhub has significant components written in the following
     languages: C/C++, Python, Lisp, and Fortran.  Lisp and 
     Python are built as part of FEMhub, and Fortran (g95) is
     included (x86 Linux and OS X only), so you do not need 
     them in order to build FEMhub.

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
    3. Extract the FEMhub source tarball and cd into a directory
       with no spaces in it.  If you have a machine with 
       4 processors, say, type  
             export MAKE="make -j4"
       To start the build type
             make

    4. Wait about 1 hour to a few hours, depending on your computer.
    5. Type ./femhub to try it out. 

SUPPORTED COMPILERS:
    * FEMhub builds with GCC >= 3.x and GCC >= 4.1.x.
    * FEMhub will not build with GCC 2.9.x.
    * WARNING: Don't build with GCC 4.0.0, which is very buggy.
    * FEMhub has never been built without using GCC compiler. 

RUNNING FEMHUB:
    1. Try running FEMhub:
          ./femhub`

REDISTRIBUTION:
 Your local FEMhub install is almost exactly the same as any "developer"
 install.  You can make changes to documentation, source, etc., and
 very easily package up the complete results for redistribution just
 like we do. You can make your own source tarball (femhub-x.y.z.tar) 
 of FEMhub or you can make a binary distribution with the packages you've
     installed included.


CHANGES TO INCLUDED SOFTWARE: 
    All software included with FEmhub is copyright by the respective
    authors and released under an open source license that is GPL
    compatible.  See the file COPYING.txt for more details.
    (Note -- jsMath is licensed under the Apache license; Apache 
    claim their license is GPL compatible, but Stallman disagrees.)

    Each spkg in FEMHUB__ROOT/spkg/standard/ is a bzip'd tarball.  You can 
    extract it with 

           tar jxvf name-*.spkg

    Inside the spkg, there is a file SPKG.txt that details all changes
    made to the given package for inclusion with FEMhub.  The inclusion
    of such a file detailing changes is specifically required by some
    of the packages included with FEMhub (e.g., for GAP).

