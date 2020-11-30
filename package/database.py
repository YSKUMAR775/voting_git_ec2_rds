import pymysql


def db_connect():
    db = pymysql.connect(host='aws2.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                         user='root',
                         password='S@i30051995',
                         db='voting_rds'
                         )
    return db
