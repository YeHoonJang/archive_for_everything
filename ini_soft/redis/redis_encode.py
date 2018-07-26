from flask import Flask
from flask import request
from flask_restful import reqparse
import pymysql
import json
from sshtunnel import SSHTunnelForwarder
import redis
from ast import literal_eval
from datetime import datetime

app = Flask(__name__)

def get_level_from_db(post_id):
    with SSHTunnelForwarder(
        ('192.168.10.37', 22),
        ssh_password="ini6223",
        ssh_username="inisoft",
        remote_bind_address=('127.0.0.1', 3306)) as server:
        conn = pymysql.connect(host='127.0.0.1',port=server.local_bind_port,
                           user='root',
                           passwd='ini6223',
                           db='redis_project')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql_1 = 'select filename, content_level from contents where cid = %s'
        curs.execute(sql_1, (post_id))
        rows_1 = curs.fetchone()
        sql_2 = 'select counts from level'
        curs.execute(sql_2)
        rows_2 = curs.fetchone()
        conn.close()
        
    return rows_1

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
    with SSHTunnelForwarder(
             ('192.168.10.37', 22),
             ssh_password="ini6223",
             ssh_username="inisoft",
             remote_bind_address=('127.0.0.1', 3306)) as server:

        conn = pymysql.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user='root',
                               passwd='ini6223',
                               db='redis_project')
        curs = conn.cursor()
        new_date = datetime.now().strftime("""%Y-%m-%d %H:%M:%S""")
        sql_1 =  "UPDATE contents SET content_level = '%s', update_time = '%s' WHERE cid = '%s'" %(final_level, new_date, post_id)
        curs.execute(sql_1)
        conn.commit()
    return curs.rowcount



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
    rc = redis_connection()
    if target != db_level: 
        data['status'] = 'update'
    else:
        data['status'] = 'done'
    rc.set(data['cid'],json.dumps(data).encode('utf-8'))
    return rc.get(data['cid'])

@app.route('/update_sentence', methods=['GET','POST'])
def profile():
    cid = request.form['cid']
    rc = redis_connection()
    if literal_eval(rc.get(cid).decode('utf-8'))["status"]=="done":
       update_db_level(cid, literal_eval(rc.get(cid).decode('utf-8'))['target'])
       return "update success"
    else:
        return "check your status again"



if __name__ == '__main__':
    app.run()

