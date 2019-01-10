Summary: Ceph mock configs for CentOS Storage SIG
Name: mock-ceph-config
Version: 1.0
Release: 1%{?dist}
License: MIT
URL: https://wiki.centos.org/SpecialInterestGroup/Storage/Ceph
Source0: LICENSE
Source1: storage7-ceph-nautilus-el7-x86_64.cfg

BuildArch: noarch

# $contentdir for altarch support was added with CentOS-7.5
Requires: mock-core-configs
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

%description
Config files which allow you to create chroots for building Ceph via the
CentOS Storage SIG.

%prep
install -p -m 0644 %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/mock/*

%changelog
* Tue Jan  8 2019 Ken Dreyer <kdreyer@redhat.com> - 1.0-1
- Initial version.
