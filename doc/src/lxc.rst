=================
Manage LXC
=================

Prepare the Host Computer
-------------------------

First install necessary packages::

    sudo apt-get install debootstrap lxc bridge-utils


Create the Root Filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to some directory, which will contain the root filesystem and configuration,
for example ``/home/ondrej/debian``::

    cd /home/ondrej/debian
    sudo debootstrap --variant=minbase --arch amd64 lucid rootfs.ubuntu http://ubuntu.osuosl.org/ubuntu/

This takes about 1.5min on my computer (it downloads and installs the Ubuntu
base packages).

Setting Up the Guest System
---------------------------

Chroot into the root filesystem::

    sudo chroot rootfs.ubuntu

and run these in the chroot::

    apt-get install --force-yes -y gpgv
    apt-get update

    apt-get -y install language-pack-en
    locale-gen en_US.UTF-8
    /usr/sbin/update-locale LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8" LC_CTYPE="C"

    apt-get install -y adduser apt-utils iproute iptables nano netbase openssh-blacklist openssh-blacklist-extra openssh-server ping rsyslog sudo vim

    echo "pythonnb" > /etc/hostname
    echo "127.0.0.1 localhost pythonnb" > /etc/hosts
    echo "192.168.0.60 pythonnb" >> /etc/hosts

    ln -s /proc/mounts /etc/mtab

    cat >> /etc/environment <<EOF
    LANG="en_US.UTF-8"
    LANGUAGE="en_US.UTF-8"
    LC_ALL="en_US.UTF-8"
    LC_CTYPE="C"
    EOF

Exit the chroot::

    exit


Finish Host Computer Setup
--------------------------

Cgroups
~~~~~~~

Become root and execute the rest as root::

    sudo -i
    mkdir /cgroup
    echo "none /cgroup cgroup defaults 0 0" >> /etc/fstab
    mount /cgroup

Network
~~~~~~~

Setup the network by editing ``/etc/network/interfaces``::

    auto lo
    iface lo inet loopback

    auto br0
    iface br0 inet static
        address 134.197.8.230
        netmask 255.255.255.0
        gateway 134.197.8.254
        bridge_ports eth0
        bridge_stp off
        bridge_maxwait 5
        post-up /usr/sbin/brctl setfd br0 0

then::

    sudo ifdown -a
    sudo ifup -a

Create the Container
~~~~~~~~~~~~~~~~~~~~~~

In the host computer in ``/home/ondrej/debian``, create ``fstab.ubuntu``::

    none /home/ondrej/debian/rootfs.ubuntu/dev/pts devpts defaults 0 0
    none /home/ondrej/debian/rootfs.ubuntu/proc proc defaults 0 0
    none /home/ondrej/debian/rootfs.ubuntu/sys sysfs defaults 0 0
    none /home/ondrej/debian/rootfs.ubuntu/var/lock tmpfs defaults 0 0
    none /home/ondrej/debian/rootfs.ubuntu/var/run tmpfs defaults 0 0
    /etc/resolv.conf /home/ondrej/debian/rootfs.ubuntu/etc/resolv.conf none bind 0 0

and config.ubuntu::

    lxc.utsname = ubuntu
    lxc.tty = 4
    lxc.network.type = veth
    lxc.network.flags = up
    lxc.network.link = br0
    lxc.network.name = eth0
    lxc.network.mtu = 1500
    lxc.network.ipv4 = 134.197.8.39/24
    lxc.rootfs = /home/ondrej/debian/rootfs.ubuntu
    lxc.mount = /home/ondrej/debian/fstab.ubuntu
    lxc.cgroup.devices.deny = a
    # /dev/null and zero
    lxc.cgroup.devices.allow = c 1:3 rwm
    lxc.cgroup.devices.allow = c 1:5 rwm
    # consoles
    lxc.cgroup.devices.allow = c 5:1 rwm
    lxc.cgroup.devices.allow = c 5:0 rwm
    lxc.cgroup.devices.allow = c 4:0 rwm
    lxc.cgroup.devices.allow = c 4:1 rwm
    # /dev/{,u}random
    lxc.cgroup.devices.allow = c 1:9 rwm
    lxc.cgroup.devices.allow = c 1:8 rwm
    # /dev/pts/* - pts namespaces are "coming soon"
    lxc.cgroup.devices.allow = c 136:* rwm
    lxc.cgroup.devices.allow = c 5:2 rwm
    # rtc
    lxc.cgroup.devices.allow = c 254:0 rwm


Create the container::

    sudo lxc-create -n ubuntu config.ubuntu

Run it::

    sudo lxc-start -n ubuntu

Stop it::

    sudo lxc-stop -n ubuntu

Destroy it::

    sudo lxc-destroy -n ubuntu
