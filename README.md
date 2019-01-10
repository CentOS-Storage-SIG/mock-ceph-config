# ceph-mock-config

This package contains the mock configuration files for Ceph in CentOS Storage
SIG.

See https://wiki.centos.org/SpecialInterestGroup/Storage/Ceph/Mock for more
documentation.

## How do I package the files in this Git repo (mock-ceph-config)?

Make a local SRPM file:

```sh
make srpm DISTRO=el7
```

Build the SRPM file in CBS and tag into `-testing`:

```sh
make build DISTRO=el7
```
