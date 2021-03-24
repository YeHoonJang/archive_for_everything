import os
from apistar import App, Route, http
import pymysql
from datetime import datetime
import webbrowser



conn = pymysql.connect(host='localhost', user='root', password='ini6223', db='wordpress', charset='utf8')

def is_validated_user(app:App, video_id:str):
    curs = conn.cursor()
    user_name = 'test'

    select_id = "SELECT ID FROM wp_users WHERE user_login=%s"
    curs.execute(select_id, user_name)
    user_id = curs.fetchall()[0][0]

    select_author = "SELECT author FROM wp_uploaded_video WHERE video_id=%s"
    curs.execute(select_author, video_id)
    author = curs.fetchall()[0][0]

    if user_id == author:
        return update_video_status(video_id, user_id)
    else:
        return "your user name is imvalidated"


def update_video_status(video_id, user_id):
    now = datetime.now()
    formatted_date = now.strftime("""%Y-%m-%d %H:%M:%S""")

    curs = conn.cursor()
    update_status = "UPDATE wp_uploaded_video SET status='delete', uploaded_time=%s WHERE video_id=%s"
    curs.execute(update_status, (formatted_date, video_id))
    conn.commit()

    return webbrowser.open('http://192.168.10.37/my_video_list')
    # headers = {'Location', 'http://192.168.10.37/my_video_list'}

routes = [
    Route('/{video_id}', method='GET', handler=is_validated_user),
    # Route('/{video_id}', method='GET', handler=update_video_status)
]

app = App(routes=routes)


if __name__ == "__main__":
    app.serve('192.168.10.37', 5000, use_debugger=True)
