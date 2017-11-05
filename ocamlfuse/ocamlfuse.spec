#
# spec file for package ocamlfuse
#
# Copyright (c) 2016 Sérgio Basto.
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ocamlfuse
Version:        2.7.1
%global tagversion cvs5
%global realversion %{version}_%{tagversion}
Release:        4.%{tagversion}%{?dist}
Summary:        Ocaml FUSE binding
Group:          Development/Libraries/Other
License:        GPLv2
Url:            https://github.com/astrada/ocamlfuse/
Source:         https://github.com/astrada/ocamlfuse/archive/v%{realversion}/%{name}-%{realversion}.tar.gz
BuildRequires:  fuse-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl

%description
This is a binding to fuse for the ocaml programming language, enabling
you to write multithreaded filesystems in the ocaml language. It has
been designed with simplicity as a goal, as you can see by looking at
example/fusexmp.ml. Efficiency has also been a separate goal. The
Bigarray library is used for read and writes, allowing the library to
do zero-copy in ocaml land.

%prep
%setup -q -n %{name}-%{realversion}

%build
cd lib
#Disable warnings to avoid spurious message about 64 bit compatibility
#due to a missing cast in a macro
export CFLAGS="%{optflags} -w"
%make_build all

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/Fuse
mkdir -p %{buildroot}/%{_libdir}/ocaml/caml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
mkdir -p %{buildroot}/%{_bindir}
cd lib
%make_install OCAMLLIB=%{buildroot}/%{_libdir}/ocaml\
     OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"\
     BINDIR=%{buildroot}/%{_bindir}

%files
%license LICENSE
%{_libdir}/ocaml/Fuse/
%{_libdir}/ocaml/stublibs/*

%changelog
* Thu Nov 02 2017 Sérgio Basto <sergio@serjux.com> - 2.7.1-4.cvs5
- Fix CFLAGS to not generate debug packages empty.

* Tue Jul 11 2017 Sérgio Basto <sergio@serjux.com> - 2.7.1-3.cvs5
- Update to 2.7.1-cvs5

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 2.7.1-2.cvs4
- Update to 2.7.1-cvs4

* Thu Mar 10 2016 Sérgio Basto <sergio@serjux.com> - 2.7.1-1.cv2
- Migrate to Fedora/Redhat.

* Sat Nov  7 2015 hpj@urpla.net
- version 2.7.1-cvs2: initial build
