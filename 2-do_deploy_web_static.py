#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy it
"""
import os.path
from fabric.api import run, put, env

env.hosts = ['35.175.134.77', '54.82.176.227']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it

    Args:
        archive_path (str): Path to the archive to be deployed

    Returns:
        bool: True if all operations have been done correctly, False otherwise
    """
    if not os.path.exists(archive_path):
        raise FileNotFoundError("Archive file not found.")

    archive_file = os.path.basename(archive_path)
    archive_folder = os.path.splitext(archive_file)[0]

    put(archive_path, "/tmp/")
    with cd("/tmp"):
        run("tar -xzf {} -C /data/web_static/releases/{}/".format(
            archive_file, archive_folder))

    with cd("/data/web_static/releases/{}/".format(archive_folder)):
        run("mv web_static/* .")
        run("rm -rf web_static")

    with cd("/data/web_static/"):
        run("rm -rf current")
        run("ln -s releases/{}/ current".format(archive_folder))

    print("New version deployed!")
    return True
