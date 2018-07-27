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
        self.table = table
        self.column = column
        self.where_clause = where_clause
        self.order_by = order_by

        conn = self.conn
        curs = conn.cursor(pymysql.cursors.DictCursor)
        if self.where_clause != None and self.order_by != None:
            sql = "SELECT %s FROM %s WHERE %s ORDER BY %s" % (self.column, self.table, self.where_clause, self.order_by)
        elif self.where_clause != None and self.order_by == None:
            sql = "SELECT %s FROM %s WHERE %s" % (self.column, self.table, self.where_clause)
        elif self.where_clause == None and self.order_by != None:
            sql = "SELECT %s FROM %s ORDER BY %s" % (self.column, self.table, self.order_by)
        else:
            sql = "SELECT %s FROM %s" % (self.column, self.table)

        curs.execute(sql)
        rows = curs.fetchall()
        curs.close()

        return rows


    def update_level(self, cid, content_level):
        self.cid = cid
        self.content_level = content_level
        conn = self.conn
        curs = conn.cursor()

        new_date = datetime.now().strftime("""%Y-%m-%d %H:%M:%S""")

        sql = "UPDATE contents SET content_level = '%s', update_time = '%s' WHERE cid = '%s'" % (self.content_level, new_date, self.cid)

        curs.execute(sql)
        conn.commit()
        rowcount = curs.rowcount

        curs.close()

        return rowcount
