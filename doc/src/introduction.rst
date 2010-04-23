============
Introduction
============

`FEMhub <http://femhub.org>` is an open source distribution of finite element codes with a unified
Python interface. It is available for download as desktop application, but all codes
are also automatically available in the `Online Numerical Methods Laboratory <http://nb.femhub.org>`
which is powered by high performance computers of the `hp-FEM group <http://hpfem.org>` at the
`University of Nevada, Reno <http://unr.edu>`. Using FEMhub you can compute with Hermes and other packages via any web
browser.

FEMhub is available under the GPL license (Version 2, 1991).

Prior to reading FEMhub documentation, we recommend that you install FEMhub using instructions
below, and subscribe to the `mailing list <http://groups.google.com/group/femhub/>`_. 
Our mailing list is an active place where you should get all answers quickly.

The best way of reading this tutorial is to run the code at the same time.
After making your way through the tutorial, you may want to view the public
worksheets on the `online lab <http://nb.femhub.org/pub>`
that contains a variety of examples that may help you to get started. If you
create an interesting model using FEMhub packages, let us know and we
will be happy to add it to the existing examples.

The source code can be viewed in the `git repository <http://hpfem.org/git/gitweb.cgi/femhub.git/tree>`.


Officially Supported Platforms:
-------------------------------

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

Not Supported:
     * FreeBSD
     * Arch Linux
     * Gentoo Linux
     * Microsoft Windows (via Visual Studio C++)
     * Microsoft Windows (via Cygwin)

 We like all of the above operating systems, but just haven't had
 the time to make FEMhub work well on them.  Help wanted!

Implementation
--------------

FEMhub has significant components written in the following
languages: C/C++, Python, Lisp, and Fortran.  Lisp and 
Python are built as part of FEMhub, and Fortran (g95) is
included (x86 Linux and OS X only), so you do not need 
them in order to build FEMhub.

Supported Compilers
-------------------

    * FEMhub builds with GCC >= 3.x and GCC >= 4.1.x.
    * FEMhub will not build with GCC 2.9.x.
    * WARNING: Don't build with GCC 4.0.0, which is very buggy.
    * FEMhub has never been built without using GCC compiler. 

Redistribution
--------------

Your local FEMhub install is almost exactly the same as any "developer"
install.  You can make changes to documentation, source, etc., and
very easily package up the complete results for redistribution just
like we do. You can make your own source tarball (femhub-x.y.z.tar) 
of FEMhub or you can make a binary distribution with the packages you've
 installed included.

Changes to Included Softwares
-----------------------------

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

Credit
------

FEMhub was developed by the hp-FEM group at the Department of Mathematics,
University of Nevada, Reno.
http://www.femhub.org
http://www.hpfem.org

FEMhub Online Lab is based on the Sage Notebook.
FEMhub build system and some packages are taken from Sage.
Sage: Copyright (C) 2006, 2007, 2008, 2009, 2010 William Stein
Distributed under the terms of the GNU General Public License (GPL)
http://www.sagemath.org

AUTHORS: There are over 125 people who have contributed code to Sage and FEMhub.
In many cases documentation for modules and functions list the authors.
