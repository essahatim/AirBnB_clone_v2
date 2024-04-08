#!/usr/bin/python3
"""
Fabric script to generates a .tgz archive from the contents of the web_static
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_file = 'versions/web_static_{}.tgz'.format(timestamp)
    if os.path.isdir("versions") is False:
        if local('mkdir -p versions').failed is True:
            return None
    result = local('tar -cvzf {} web_static'.format(archive_file))
    return archive_file if result.succeeded else None
