#!/bin/sh
docker run --rm \
  -v mc_data:/data \
  -v "$(pwd)":/backup \
  busybox \
  sh -c "cd /data && tar xzf /backup/mc_data_backup.tgz"
