#Set fedora version
ARG FEDORA_VERSION=37

#We will build on Rocky 9
FROM fedora:$FEDORA_VERSION

#Install RPM dev dependencies
RUN dnf install -y dnf-plugins-core
#RUN dnf config-manager -y --set-enabled crb
#RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
RUN dnf update -y
RUN dnf install -y rpmdevtools

#Install build dependencies


#Copy source files to container
WORKDIR /build/gdfs
COPY . .