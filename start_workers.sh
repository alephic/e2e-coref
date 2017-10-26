#!/bin/bash

./start_worker.sh $1 0 &
w0=$!
./start_worker.sh $1 1 &
w1=$!
trap "kill $w0 $w1" SIGINT
