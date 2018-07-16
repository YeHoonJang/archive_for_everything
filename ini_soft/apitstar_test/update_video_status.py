import os
from apistar import App, Route
import pymysql
from datetime import datetime

conn = pymysql.connect(host='localhost', user='root', password='ini6223', db='wordpress', charset='utf8')

def update_video_status(app:App, db:conn, video_id:int):
    print(video_id)
    now = datetime.now()
    formatted_date = now.strftime("""%Y-%m-%d %H:%M:%S""")

    curs = conn.cursor()
    update_sql = "UPDATE wp_uploaded_video SET status='delete', uploaded_time=%s WHERE video_id=%s"
    curs.execute(update_sql, (formatted_date, video_id))
    print(video_id)
    conn.commit()
    return "success connection"


routes = [
Route('/{video_id}', method='GET', handler=update_video_status)
]
app = App(routes=routes)


if __name__ == "__main__":
    app.serve('192.168.10.37', 5000, use_debugger=True)
    print("여기")
