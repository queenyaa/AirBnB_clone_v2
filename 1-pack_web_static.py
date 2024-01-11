#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
import os

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

        local("tar -cvzf {} web_static".format(archive_p))
        return archive_p
    except Exception as e:
        return None


if __name__ == '__main__':
    result = do_pack()
    if result:
        in_put = "web_static packed: {} -> {}Bytes"
        print(in_put.format(result, os.path.getsize(result)))
    else:
        print("Packing failed.")
