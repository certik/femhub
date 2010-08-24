=================
Manage VirtualBox
=================
To ensure higher security of your server you may want to host FEMhub in VirtualBox. Following are a few important tips on VirtualBox.


Install VirtualBox
------------------

To install VirtualBox::

  \$ wajig install virtualbox-ose

Answer yes to install the kernel module, it should just work. Create the
virtual image::

  \$ VBoxManage createvm -name ubuntu -register
  \$ VBoxManage modifyvm ubuntu -memory "2048MB" -acpi on -boot1 dvd -nic1 nat
  \$ VBoxManage createvdi -filename ~/.VirtualBox/Machines/ubuntu/ubuntu.vdi -size 20000 -register
  \$ VBoxManage modifyvm ubuntu -hdb ~/.VirtualBox/Machines/ubuntu/ubuntu.vdi
  \$ VBoxManage registerimage dvd ~/ext/debian-40r6-i386-netinst.iso
  \$ VBoxManage modifyvm ubuntu -dvd ~/ext/debian-40r6-i386-netinst.iso

Start the Image
---------------

To start the virtual image do:
::

  \$ VBoxHeadless -startvm ubuntu
  VirtualBox Headless Interface 2.1.2
  (C) 2008-2009 Sun Microsystems, Inc.
  All rights reserved.

  Listening on port 3389

Connect to the image (requires X) on the same machine:
::
 
  \$ rdesktop localhost

Or you can login remotely by forwarding the 3389 port: 
::

  \$ ssh -L 3389:localhost:3389 server

And from your desktop computer
::

  \$ rdesktop localhost

Install the system. After installing it, remove the cd (iso image) by
::

  \$ VBoxManage modifyvm ubuntu -dvd none


Stop the Image (Do not Save Changes)
------------------------------------

To stop the image without saving changes, do
::

  \$ VBoxManage controlvm ubuntu poweroff

Stop the Image (Save Changes)
-----------------------------
To stop the image saving changes,
::

\$ VBoxManage controlvm ubuntu savestate

Networking
----------

In order to be able to login using ssh, do::

    \$ VBoxManage modifyvm "ubuntu" --natpf1 "guestssh,tcp,,2222,,22"

Then you can login on the server using::

  \$ ssh -p 2222 localhost

Or if you put this into your .ssh/config::

  Host pythonnb
    HostName localhost
    User ondrej
    Compression no
    Port 2222

Then you can connect just by ssh pythonnb.

To forward the port 8000, do::

    \$ VBoxManage modifyvm "ubuntu" --natpf1 "guesthttp,tcp,,8000,,8000"

One can then delete any of the rules above by::

    \$ VBoxManage modifyvm "ubuntu" --natpf1 delete "guestssh"

(or guesthttp). One can use any names instead of guesthttp/guestssh.


Import the Appliance
--------------------

First use dry run::

    VBoxManage import ext/virtualbox_image/new_lab.ovf --dry-run

Check that the name and other things are ok, or change them using the suggested
cmd line options that it offers. In our case::

    VBoxManage import ext/virtualbox_image/new_lab.ovf --dry-run --vsys 0 --vmname new_lab_backend

Once satisfied, do it for real::

    \$ VBoxManage import ext/virtualbox_image/new_lab.ovf --vsys 0 --vmname new_lab_backend
    [...]
    0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
    Successfully imported the appliance.

And you are done, the new virtual machine will show up::

    \$ VBoxManage list vms
    Oracle VM VirtualBox Command Line Management Interface Version 3.2.8
    (C) 2005-2010 Oracle Corporation
    All rights reserved.

    "ubuntu" {7b6c0b84-9070-4e64-9bc1-af659c1f5efb}
    "new_lab" {42d7216a-1b7c-4376-a46c-719f9363c212}
    "new_lab_backend" {edf1e2ee-1c8a-4f5d-957f-3adda9e25e6b}
