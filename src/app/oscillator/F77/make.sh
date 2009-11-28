#!/bin/sh -x
compiler=gfortran
options=-O3
$compiler -o oscillator $options oscillator.f

# install the oscillator executable:
if [ ! -d $scripting/$MACHINE_TYPE/bin ]; then
  mkdirhier $scripting/$MACHINE_TYPE/bin
fi
mv -f oscillator $scripting/$MACHINE_TYPE/bin


