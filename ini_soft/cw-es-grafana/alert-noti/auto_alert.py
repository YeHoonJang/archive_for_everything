from flask import Flask,request, Response
import json
import logging
import requests
import datetime
import time

app = Flask(__name__)
CORS(app)
logging.basicConfig(
#   format='%(asctime)s [%(levelname)s] %(message)s',
    format='{access_key:,key_id:,%(message)s}',
    filename='/var/log/webapi.log',
    level=logging.INFO
)


@app.route("/api/webhook/hangouts",methods=["POST","PUT","GET"])
def webhook():
    logging.info(request.get_data())
    message = json.loads(request.get_data())
    #{"evalMatches":[],"message":"Test Message","ruleId":8,"ruleName":"ELB Status Error 400 alert","ruleUrl":"http://13.231.223.137:3000/d/4dgCpYbmz/ls-monit-v1-0?fullscreen=true\u0026edit=true\u0026tab=alert\u0026panelId=8\u0026orgId=1","state":"alerting","title":"[Alerting] ELB Status Error 400 alert"}
    message["ruleUrl"] = message["ruleUrl"].replace("13.231.223.137:3000", "grafana.drmkeyserver.com")
    message["ruleUrl"] = message["ruleUrl"].replace("&edit=true&tab=alert", "")

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

    request_png_url = "%s/render/d-solo/%s/%s?%sto=%d&from=%d&width=1000&height=500&tz=Asia\Seoul"%(url,url_list[4],page,parm_str,timestamp*1000,(timestamp-259200)*1000)
    request_png_url = request_png_url.replace("\\","%2F")
    logging.info(request_png_url)
    png_name = "%s-%s.png"%(url_list[4], panel_id)
    logging.info(png_name)
    r = requests.get(request_png_url, headers=header)
    with open("/usr/share/nginx/html/%s"%png_name,"wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    message["imageUrl"] = "https://license-eval.drmkeyserver.com/%s"%(png_name)
    logging.info("get_png")
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

    try:
        if message["region"] == "EU":
            webhook = "https://chat.googleapis.com/v1/spaces/AAAAm90Stuc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=zeimA1cPeF0a-Ku6-Y7Vdjt7dGEpX2gZHoDQjdUJsYo%3D"
        elif message["region"] == "JP":
            webhook = "https://chat.googleapis.com/v1/spaces/AAAAOLPngcw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=Y32E1vBflP8hLXVQlKZPHXop_i8B3nrjBUQZD19FqTM%3D"
    except:
        webhook = "https://chat.googleapis.com/v1/spaces/AAAAsvqxoN0/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=NQCRsRlBKslcRfZn-5n4M1EYsNs7ApQoL9LCvIPpS4M%3D"

    r = requests.post(webhook, data=json.dumps(text_msg), headers=headers)

    logging.info(r.text)
    return "200"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
