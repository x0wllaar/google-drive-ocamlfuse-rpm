#
# spec file for package tiny-httpd-ocaml
#
# Copyright (c) 2022 Grigorii Khvatskii
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
#for Fedora 33
%global debug_package %{nil}

Name:           tiny-httpd-ocaml
Version:        0.12
Release:        1%{?dist}
Summary:        Minimal HTTP server using good old threads (OCAML)
License:        MIT

Url:            https://github.com/c-cube/tiny_httpd/
Source0:        https://github.com/c-cube/tiny_httpd/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 3.12
BuildRequires:  ocaml-dune-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-seq-devel

%description
*tiny_httpd* is a minimal HTTP server using good old threads, 
with stream abstractions, simple routing, URL encoding/decoding, 
static asset serving, and optional compression with camlzip. 
It also supports server-sent events (w3c)

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n tiny_httpd-%{version}

%build
dune build @install

%install
dune install --prefix=%{buildroot}/usr --libdir=%{buildroot}%{_libdir}/ocaml
find %{buildroot} -type f | xargs sed -i "s|%{buildroot}||g" #Fix buildroot leaking
#See https://adam.younglogic.com/2010/05/found-buildroot-in-installed-files-aborting/

#only remove README.md and LICENSE
rm -r %{buildroot}/usr/doc/tiny_httpd
rm -r %{buildroot}/usr/doc/tiny_httpd_camlzip


%files
%doc README.md
%{_libdir}/ocaml/tiny_httpd
%{_libdir}/ocaml/tiny_httpd_camlzip
/usr/bin/http_of_dir
/usr/bin/tiny-httpd-vfs-pack
%if %{opt}
%exclude %{_libdir}/ocaml/tiny_httpd/*.a
%exclude %{_libdir}/ocaml/tiny_httpd/*.cmx
%exclude %{_libdir}/ocaml/tiny_httpd/*.cmxa
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.a
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.cmx
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.cmxa
%endif
%exclude %{_libdir}/ocaml/tiny_httpd/*.mli
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.mli

%files devel
%if %{opt}
%{_libdir}/ocaml/tiny_httpd/*.a
%{_libdir}/ocaml/tiny_httpd/*.cmx
%{_libdir}/ocaml/tiny_httpd/*.cmxa
%{_libdir}/ocaml/tiny_httpd_camlzip/*.a
%{_libdir}/ocaml/tiny_httpd_camlzip/*.cmx
%{_libdir}/ocaml/tiny_httpd_camlzip/*.cmxa
%endif
%{_libdir}/ocaml/tiny_httpd/*.mli
%{_libdir}/ocaml/tiny_httpd_camlzip/*.mli

%changelog
* Mon Nov 07 2022 Grigorii Khvatskii <gkhvatsk@nd.edu> - 0.12
- Initial build