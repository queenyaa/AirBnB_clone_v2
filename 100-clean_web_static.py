#!/usr/bin/python3

"""
Fabric script to delete older version of packages
"""

from fabric.api import run, env
from fabric.context_managers import cd, lcd
from datetime import datetime
import os

env.hosts = ['54.237.74.212', '100.25.159.153']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    Delete older versions of packages in versions and release folders
    """
    try:
        number = int(number)
        if number < 0:
            return False
        # Local clean
        with lcd('versions'):
            local('lt -t | tail -n +{} | xargs rm -f'.format(number + 1))

        # Remote clean on each server
        with cd('/data/web_static/releases'):
            run('ls -t | tail -n +{} | xargs rm -f'.format(number + 1))

        with cd('/data/web_static'):
            run('ls -t versions | tail -n + {} | xargs rm -rf'.format
                (number + 1 ))

        print("Old versions cleaned successfully!")
        return True

    except Exception as e:
        return False
