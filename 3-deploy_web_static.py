#!/usr/bin/python3

"""
Fabric script to deploy a package
"""

from fabric.api import put, local, run, env
from os.path import isdir, exists, isfile
from datetime import datetime
import os

env.hosts = ['54.237.74.212', '100.25.159.153']
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
        if isdir("versions") is False:
            local('mkdir -p versions')
        archive_p = "versions/web_static_{}.tgz".format(cur_time)
        # archive_path = "versions/{}".format(archive_n)

        # local('mkdir -p versions')
        local("tar -cvzf {} web_static".format(archive_p))
        # if result.failed:
            # return None
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not isfile(archive_path):
        return False
    try:
        # if not isfile(archive_path):
            # return False

        file_n = archive_path.split("/")[-1]
        file_n_ext = file_n.split(".")[0]
        l_path = "/data/web_static/releases/"

        # if not exists(archive_path):
            # return False

        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(l_path, file_n_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format
            (file_n, l_path, file_n_ext))
        run('sudo rm /tmp/{}'.format(file_n))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(l_path, file_n_ext))
        run('sudo rm -rf {}{}/web_static'.format(l_path, file_n_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format
            (l_path, file_n_ext))
        print("New version deployed!")
        return True

    except Exception as e:
        return False

def deploy():
    """
    Deploys the archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
