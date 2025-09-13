import errno
import hashlib
import os

import mysql.connector


class DBHolder:
    def __init__(self, _config=None):
        if _config is None:
            _config = {
                "host": "localhost",
                "user": "root",
                "passwd": "root",
                "database": "test",
                "pool_name": "mypool",
                "pool_size": 3
            }
        self.mydb = mysql.connector.connect(
            **_config
        )

    def fetchall(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        entities = mycursor.fetchall()
        return entities

    def __del__(self):
        self.mydb.close()


def short_url(url):
    return hashlib.md5(url.encode('utf-8')).hexdigest()[-6:]


def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except OSError as exec1:
            if exec1.errno != errno.EEXIST:
                raise


def joke():
    return (
        "it's a joke"
    )
# __all__ = ['short_url']
