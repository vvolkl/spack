#!/bin/sh
set -ex
if [ "$TRAVIS_OS_NAME" = "linux" ]; then
    wget https://github.com/NixOS/patchelf/archive/0.10.tar.gz
    tar -xvf 0.10.tar.gz
    pushd patchelf-0.10 && ./bootstrap.sh && ./configure --prefix=/usr && make && sudo make install && popd
fi
