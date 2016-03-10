# google-drive-ocamlfuse
packaging google-drive-ocamlfuse

1 - ocamlfuse
<pre>
   cd ocamlfuse
   spectool -g ocamlfuse.spec
   rpmbuild -bs ocamlfuse.spec --define '_sourcedir .' --    define '_srcrpmdir .'
   mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm
</pre>


2 - gapi-ocaml
<pre>
    cd gapi-ocaml
    spectool -g gapi-ocaml.spec
    rpmbuild -bs gapi-ocaml.spec --define '_sourcedir .' --define '_srcrpmdir .'
    mock -r fedora-24-x86_64 --no-clean --rebuild ./gapi-ocaml-0.2.8-1.fc23.src.rpm
    md5sum gapi-ocaml-0.2.8.tar.gz > sources 
    cat sources| cut -c 35- >> .gitignore
</pre>

3 - google-drive-ocamlfuse
<pre>
    cd google-drive-ocamlfuse/
    rpmbuild -bs google-drive-ocamlfuse.spec --define '_sourcedir .' --define '_srcrpmdir .'
    cd ..
</pre>

4 - Build all in chain
<pre>
    mockchain -r fedora-23-x86_64 \
    ocamlfuse/ocamlfuse-2.7.1-1.cv2.fc23.src.rpm \
    gapi-ocaml/gapi-ocaml-0.2.8-1.fc23.src.rpm \
    google-drive-ocamlfuse/google-drive-ocamlfuse-0.5.22-1.fc23.src.rpm
</pre>

