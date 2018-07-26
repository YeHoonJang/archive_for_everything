from flask import Flask
from flask import request
import pymysql
import json
import redis
from datetime import datetime
import requests
import db_query as db
app = Flask(__name__)

def get_level_from_db(post_id):
    table = "contents"
    column = "filename, content_level"
    where_clause = "cid=%s" % (post_id)
    rows = db.select(table, column, where_clause)

    # conn = pymysql.connect(host='192.168.10.37',
    #                          user='root',
    #                          password='ini6223',
    #                          db='redis_project',
    #                          charset='utf8',
    #                          )
    #
    # print ("connect successful!!")
    # try:
    #     with conn.cursor(pymysql.cursors.DictCursor) as curs:
    #         sql_1 = 'select filename, content_level from contents where cid = %s'
    #         curs.execute(sql_1, (post_id))
    #         rows_1 = curs.fetchall()
    #         sql_2 = 'select counts from level'
    #         curs.execute(sql_2)
    #         rows_2 = curs.fetchall()
    # finally:
    #     conn.close()
    #
    return rows

def redis_connection():
    rc = redis.Redis(host='192.168.10.37', port=6379, db=1)
    return rc

def get_target(a):
        if a>=2000:
            level = 'gold'
        elif a>=1000:
            level = 'silver'
        else:
            level = 'bronze'
        return level

def update_db_level(post_id, final_level):
    rowcount = db.update_level(post_id, final_level)
    # conn = pymysql.connect(host='127.0.0.1',
    #                        port=server.local_bind_port,
    #                        user='root',
    #                        passwd='ini6223',
    #                        db='redis_project')
    # curs = conn.cursor()
    # new_date = datetime.now().strftime("""%Y-%m-%d %H:%M:%S""")
    # sql_1 =  "UPDATE contents SET content_level = '%s', update_time = '%s' WHERE cid = '%s'" %(final_level, new_date, post_id)
    # curs.execute(sql_1)
    # conn.commit()
    return rowcount



@app.route('/get_sentence',methods=['POST', 'GET'])
def set_contents_redis():
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    target = get_target(int(data['count']))
    data['target'] = target
    filename = get_level_from_db(data['cid'])['filename']
    db_level = get_level_from_db(data['cid'])['content_level']
    data['db_level'] = db_level
    data['filename'] = filename
    data['worker_id'] = None
    rc = redis_connection()
    if target != db_level:
        data['status'] = 'update'
    else:
        data['status'] = 'done'
    rc.set(data['cid'],json.dumps(data).encode('utf-8'))
    return rc.get(data['cid'])

@app.route('/update_sentence', methods=['GET','POST'])
def update_sentence():
    cid = request.form['cid']
    rc = redis_connection()
  #  print("this is cid : ", cid)
    if json.loads(rc.get(cid))['status']=="done":
       update_db_level(cid,json.loads(rc.get(cid))['target'])
       print("check done and db update success")
       return cid
    else:
       print("check content status again")
       return "check your status again"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
