Summary: Ceph mock configs for CentOS Storage SIG
Name: mock-ceph-config
Version: 1.0
Release: 5%{?dist}
License: MIT
URL: https://wiki.centos.org/SpecialInterestGroup/Storage/Ceph
Source0: LICENSE
Source1: storage7-ceph-luminous-el7-x86_64.cfg
Source2: storage7-ceph-luminous-el7-aarch64.cfg
Source3: storage7-ceph-luminous-el7-ppc64le.cfg
Source4: storage7-ceph-nautilus-el7-x86_64.cfg
Source5: storage7-ceph-nautilus-el7-aarch64.cfg
Source6: storage7-ceph-nautilus-el7-ppc64le.cfg
Source7: storage8-ceph-nautilus-el8-x86_64.cfg
Source8: storage8-ceph-nautilus-el8-aarch64.cfg
Source9: storage8-ceph-nautilus-el8-ppc64le.cfg

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
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/mock/
install -p -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/mock/

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/mock/*

%changelog
* Mon Feb 10 2020 Giulio Fidente <gfidente@redhat.com> - 1.0-5
- fix wrong references to luminous targets on el8

* Mon Feb 10 2020 Giulio Fidente <gfidente@redhat.com> - 1.0-4
- add nautilus storage8 configurations

* Tue Jan 22 2019 Ken Dreyer <kdreyer@redhat.com> - 1.0-3
- add luminous configurations

* Fri Jan 11 2019 Ken Dreyer <kdreyer@redhat.com> - 1.0-2
- drop the "sclo" repository
- use HTTPS for buildlogs.centos.org
- use releasever and basearch variables
- add aarch64 and ppc64le configurations

* Tue Jan  8 2019 Ken Dreyer <kdreyer@redhat.com> - 1.0-1
- Initial version.
