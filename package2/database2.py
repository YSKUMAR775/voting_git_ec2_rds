import pymysql


def db_conn():
    db = pymysql.connect(host='aws2.c42ojr1a1cpj.ap-south-1.rds.amazonaws.com',
                         user='admin',
                         password='yskumar775',
                         db='voting_rds'
                         )
    return db
