#! /bin/bash
# 注意: 同步此文件后它应该同步到/home/scripts
# shellcheck disable=SC1090
export FLASK_ENV=production
export FLASK_DEBUG=False
cd /home/about_me || echo "无法进入/home/about_me"
exec python3 -m gunicorn -c ./gunicorn.conf.py server.main:app --preload --daemon

