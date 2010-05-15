============
Introduction
============

`FEMhub <http://femhub.org>`_ is an open source distribution of finite element codes with a unified
Python interface. It is available for download as desktop application, but all codes
are also automatically available in the `Online Numerical Methods Laboratory <http://lab.femhub.org>`_
which is powered by high performance computers of the `hp-FEM group <http://hpfem.org>`_ at the
`University of Nevada, Reno <http://unr.edu>`_. Every FEM code included in FEMhub can be used remotely via any web browser.

FEMhub is available under the GPL license (Version 2, 1991).

Prior to reading FEMhub documentation, we recommend that you install FEMhub using instructions
below, and subscribe to the `mailing list <http://groups.google.com/group/femhub/>`_. 
Our mailing list is an active place where you should get all answers quickly.

The best way of reading this tutorial is to run the code at the same time.
After making your way through the tutorial, you may want to view the `public
worksheets <http://lab.femhub.org/pub>`_
that contains a variety of examples that may help you to get started. If you
create an interesting model using FEMhub packages, let us know and we
will be happy to add it to the existing examples.

The source code can be viewed in the `git repository <http://hpfem.org/git/gitweb.cgi/femhub.git/tree>`_.


Officially Supported Platforms
------------------------------

Building of FEMhub from source is regularly tested on different Linux distributions and  Mac OS X. Please `click here <http://femhub.org/doc/src/install_run.html>`_ for the instructions on installing FEMhub.

**FEMhub in Windows:** You can install FEMhub on Windows using Cygwin. Please `click here <http://femhub.org/doc/src/install_run.html#microsoft-windows>`_ to view the instructions for installing FEMhub in Windows.

FEMhub may not build in all operationg systems. We like all of the operating systems, but just haven't had
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
of FEMhub or you can make a binary distribution with the packages you've installed included. User's action must comply with terms of the license under which FEMhub is distributed.

Changes to Included Softwares
-----------------------------

All software included with FEmhub is copyright by the respective
authors and released under an open source license that is GPL
compatible.  See the file COPYING.txt for more details.
(Note -- jsMath is licensed under the Apache license; Apache 
claim their license is GPL compatible, but Stallman disagrees.)

Each spkg in FEMHUB__ROOT/spkg/standard/ is a bzip'd tarball.  You can 
extract it with:: 

       tar jxvf name-*.spkg

Credit
------

FEMhub was developed by the `hp-FEM group <http://hpfem.org>`_ at the Department of Mathematics ans Statistics, University of Nevada, Reno.

FEMhub Online Lab is based on the Sage Notebook.
FEMhub build system and some packages are taken from `Sage <http://www.sagemath.org>`_.
Distributed under the terms of the GNU General Public License (GPL)
