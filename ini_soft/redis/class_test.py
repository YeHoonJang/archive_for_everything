import db_query as db

def select_test(cid):
    table = "contents"
    columns = "filename"
    where = "cid = %s" % cid
    db_conn = db.db()
    rows = db_conn.select(table, columns, where)
    return rows
if __name__ == "__main__":
    select_test(1)
