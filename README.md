# google-drive-ocamlfuse
Packaging google-drive-ocamlfuse

1 - Prepare ocamlfuse
```
   cd ocamlfuse
   spectool -g ocamlfuse.spec
   rpmbuild -bs ocamlfuse.spec --define "_sourcedir ." --    define "_srcrpmdir ."
   # optional
   mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm
   cd ..
```

2 - Prepare gapi-ocaml
```
    cd gapi-ocaml
    spectool -g gapi-ocaml.spec
    rpmbuild -bs gapi-ocaml.spec --define "_sourcedir ." --define "_srcrpmdir ."
    # optional
    mock -r fedora-23-x86_64 --no-clean --rebuild ./gapi-ocaml-0.2.8-1.fc23.src.rpm
    cd ..
```

3 - Prepare google-drive-ocamlfuse
```
    cd google-drive-ocamlfuse/
    spectool -g google-drive-ocamlfuse.spec
    rpmbuild -bs google-drive-ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
    cd ..
```

4 - Build google-drive-ocamlfuse in chain
```
    mockchain -r fedora-23-x86_64 -l resultsdir \
    ocamlfuse/ocamlfuse-2.7.1-1.cv2.fc23.src.rpm \
    gapi-ocaml/gapi-ocaml-0.2.8-1.fc23.src.rpm \
    google-drive-ocamlfuse/google-drive-ocamlfuse-0.5.22-1.fc23.src.rpm
```
