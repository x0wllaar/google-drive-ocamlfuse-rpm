fuse_ver=2.7.1-cvs7
fuse_tag=cvs7
fuse_srcrpm=ocamlfuse-2.7.1-8.cvs7.fc33.src.rpm
gapi_ver=0.3.19
googledrive_ver=0.7.26
fver=33

if [ -z "$1" ]
then
      stage=0
else
      stage=$1
fi

if test $stage -le 0
then
echo STAGE 0
cd ocamlfuse
name=ocamlfuse
sed -i "s|^%global tagversion .*|%global tagversion $fuse_tag|" $name.spec
rpmdev-bumpspec -c "Update $name to $fuse_ver" $name.spec
spectool -g ocamlfuse.spec
rpmbuild -bs ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
# optional
#mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm
#or
copr-cli build sergiomb/google-drive-ocamlfuse ./$fuse_srcrpm
cd ..
echo Press enter to continue to gapi-ocaml; read dummy;
fi
if test $stage -le 1
then
echo STAGE 1
cd gapi-ocaml
rpmdev-bumpspec -n $gapi_ver -c "Update gapi-ocaml to $gapi_ver" gapi-ocaml.spec
spectool -g gapi-ocaml.spec
rpmbuild -bs gapi-ocaml.spec --define "_sourcedir ." --define "_srcrpmdir ."
# optional
#mock -r fedora-23-x86_64 --no-clean --rebuild ./gapi-ocaml-0.2.10-1.fc23.src.rpm
copr-cli build sergiomb/google-drive-ocamlfuse ./gapi-ocaml-$gapi_ver-1.fc$fver.src.rpm
cd ..
echo Press enter to continue to google-drive-ocamlfuse; read dummy;
fi
if test $stage -le 2
then
echo STAGE 2
cd google-drive-ocamlfuse/
rpmdev-bumpspec -n $googledrive_ver -c "Update google-drive-ocamlfuse to $googledrive_ver" google-drive-ocamlfuse.spec
spectool -g google-drive-ocamlfuse.spec
rpmbuild -bs google-drive-ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
copr-cli build sergiomb/google-drive-ocamlfuse ./google-drive-ocamlfuse-$googledrive_ver-1.fc$fver.src.rpm
cd ..
fi

#mockchain -r fedora-23-x86_64 -l resultsdir \
#ocamlfuse/ocamlfuse-2.7.1-1.cv2.fc23.src.rpm \
#gapi-ocaml/gapi-ocaml-0.2.10-1.fc23.src.rpm \
#google-drive-ocamlfuse/google-drive-ocamlfuse-0.5.22-2.fc23.src.rpm
#and the rpm is in resultsdir/results/fedora-23-x86_64/google-drive-ocamlfuse-0.5.22-2.fc23/
