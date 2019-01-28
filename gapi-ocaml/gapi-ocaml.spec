#
# spec file for package gapi-ocaml
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


%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%global debug_package %{nil}
Name:           gapi-ocaml
Version:        0.3.9
Release:        1%{?dist}
Summary:        A simple OCaml client for Google Services
License:        MIT
Group:          Development/Libraries/Other

Url:            https://github.com/astrada/gapi-ocaml
Source0:        https://github.com/astrada/gapi-ocaml/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 3.12
BuildRequires:  ocaml-biniou
BuildRequires:  ocaml-findlib-devel >= 1.2.7
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlnet-nethttpd-devel >= 3.3.5
BuildRequires:  ocaml-cryptokit-devel >= 1.3.14
BuildRequires:  ocaml-extlib-devel >= 1.5.1
BuildRequires:  ocaml-yojson >= 1.0.2
BuildRequires:  ocaml-xmlm-devel >= 1.0.2
BuildRequires:  ocaml-ounit-devel >= 1.1.0
BuildRequires:  ocaml-curl-devel
BuildRequires:  jbuilder
BuildRequires:  opam-installer
BuildRequires:  zlib-devel

# ocaml autodep start for pkg: gapi-ocaml
# hardcoded rpm dependency for pre 12.1 to compensate for lack of ocaml() provides/requires
%if 0%{?suse_version} < 1210
Requires:       ocaml-biniou ocaml-cryptokit ocaml-easy-format ocaml-extlib ocaml-runtime ocaml-xmlm ocaml-yojson
%endif
# ocaml autodep end for pkg: gapi-ocaml

%description
**gapi-ocaml** is a simple, unofficial, OCaml client for Google Services. The
library supports ClientLogin, OAuth 1.0a, and OAuth 2.0 authentication.
Supported RESTful APIs:

* Calendar APIs v3
* Google+ API v1
* Tasks API v1
* APIs Discovery Service v1
* URL Shortener API v1
* OAuth2 API v2
* Custom Search API v1
* Google Analytics API v3
* Page Speed Online API v1
* Blogger API v2
* Site Verification API v1
* AdSense Management API v1.1
* BigQuery API v2
* Drive API v2
* Gmail API v1

Google Data Protocol APIs (GData):

* Google Documents List API v3 (supports Google Drive)

### Features

* Monadic interface
* [Functional lenses](http://astrada.github.com/gapi-ocaml/GapiLens.html) to
  access data structures
* Service generator (experimental): a tool for generating client libraries for
  APIs based on the Google API Discovery format


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

%build
jbuilder build @install
#ocaml setup.ml -configure --enable-examples
#ocaml setup.ml -build

%install
#export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
#mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
#ocaml setup.ml -install
mkdir -p %{buildroot}%{_libdir}/ocaml
#mkdir -p %{buildroot}%{_docdir}
jbuilder install --prefix=%{buildroot} --libdir=%{buildroot}%{_libdir}/ocaml
#only remove README.md and LICENSE
rm -r %{buildroot}/doc/gapi-ocaml/


%files
%doc README.md
%license LICENSE
%{_libdir}/ocaml/gapi-ocaml
%if %{opt}
%exclude %{_libdir}/ocaml/gapi-ocaml/*.a
%exclude %{_libdir}/ocaml/gapi-ocaml/*.cmx
%exclude %{_libdir}/ocaml/gapi-ocaml/*.cmxa
%endif
%exclude %{_libdir}/ocaml/gapi-ocaml/*.mli

%files devel
%if %{opt}
%{_libdir}/ocaml/gapi-ocaml/*.a
%{_libdir}/ocaml/gapi-ocaml/*.cmx
%{_libdir}/ocaml/gapi-ocaml/*.cmxa
%endif
%{_libdir}/ocaml/gapi-ocaml/*.mli

%changelog
* Mon Jan 28 2019 Sérgio Basto <sergio@serjux.com> - 0.3.9-1
- Update gapi-ocaml to 0.3.9

* Wed Jan 24 2018 Sérgio Basto <sergio@serjux.com> - 0.3.6-1
- Update gapi-ocaml to 0.3.6

* Tue Jul 11 2017 Sérgio Basto <sergio@serjux.com> - 0.3.4-1
- Update to 0.3.4

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 0.3.1-1
- Update to 0.3.1

* Fri Apr 22 2016 Sérgio Basto <sergio@serjux.com> - 0.2.10-1
- Update to 0.2.10

* Wed Mar 09 2016 Sérgio Basto <sergio@serjux.com> - 0.2.8-1
- Update to 0.2.8
- Migrate to Fedora.

* Tue Nov 10 2015 ohering@suse.de
- Add hardcoded Provides for pre 12.1 repos
* Mon Nov  9 2015 hpj@urpla.net
- explicitly require misc. ocaml-ocamlnet modules
  in order to fix build for older distributions (<= 11.4)
* Mon Jan  5 2015 hpj@urpla.net
- version 0.2.6: initial build
