#!/bin/sh

echo "%{F#2495e7} %{F#ffffff}$(/usr/sbin/ifconfig eno1 | grep "inet " | awk '{print $2}')%{u-}"
