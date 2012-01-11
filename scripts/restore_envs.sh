#!/bin/sh

# Restore test/prod from Mongodb idump
for env in prod test; do for db in cheisel-backup/kardconfig/dump/kardboard/*.bson; do mongorestore --drop -d kardboard-$env -c `echo $db | sed -r 's,.*/([^.]+).*,\1,;s/_//'` $db; done; done
