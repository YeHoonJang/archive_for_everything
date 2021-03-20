import requests
import json

js_url = "http://localhost:5000/es-test"
es_url = "https://search-inisoft-elasticsearch-cterqbonqj5n4xgnplulvs4upq.ap-northeast-1.es.amazonaws.com/license-log2*/_search"


headers = {"Content-Type":"application/json"}
es_res = requests.get(es_url).json()
es_data = es_res["hits"]["hits"]

js_res = requests.get(js_url).json()
id = len(js_res) + 1

for i in range(len(es_data)):
    data = es_data[i]
    data["id"] = id
    data = json.dumps(data)
    print(i, ":", data, "\n")
    requests.post(js_url, data, headers=headers)
    id += 1

#
# data = {"id":3, "evalMatches":[],"message":"Test Message","ruleId":8,"ruleName":"ELB Status Error 400 alert","ruleUrl":"http://13.231.223.137:3000/d/4dgCpYbmz/ls-monit-v1-0?fullscreen=true\u0026edit=true\u0026tab=alert\u0026panelId=8\u0026orgId=1","state":"alerting","title":"[Alerting] ELB Status Error 400 alert"}
#
# data = json.dumps(data)
# print(data)
#
#
# res = requests.post(url, data=data, headers=headers)
