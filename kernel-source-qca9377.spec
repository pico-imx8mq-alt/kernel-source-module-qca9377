Name: kernel-source-qca9377
Version: 4.5.24.4
Release: alt3

Summary: Qualcomm QCA9377 Wireless Driver
License: GPL
Group: Development/Kernel
URL: https://github.com/TechNexion/qcacld-2.0
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
Qualcomm QCA9377 Wireless Driver

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%changelog
* Tue Oct 27 2020 Pavel Nakonechnyi <zorg@altlinux.org> 4.5.24.4-alt3
- updated to the current version of upstream tn-CNSS.LEA.NRT_3.0 branch

* Thu Dec 26 2019 Pavel Nakonechnyi <zorg@altlinux.org> 4.5.24.4-alt2
- updated to the current version of upstream tn-CNSS.LEA.NRT_3.0 branch

* Sun Jul 07 2019 Pavel Nakonechnyi <zorg@altlinux.org> 4.5.24.4-alt1
- initial build
