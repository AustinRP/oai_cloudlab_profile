#!/bin/bash

set -e

source /local/repository/shared_startup.sh

cd /mydata/openairinterface5g
source oaienv
cd cmake_targets/
./build_oai -I -w USRP --UE
