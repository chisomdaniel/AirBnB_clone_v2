#!/usr/bin/python3

'''
Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack.
'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''
    Generates a .tgz archive file

    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist)
    Return the archive path if the archive has been correctly generated.
    Otherwise, it should return None
    '''

    dt = datetime.now()
    timestamp = f"{dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}"

    if not os.path.exists('versions'):
        os.mkdir('versions')

    output = local(f"tar -cvzf versions/web_static_{timestamp}.tgz web_static")

    if (output.failed is False):
        return (f"versions/web_static_{timestamp}.tgz")
    else:
        return (None)
