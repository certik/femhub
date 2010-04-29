=================
Manage VirtualBox
=================
To ensure higher security of your server you may want to host FEMhub in VirtualBox. Following are a few important tips on VirtualBox.


Install VirtualBox
~~~~~~~~~~~~~~~~~~
To install VirtualBox
::
  \$ wajig install virtualbox-ose

Answer yes to install the kernel module, it should just work. Create the virtual image: 
::
  \$ VBoxManage createvm -name ubuntu -register
  \$ VBoxManage modifyvm ubuntu -memory "2048MB" -acpi on -boot1 dvd -nic1 nat
  \$ VBoxManage createvdi -filename ~/.VirtualBox/Machines/ubuntu/ubuntu.vdi -size 20000 -register
  \$ VBoxManage modifyvm ubuntu -hdb ~/.VirtualBox/Machines/ubuntu/ubuntu.vdi
  \$ VBoxManage registerimage dvd ~/ext/debian-40r6-i386-netinst.iso
  \$ VBoxManage modifyvm ubuntu -dvd ~/ext/debian-40r6-i386-netinst.iso

Start the Image
~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To stop the image without saving changes, do
::

  \$ VBoxManage controlvm ubuntu poweroff

Stop the Image (Save Changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~
To stop the image saving changes,
::

\$ VBoxManage controlvm ubuntu savestate

Networking
~~~~~~~
In order to be able to login using ssh, do:
::
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/Protocol" TCP
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/GuestPort" 22
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guestssh/HostPort" 2222

Then you can login on the server using:
::
  \$ ssh -p 2222 localhost

Or if you put this into your .ssh/config:
::
  Host pythonnb
    HostName localhost
    User ondrej
    Compression no
    Port 2222

Then you can connect just by ssh pythonnb.

To forward the port 8000, do: 
::
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guest8000/Protocol" TCP
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guest8000/GuestPort" 8000
  \$ VBoxManage setextradata ubuntu "VBoxInternal/Devices/pcnet/0/LUN#0/Config/guest8000/HostPort" 8000

