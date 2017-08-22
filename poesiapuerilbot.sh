#!/bin/bash
# this script should be run from the user's home (not from /opt/poesiapueril/
nohup python3 /opt/poesiapueril/poesiapuerilbot.py > /opt/poesiapueril/log/errors.log 2>&1  &
