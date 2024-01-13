#!/usr/bin/python3

"""
Fabric script to delete older version of packages
"""

from fabric.api import run, env, local
from fabric.context_managers import cd
from datetime import datetime
import os

env.hosts = ['54.237.74.212', '100.25.159.153']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Delete older versions of packages in versions and release folders
    this should go into the version directory find the number
    of version listed then delete both locally
    and on each deployment web server
    """
    try:
        number = int(number)
        if number < 0:
            return False
        # Local clean
        with local.cwd('versions'):
            local('lt -t | tail -n +{} | xargs rm -f'.format(number + 1))

        # Remote clean on each server
        with cd('/data/web_static/releases'):
            run('find . -maxdepth 1 -type d -name "web_static*" \
                | sort - r | tail -n +{} | xargs rm -f'.format(number + 1))

        with cd('/data/web_static'):
            run('find versinos -maxdepth 1 -type d | sort -r \
                | tail -n + {} | xargs rm -rf'.format
                (number + 1))

        print("Old versions cleaned successfully!")
        return True

    except Exception as e:
        return False
