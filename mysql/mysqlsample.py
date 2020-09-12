# encoding = UTF-8

"""
    Oracle DB Handling...

    1. Select
    2. Insert
    3. Update
    4. Delete
"""
import pymysql

def connectDB():
    url = "idlecatmysql.cu3my8xgwpri.ap-northeast-2.rds.amazonaws.com"
    userid = "admin"
    passwd = "idlecat5717"
    dbname = "mercury"
    charset = "utf8"

    con = pymysql.connect(host=url, user=userid, password=passwd,  db=dbname, charset=charset)
    sql = "select * from user"
    try:
        with con.cursor() as curs:
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                print(row)
    finally:
        con.close()


def closeDB():
    pass

def selectItem():
    pass



def run():
    connectDB()


if __name__ == '__main__':
    run()
