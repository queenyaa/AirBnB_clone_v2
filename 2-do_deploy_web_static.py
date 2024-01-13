#!/usr/bin/python3

"""
Fabric script to deploy a package
"""

from fabric.api import put, run, env, local
from os.path import exists
from datetime import datetime
import os

env.hosts = ['54.237.74.212', '100.25.159.153']
# env.hosts = ['100.25.159.153']
env.user = 'ubuntu'


# Ensure the existence of the versions folder
if not os.path.exists("versions"):
    os.makedirs("versions")


def do_pack():
    """
    function to generate a .tgz archive from the contents of web_static
    """

    try:
        date_f = "%Y%m%d%H%M%S"
        cur_time = datetime.utcnow().strftime(date_f)
        archive_n = "web_static_{}.tgz".format(cur_time)
        archive_p = "versions/{}".format(archive_n)

        local("sudo tar -cvzf {} web_static".format(archive_p))
        return archive_p
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    try:
        # if not exists(archive_path):
        # return False

        file_n = archive_path.split("/")[-1]
        file_n_ext = file_n.split(".")[0]
        l_path = "/data/web_static/releases/"

        if not exists(archive_path):
            return False

        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(l_path, file_n_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format
            (file_n, l_path, file_n_ext))
        run('rm /tmp/{}'.format(file_n))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(l_path, file_n_ext))
        run('sudo rm -rf {}{}/web_static'.format(l_path, file_n_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {}{}/ /data/web_static/current'.format
            (l_path, file_n_ext))
        print("New version deployed!")
        return True

    except Exception as e:
        return False
