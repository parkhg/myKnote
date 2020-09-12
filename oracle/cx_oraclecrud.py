# encoding = UTF-8

"""
    Oracle DB Handling...

    1. Select
    2. Insert
    3. Update
    4. Delete
"""
import cx_Oracle

def connectDB():
    url = "idlecatoracle.cu3my8xgwpri.ap-northeast-2.rds.amazonaws.com"
    userid = "admin"
    passwd = "idlecat5717"
    CONNECTINFO = userid + '/' + passwd + '@' + url

    con = cx_Oracle.connect(CONNECTINFO)
    cur = con.cursor()
    sql = "select 1 from dual"
    cur.execute(sql)

    for row in cur:
        for i in range(len(row)):
            print(row[i], end="")

    cur.close()
    con.close()

    return con

def closeDB():
    pass

def selectItem():
    pass



def run():
    connectDB()


if __name__ == '__main__':
    run()
