#!/bin/bash

set -ex
exec 3>&1 4>&2
trap 'exec 2>&4 1>&3' 0 1 2 3
exec 1>/tmp/startup_log.out 2>&1

sudo chmod o+rw /mydata

git clone --branch v1.2.1 https://gitlab.eurecom.fr/oai/openairinterface5g.git /mydata/openairinterface5g

