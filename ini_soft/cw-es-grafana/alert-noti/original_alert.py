# -*- coding: utf-8 -*-

from flask import Flask, request, abort, Response
from flask_cors import CORS, cross_origin
import json
import logging
import requests
import urllib
import json
import datetime
import time

app = Flask(__name__)


@app.route("/api/webhook/hangouts",methods=["POST","PUT"])
def webhook():
    # logging.info(request.get_data())
    message = json.loads(request.get_data())
    #{"evalMatches":[],"message":"Test Message","ruleId":8,"ruleName":"ELB Status Error 400 alert","ruleUrl":"http://13.231.223.137:3000/d/4dgCpYbmz/ls-monit-v1-0?fullscreen=true\u0026edit=true\u0026tab=alert\u0026panelId=8\u0026orgId=1","state":"alerting","title":"[Alerting] ELB Status Error 400 alert"}
    message["ruleUrl"] = message["ruleUrl"].replace("13.231.223.137:3000", "grafana.drmkeyserver.com")
    message["ruleUrl"] = message["ruleUrl"].replace("&edit=true&tab=alert", "")
    message["ruleUrl"].replace("&edit=true", "")

    url_list = message["ruleUrl"].split("/")
    url = "%s//%s"%(url_list[0],url_list[2])
    parameter = url_list[-1].split("?")
    page = parameter[0]
    parm_str = ""
    for i in parameter[1].split("&"):
        if "orgId" in i:
            parm_str = "%s%s&"%(parm_str,i)

        if "panelId" in i:
            panel_id = i.split("=")[-1]
            parm_str = "%s%s&"%(parm_str,i)

    auth_key = "Bearer eyJrIjoiNjdKNGtHS2J0Ym9pZlVlOGloNG5yMnpzaUtTUmZGR1oiLCJuIjoicG5nLXRlc3QiLCJpZCI6MX0="
    header = {"Authorization" : auth_key,"Accept":"application/json", "Content-Type":"application/json"}
    timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
    request_png_url = "%s/render/d-solo/%s/%s?%sto=%d&from=%d&width=1000&height=500&tz=Asia\Seoul.png"%(url,url_list[4],page,parm_str,timestamp*1000,(timestamp-7200)*1000)
    request_png_url = request_png_url.replace("\\","%2F")
    # logging.info(request_png_url)
    png_name = "%s-%s.png"%(url_list[4], panel_id)
    # logging.info(png_name)
    r = requests.get(request_png_url, headers=header)
    # with open("/usr/share/nginx/html/%s"%png_name,"w+") as f:
    #     for chunk in r.iter_content(1024):
    #         f.write(chunk)
    message["imageUrl"] = "https://license-eval.drmkeyserver.com/%s"%(png_name)
    # logging.info("get_png")
    text_msg = {
        "cards": [
            {
                "header": {
                    "title": message["title"],
                    "subtitle": message["message"]
                },
                "sections": [
                    {
                        "header": message["title"],
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": message["imageUrl"]
                                }
                            }
                        ]
                    },
                    {
                        "widgets": [
                                {
                                        "buttons": [
                                            {
                                                "textButton": {
                                                    "text": "Enter monit",
                                                    "onClick": {
                                                        "openLink": {
                                                            "url": message["ruleUrl"]
                                                        }
                                                    }
                                                }
                                            },
                                            {
                                                "textButton": {
                                                    "text": "PNG open",
                                                    "onClick": {
                                                        "openLink": {
                                                            "url": message["imageUrl"]
                                                        }
                                                    }
                                                }
                                            }
                                        ]
                                }
                        ]
                    }
                ]
            }
        ]
    }
    headers = {"Content-Type":"application/json"}
    #r = requests.post("https://chat.googleapis.com/v1/spaces/AAAAeJtZeRg/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jCu5LSqYHrGU8xtTV-NJKLyPTCGzUfFOnrzyjIctgO8%3D", data=json.dumps(text_msg), headers=headers)
    #r = requests.post("https://chat.googleapis.com/v1/spaces/AAAAm90Stuc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5r_lzMnZFyOMmlkeXe3z6UsyOuMc4HoNrMdEq9mWme0%3D", data=json.dumps(text_msg), headers=headers)
    r = requests.post("https://chat.googleapis.com/v1/spaces/AAAAv60PSr0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=P_T2VrBXRuaRMDO9m_OksEdLlNADfQ23v1khca8mnGI%3D", data=json.dumps(text_msg), headers=headers)

    # logging.info(r.text)

    return "200"

if __name__ == "__main__":
    app.run(host='192.168.10.135', port='1005', debug=True)
