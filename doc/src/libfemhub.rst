=========
LibFEMhub
=========

LibFEMhub is the collection of "femhub" python modules including python wrappers to mesh editors and FE libraries.

Git Repository
--------------
You can browse libfemhub git repository here: http://git.hpfem.org/libfemhub.git
To develop the libfemhub package you can clone it:
::
  \$ git clone http://git.hpfem.org/git/libfemhub.git

After you create patches or make required changes you can apply these changes by following these steps:
::
  \$ cd libfemhub/
  \$ path_to_femhub/femhub -shell # this launches FEMhub shell
  \$ bash spkg-install
   CTRL+D # exits this shell after the previous command completes
