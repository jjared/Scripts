#!/bin/bash
# Simple port scanner

if [ -z $1 ]; then
	read -p "IP to scan: " host;
else
	host=$1
fi
for port in {1..65535}; do
	timeout .1 bash -c "echo >/dev/tcp/$host/$port" &&
	echo "Port $port is open";
done
echo "Done"