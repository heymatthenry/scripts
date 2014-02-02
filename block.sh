#! /bin/sh

cp /etc/hosts.blocker /etc/hosts
dscacheutil -flushcache
