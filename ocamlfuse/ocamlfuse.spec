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
Release:        1.cv2%{?dist}
Summary:        Ocaml FUSE binding
Group:          Development/Libraries/Other
License:        GPLv2
Url:            https://github.com/astrada/ocamlfuse/
Source:         https://github.com/astrada/ocamlfuse/archive/v2.7.1_cvs2/%{name}-%{version}_cvs2.tar.gz
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
%setup -q -n %{name}-%{version}_cvs2

%build
cd lib
#Disable warnings to avoid spurious message about 64 bit compatibility
#due to a missing cast in a macro
#using _smp_mflags here results in failed builds
make CFLAGS="-w -D_FILE_OFFSET_BITS=64 -fPIC" all

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/Fuse
mkdir -p %{buildroot}/%{_libdir}/ocaml/caml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
mkdir -p %{buildroot}/%{_bindir}

cd lib
make OCAMLLIB=%{buildroot}/%{_libdir}/ocaml\
     OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"\
     BINDIR=%{buildroot}/%{_bindir} \
     install

%files
%license LICENSE
%{_libdir}/ocaml/Fuse/
%{_libdir}/ocaml/stublibs/*

%changelog
* Thu Mar 10 2016 Sérgio Basto <sergio@serjux.com> - 2.7.1-1.cv2
- Migrate to Fedora/Redhat.

* Sat Nov  7 2015 hpj@urpla.net
- version 2.7.1-cvs2: initial build
