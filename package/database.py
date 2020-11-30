import pymysql


def db_connect():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='S@i30051995',
                         db='voting_rds'
                         )
    return db
