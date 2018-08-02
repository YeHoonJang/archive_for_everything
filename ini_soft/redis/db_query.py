import pymysql
from datetime import datetime

class db:
    def __init__(self):
        self.host = '192.168.10.37'
        self.user = 'root'
        self.password = 'ini6223'
        self.db = 'redis_project'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8')


    def select(self, table, column, where_clause=None, order_by=None):
        conn = self.conn
        curs = conn.cursor(pymysql.cursors.DictCursor)
        if where_clause != None and order_by != None:
            sql = "SELECT %s FROM %s WHERE %s ORDER BY %s" % (column, table, where_clause, order_by)
        elif where_clause != None and order_by == None:
            sql = "SELECT %s FROM %s WHERE %s" % (column, table, where_clause)
        elif where_clause == None and order_by != None:
            sql = "SELECT %s FROM %s ORDER BY %s" % (column, table, order_by)
        else:
            sql = "SELECT %s FROM %s" % (column, table)

        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()

        return rows


    def update_level(self, cid, content_level):
        conn = self.conn
        curs = conn.cursor()

        sql = "UPDATE contents SET content_level = '%s', update_time = now() WHERE cid = '%s'" % (content_level, cid)

        curs.execute(sql)
        conn.commit()
        rowcount = curs.rowcount
        curs.close()

        return rowcount

if __name__ =="__main__":
    db = db()
    db.update_level(1, 'silver')
