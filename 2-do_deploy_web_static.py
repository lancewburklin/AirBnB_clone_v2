#!/usr/bin/python3
"""
This file will help set up the web static stuff with a .tgz archive
"""
from fabric.api import run, put
from fabric.state import env
env.hosts = ['34.75.100.36', '54.159.26.151']


def do_deploy(archive_path):
    """ This sets up the tgz """
    try:
        thingy = archive_path.split("/")[1]
        thingy2 = thingy.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(thingy2))
        put(archive_path, '/tmp')
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            thingy, thingy2))
        run("rm /tmp/{}".format(thingy))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current".
            format(thingy2))
    except:
        return None
