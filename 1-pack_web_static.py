#!/usr/bin/python3
"""
This file will help set up the web static stuff with a .tgz archive
"""


def do_pack():
    """ This sets up the tgz """
    from datetime import datetime
    from fabric.api import local
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    try:
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(time))
    except:
        return None
