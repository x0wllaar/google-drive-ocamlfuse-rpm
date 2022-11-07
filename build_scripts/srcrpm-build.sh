#!/usr/bin/env bash
set -exou pipefail

pushd ./src_rpms
dnf builddep -y gapi-ocaml-*.src.rpm
rpmbuild --rebuild gapi-ocaml-*.src.rpm
dnf install -y /root/rpmbuild/RPMS/$(arch)/*.rpm

dnf builddep -y ocamlfuse-*.src.rpm
rpmbuild --rebuild ocamlfuse-*.src.rpm
dnf install -y /root/rpmbuild/RPMS/$(arch)/*.rpm

dnf builddep -y google-drive-ocamlfuse-*.src.rpm
rpmbuild --rebuild google-drive-ocamlfuse-*.src.rpm
dnf install -y /root/rpmbuild/RPMS/$(arch)/*.rpm
popd