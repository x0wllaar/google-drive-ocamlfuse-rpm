#
# spec file for package google-drive-ocamlfuse
#
# Copyright (c) 2016 Sérgio Basto.
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:       google-drive-ocamlfuse
Version:    0.6.17
Release:    1%{?dist}
License:    BSD-2-Clause
Summary:    FUSE filesystem for Google Drive
Url:        http://gdfuse.forge.ocamlcore.org
Group:      System/Filesystems
Source:     https://github.com/astrada/google-drive-ocamlfuse/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 3.12.0
BuildRequires:  ocaml-findlib-devel >= 1.2.7
BuildRequires:  ocamlfuse >= 2.7.1
BuildRequires:  gapi-ocaml-devel >= 0.2.10
BuildRequires:  ocaml-sqlite-devel >= 1.6.1
BuildRequires:  ocaml-cryptokit-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-curl-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ocamlnet-nethttpd-devel
BuildRequires:  sqlite-devel
BuildRequires:  curl-devel
BuildRequires:  zlib-devel
BuildRequires:  fuse-devel
BuildRequires:  ocaml-zarith-devel
%if 0%{?fedora} >= 26
BuildRequires:  ocaml-ocamlbuild
%endif

%description
google-drive-ocamlfuse is a FUSE-based file system backed by Google Drive,
written in OCaml. It lets you mount your Google Drive on Linux.

On the first time, just run google-drive-ocamlfuse, which will open a
browser for authentication. If that process succeeds, it will print
"Access token retrieved correctly.". Now run google-drive-ocamlfuse
with an empty directory supplied, which is the mount point for your Google
Drive. You can optionally unmount with fusermount -u mount-point.

Further documentation is available here:

  https://github.com/astrada/google-drive-ocamlfuse/wiki


%prep
%setup -q

%build
ocaml setup.ml -configure
ocaml setup.ml -build

%install
mkdir -p %{buildroot}%{_bindir}
cp gdfuse.native %{buildroot}%{_bindir}/%{name}

%files
%doc README.md doc/
%license LICENSE
%{_bindir}/%{name}


%changelog
* Tue Jul 11 2017 Sérgio Basto <sergio@serjux.com> - 0.6.17-1
- Update to 0.6.17

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 0.6.2-1
- Update to 0.6.2

* Fri Apr 22 2016 Sérgio Basto <sergio@serjux.com> - 0.5.22-2
- Rebuild for gapi-ocaml-0.2.10

* Thu Mar 10 2016 Sérgio Basto <sergio@serjux.com> - 0.5.22-1
- Update to 0.5.22

* Mon Sep 28 2015 hpj@urpla.net
- update to version 0.5.18 (no changelog available)
* Sun Mar 29 2015 hpj@urpla.net
- update to version 0.5.13 (no changelog available)
* Tue Jan  6 2015 hpj@urpla.net
- version 0.5.12: initial build
