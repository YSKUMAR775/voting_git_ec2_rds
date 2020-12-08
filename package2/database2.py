import pymysql


def db_conn():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='S@i30051995',
                         db='voting'
                         )
    return db
