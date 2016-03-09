# google-drive-ocamlfuse
packaging google-drive-ocamlfuse

1 - ocamlfuse
cd ocamlfuse
spectool -g ocamlfuse.spec
rpmbuild -bs ocamlfuse.spec --define '_sourcedir .' --define '_srcrpmdir .'
mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm

2 - gapi-ocaml
cd gapi-ocaml
spectool -g gapi-ocaml.spec
rpmbuild -bs gapi-ocaml.spec --define "_sourcedir ." --define '_srcrpmdir .'
mock -r fedora-24-x86_64 --no-clean --rebuild ./gapi-ocaml-0.2.8-1.fc23.src.rpm
md5sum gapi-ocaml-0.2.8.tar.gz > sources 
cat sources | cut -c 35- >> .gitignore

