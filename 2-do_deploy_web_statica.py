#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import env, put, run
import os

# Define the environment and variables
env.hosts = ['54.237.74.212', '100.25.159.153']
env.user = 'ubuntu'
env.key_filename = ['/root/.ssh/id_rsa']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/file.jkp
        filen = os.path.basename(archive_path)
        filen_no_ext = os.path.splitext(filen)[0]
        # release_p = '/tmp/{}'.format(filen_no_ext)
        release_p = '/data/web_static/releases/{}'.format(filen_no_ext)
        # print("Release Path:", release_p)
        # run('sudo rm -rf {}'.format(release_p)) # remove existing pkg
        run('sudo mkdir -p {}'.format(release_p))
        run('tar -xzf /tmp/{} -C {}'.format(filen, release_p))

        # permit_user = sudo chown -R ubuntu:ubuntu {}
        # run('sudo chown -R /data/')
        run('sudo chown -R ubuntu:ubuntu {}'.format(release_p))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filen))

        # Delete the symbolic link /data/web_static/current
        cur_link = '/data/web_static/current'
        run('rm -f {}'.format(cur_link))
        # Create a new symbolic link
        run('ln -s {} {}'.format(release_p, cur_link))

        return True
    except Exception as e:
        return False
