from apistar import App, Route
import os


def test(data:RequestData):
    print("Okay")

routes = [
Route('192.168.10.37/my_video_list', method='POST', handler=test)
]
