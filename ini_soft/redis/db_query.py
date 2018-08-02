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


    def insert_contents(self, table, cid, file_name):
        conn = self.conn
        curs = conn.cursor()

        #get a level of zero count
        level = db.select('level', 'content_level', 'min_counts=0')[0]['content_level']

        values = "(%s, '%s', '%s', now(), null)" % (cid, level, file_name)
        sql = "INSERT INTO %s VALUES %s" % (table, values)

        curs.execute(sql)
        conn.commit()
        rowcount = curs.rowcount
        curs.close()

        return rowcount


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
    # db.update_level(1, 'silver')
    # db.insert_content('contents', )
    db.insert_contents("contents", 21, "test.mp4")
