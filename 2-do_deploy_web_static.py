#!/usr/bin/python3

"""
Fabric script to deploy a package
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.237.74.212', '100.25.159.153']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    try:
        if not exists(archive_path):
            return False

        file_n = archive_path.split("/")[-1]
        file_n_ext = file_n.split(".")[0]
        l_path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(l_path, file_n_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, l_path, file_n_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(l_path, file_n_ext))
        run('rm -rf {}{}/web_static'.format(l_path, file_n_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(l_path, file_n_ext))
        return True

    except Exception as e:
        return False
