from flask import Flask, request, abort, Response
from flask_cors import CORS, cross_origin
import json
import logging
import requests
import urllib

import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import schedule


app = Flask(__name__)

# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#
# def scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(func=print_date_time, trigger="interval", seconds=30)
#     scheduler.start()
#
#     # Shut down the scheduler when exiting the app
#
#     atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def hello_world():

    return "hi"

@app.route('/webhook', methods=['POST, PUT'])
def webhook():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return time.strftime("%A, %d. %B %Y %I:%M:%S %p")

# def job():
#     print("I'm working...")
#     now = time.gmtime(time.time())
#     print(now.tm_hour+9, now.tm_min, now.tm_sec)

    # print(schedule.every(1).minutes.do(job))
    # while True:
    #     schedule.run_pendeing()
    #     time.sleep(1)


# def job_schedule():

# print("Are you there?")
# job()
# schedule.every(1).minutes.do(job)
# while True:
#     schedule.run_pendeing()
#     time.sleep(1)

# job_schedule()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
