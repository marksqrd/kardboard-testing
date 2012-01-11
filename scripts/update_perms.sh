#!/bin/sh

# Set ownership to supplied argument or the most common user/group pairing relative the current directory.  (searches three in depth)
# Sets directory sticky bit and group shared based permissioning

pushd /services/kardboard

[ -z "$1" ] &&
set `find $PWD -maxdepth 3 -printf '%u:%g\n' | uniq -cd | sort -n | awk 'END{print $2}'`

echo "Updating $PWD to $1"

{
chown -R $1 $PWD
find $PWD -type d -exec chmod 2770 {} \;
find $PWD -type f -exec chmod u+rw,g+rw,o= {} \;
} &
