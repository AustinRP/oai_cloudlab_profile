#!/bin/bash

if [ -d "/mydata" ]; then
  echo "Found /mydata" > /tmp/startup_log
  ls -hal /mydata > /tmp/startup_log
else
  echo "Could not find /mydata" > /tmp/startup_log
fi

