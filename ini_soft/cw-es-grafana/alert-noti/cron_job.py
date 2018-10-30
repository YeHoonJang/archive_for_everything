import requests
import json

data = {"evalMatches":[],"message":"Test Message","ruleId":8,"ruleName":"ELB Status Error 400 alert","ruleUrl":"http://13.231.223.137:3000/d/4dgCpYbmz/ls-monit-v1-0?fullscreen=true\u0026edit=true\u0026tab=alert\u0026panelId=8\u0026orgId=1","state":"alerting","title":"[Alerting] ELB Status Error 400 alert"}

data = json.dumps(data)
print(data)
print("type:", type(data))

url1 = 'http://localhost:5005/api/webhook/hangouts'
# url2 = 'http://localhost:5000'

# data = {'param1': 'value1', 'param2': 'value'}
res = requests.post(url1, data=data)
# res = requests.post(url2, data=data)
