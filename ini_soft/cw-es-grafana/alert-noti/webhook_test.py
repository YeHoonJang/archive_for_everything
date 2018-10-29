#-*- coding: utf-8 -*-
from flask import (
    Flask,
    request,
    Response
)
# from flask_cors import CORS, cross_origin
import json
import logging
import requests
app = Flask(__name__)
# CORS(app)
# logging.basicConfig(
#     format='%(asctime)s [%(levelname)s] %(message)s',
#     filename='/var/log/webapi.log',
#     level=logging.INFO
# )

@app.route("/webhook",methods=["POST","PUT"])
def webhook():
    logging.info(request.get_data())
    message = json.loads(request.get_data())
    #{"evalMatches":[{"value":100,"metric":"High value","tags":null},{"value":200,"metric":"Higher Value","tags":null}],"imageUrl":"http://grafana.org/assets/img/blog/mixed_styles.png","message":"Someone is testing the alert notification within grafana.","ruleId":0,"ruleName":"Test notification","ruleUrl":"http://13.231.223.137:3000/","state":"alerting","title":"[Alerting] Test notification"}
    #{"evalMatches":[],"message":"Test Message","ruleId":8,"ruleName":"ELB Status Error 400 alert","ruleUrl":"http://13.231.223.137:3000/d/4dgCpYbmz/ls-monit-v1-0?fullscreen=true\u0026edit=true\u0026tab=alert\u0026panelId=8\u0026orgId=1","state":"alerting","title":"[Alerting] ELB Status Error 400 alert"}
    message["ruleUrl"] = message["ruleUrl"].replace("13.231.223.137:3000", "grafana.drmkeyserver.com")
    message["ruleUrl"] = message["ruleUrl"].replace("&edit=true&tab=alert", "")
    text_msg = {
        "cards": [
            {
                "header": {
                    "title": message["title"],
                    "subtitle": message["ruleUrl"]
                },
                "sections": [
                    {
                        "header": "%s <%s|link>"%(message["ruleUrl"],message["ruleUrl"]),
                        "widgets": [
                            {
                                "image": {
                                    "imageUrl": "message["imageUrl"]"
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
    r = requests.post("https://chat.googleapis.com/v1/spaces/AAAAeJtZeRg/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jCu5LSqYHrGU8xtTV-NJKLyPTCGzUfFOnrzyjIctgO8%3D", data=json.dumps(text_msg), headers=headers)
    r = requests.post("https://chat.googleapis.com/v1/spaces/AAAAv60PSr0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=P_T2VrBXRuaRMDO9m_OksEdLlNADfQ23v1khca8mnGI%3D", data=json.dumps(text_msg), headers=headers)

    logging.info(r.text)

    return "200"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
