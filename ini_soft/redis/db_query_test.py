import pymysql
from datetime import datetime

class db:
    def __init__(self):
        self.host = '192.168.10.37'
        self.user = 'root'
        self.password = 'ini6223'
        self.db = 'redis_project'
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8')


    def select(self, table=None, column=None, where_clause=None):
        # if table == None and column == None:
        #     table = input("table : ")
        #     column = input("column (if you want to select all columns, write all or *) : ")
        #     if column == "all":column = "*"
        #     self.table = table
        #     self.column = column
        # else:

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

        db.select('contents', '*')
        curs.close()

        return rowcount
    #update_history 테이블 업데이트
    # def insert_history(self, cid, content_level):
    #     self.cid = cid
    #     self.content_level = content_level
    #     conn = self.conn
    #     curs = conn.cursor()
    #
    #     get_number_of_row_sql = "SELECT cid FROM update_history WHERE cid = '%s'" % (self.cid)
    #     curs.execute(get_number_of_row_sql)
    #     rows = curs.fetchall()
    #
    #     if len(rows) >= 1:
    #         get_old_date_sql = "SELECT max(new_updated_date) FROM update_history WHERE cid = '%s'" % (self.cid)
    #     else:
    #         get_old_date_sql = "SELECT update_time FROM contents WHERE cid='%s'" % (self.cid)
    #
    #     curs.execute(get_old_date_sql)
    #     old_date = curs.fetchall()[0][0]
    #
    #     new_date = datetime.now().strftime("""%Y-%m-%d %H:%M:%S""")
    #
    #     sql = "INSERT INTO update_history VALUES ('%s', '%s', '%s', '%s')" % (str(self.cid), str(old_date), str(new_date), str(self.content_level))
    #
    #     curs.execute(sql)
    #     conn.commit()
    #     db.select('update_history', '*')
    #     curs.close()


if __name__ == '__main__':
    db = db()
    table = "update_history"
    db.select(table, "*", "new_content_level = 'gold'")
    # db.select()
    # db.update_level(12, 'silver')
