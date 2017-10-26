#!/bin/bash

./start_worker.sh $1 0 &
w0=$!
./start_worker.sh $1 1 &
w1=$!
./start_worker.sh $1 2 &
w2=$!
trap "kill $w0 $w1 $w2" SIGINT
