#!/bin/bash

set -e
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/tmp/startup_log.out 2>&1
set -x

source /local/repository/shared_startup.sh

cd /mydata/openairinterface5g
source oaienv
cd cmake_targets/
./build_oai -I -w USRP --UE
