import psycopg2
import urllib.parse as urlparse
import os


def database_connection():
    database=psycopg2.connect(
            host="ec2-54-82-205-3.compute-1.amazonaws.com",
            database="d540clukt96u83",
            user="trtztcfphkhoxq",
            password="9160185682d54840d0c645c756947ac6259a4d3d983b016e857e39a863744623")
    return database
