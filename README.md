# ceph-mock-config

This package contains the mock configuration files for Ceph in CentOS Storage
SIG.

## How do I use this?


Install the `mock` package and add your user account to the `mock` group:

```sh
yum install mock
usermod -a -G mock kdreyer
```

Log out and log back in to ensure that you're in the `mock` group (or use the
`newgrp` command to ensure you have the mock group set on your current login
session).

You must also install this `ceph-mock` package. You can get it from the Storage
SIG repository (`centos-release-ceph` package):

```sh
yum install centos-release-ceph-nautilus
yum install mock-ceph-config
```

To rebuild a SRPM for nautilus, specify the mock configuration with "-r":

```
mock -r storage7-ceph-nautilus-el7-x86_64 path/to/ceph-ansible-3.2.0-1.el7.src.rpm
```

## What is mock?

[Mock](https://github.com/rpm-software-management/mock/wiki) is a tool for
building packages. It builds RPMs in a minimal chroot. It is similar to
Debian's pbuilder.

## Why use mock?

When you use mock to build RPMs locally, you can have a high degree of
confidence that your build artifacts will match the build in the official build
system, [CentOS' CBS](https://cbs.centos.org/koji/) (Koji).

## How do I package the files in this Git repo (mock-ceph-config)?

```sh
make srpm DISTRO=el7
```
