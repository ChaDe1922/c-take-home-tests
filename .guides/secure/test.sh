#!/bin/bash

function run_cmd {
  OUTPUT="$($1 2>&1)"
  CODE=$?
  if [ $CODE -ne 0 ] 
  then
    echo "$OUTPUT"
  fi
}

#cp ~/workspace/calc.c ~/workspace/.guides/secure/$1/src/
python3 $HOME/workspace/.guides/secure/moveStdtCode.py ~/workspace/$1.c $1.h ~/workspace/.guides/secure/$1/src/$1.c

cd $HOME/workspace/.guides/secure/$1

run_cmd 'autoreconf --install'
run_cmd './configure'
run_cmd 'make'
run_cmd 'make check'
tests/$2