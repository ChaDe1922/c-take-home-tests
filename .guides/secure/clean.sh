#!/bin/bash
echo "$HOME/workspace/.guides/secure/$1"
cd $HOME/workspace/.guides/secure/$1
make clean || true
echo "clean autotools"
rm -rf autom4te.cache build-aux m4 aclocal.m4 config.log config.status configure libtool Makefile Makefile.in || true
rm -rf src/.deps src/.libs src/Makefile src/Makefile.in || true
rm -rf tests/.deps src/.libs tests/Makefile tests/Makefile.in || true