#!/bin/sh

set -eux

RPM_DIR=rpms/
SRC=src/

build_srpms() {
    spec_file=$1
    sources=$2

    spectool -g ${spec_file} --directory ${SRC}
    mock --buildsrpm --spec ${spec_file} --sources ${SRC}/${sources} --resultdir $RPM_DIR
}

rm -rf ${RPM_DIR}
mkdir -p ${RPM_DIR} ${SRC}

build_srpms guake.spec 3.4.0.tar.gz

mock --resultdir $RPM_DIR $RPM_DIR*.src.rpm


