import pymysql
from datetime import datetime

class db:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'ini6223'
        self.db = 'redis_project'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8')


    def select(self, table=None, column=None, where_clause=None):
        self.table = table
        self.column = column
        self.where_clause = where_clause

    # TODO: column name 보여주는 거
        conn = self.conn
        curs = conn.cursor(pymysql.cursors.DictCursor)
        if self.where_clause != None:
            sql = "SELECT %s FROM %s WHERE %s" % (self.column, self.table, self.where_clause)
        else:
            sql = "SELECT %s FROM %s" % (self.column, self.table)

        curs.execute(sql)
        rows = curs.fetchall()

        print("\n------------ " + table + " table ------------")
        for row in rows:
            print(row)
        print("\n")
        curs.close()


    def update_level(self, cid, content_level):
        self.cid = cid
        self.content_level = content_level
        conn = self.conn
        curs = conn.cursor()

        new_date = datetime.now().strftime("""%Y-%m-%d %H:%M:%S""")

        sql = "UPDATE contents SET content_level = '%s', update_time = '%s' WHERE cid = '%s'" % (self.content_level, new_date, self.cid)

        curs.execute(sql)
        conn.commit()

        db.select('contents', '*')
        curs.close()


if __name__ == '__main__':
    db = db()
    db.select("update_history", "*", "new_content_level = 'gold'")
