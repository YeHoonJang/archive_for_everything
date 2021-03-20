<h3> 1. 프로젝트 개요

- 프로젝트 기간
<br> 2018.07.24 ~ 2018.08.02

- 개발 환경
  - OS : ubutu 16.04
  - python==3.6.5 , MySQL==5.7 , Flask==1.0.2 , PyMySQL==0.9.2 , redis-server==4.0.10

- 목적
   <Br> 컨텐츠에 대한 접근 수가 증가하면 서버에 대한 트래픽 양 또한 증가하여 용량이 더 큰 서버로의 컨텐츠 재배치가 요구됨
  이를 실시간으로 수행하기 위하여 메모리 기반의 realtime database 인 redis 와 파이썬의 asyncio 를 이용한 비동기 파일 재배치 프로그램을 제작

- 기대효과
   <Br> 트래픽 용량에 따른 컨텐츠 재배치가 자동으로 이루어져 서버의 부하를 실시간으로 조절하고 여러 개의 워커가 비동기적으로 작동하여 큰 용량의 파일이 이동할 때에도 병목 현상이 일어나지 않도록 함

<br>


-  Data Flow Diagram
<center><img src="https://i.imgur.com/vIeEdW1.png" width="60%" /></center>


- Flow chart
<center><img src="https://i.imgur.com/Yr4qzaf.png" width="35%" /></center>

<hr>
###  2. API 구현 정보

##### 컨텐츠 정보 쿼리 및 redis 업데이트(Flow chart. 2)
1. 사용자가 컨텐츠를 조회하면 컨텐츠의 cid 와 count 정보를 포함하여 API를 호출 (e.g.curl http://192.168.10.108:5001/post_sentence -d "cid=3&count=664"
)
2. db_que  ry 모듈을 이용하여 database의 contents table 과 level table에서 post 된 cid를 가진 content의 현재위치와 목적위치를 반환 <br>

| <small>contents | <small>level |
|---------|----------------|
|<img src="https://i.imgur.com/L8I5vfa.png" width="110%" />  |   <img src="https://i.imgur.com/OArMB1b.png " width="110%" />    |

3. cid를 key 값으로 현재 위치와 counts에 따른 목적 위치가 다른 경우 status 에 'update' 라는 문자열을, 현재위치와 목적 위치가 같은 경우 status에 'done' 이라는 문자열을 삽입하여 redis database에 json 형식으로 set
  (worker_id 는 이 후 단계에서 할당되기 때문에 null값으로 초기화)
<br>(e.g.)
{'3':{"cid": "3", "count": "664", "target": "bronze", "db_level": "silver", "filename": "c.mp4", "worker_id": null, "status": "update"}} 형식으로 저장
<br>

```bash
# 컨텐츠 정보 쿼리 및 redis 업데이트 example
foo@bar:~/$ curl http://192.168.10.108:5000/post_sentence -d "cid=7&count=1964"
{"cid": "7", "count": "1964", "target": "silver", "db_level": "bronze", "filename":
"g.mp4", "worker_id": null, "status": "update"}
```
<br>

##### redis 값 체크 및 MySQL database 업데이트(Flow chart. 7)
1. worker가 파일을 재배치한 후 해당 contents 의 status 를 'done' 으로 바꾸고 API 를 호출 (e.g. curl http://192.168.10.108:5000/update_sentence -d "cid=3"
)
2. request를 받으면 cid 를 key 값으로 redis에서 해당 content의 status 가 'done' 인지 검사하고 MySQL의 contents table 에 새로운 level 과 update time 을 업데이트
만약 status 가 'done' 이 아니면 "check your status again" 메세지를 반환

```bash
# redis 값 체크 및 MySQL database 업데이트 example
# db update 후 해당 content 의 cid 반환
foo@bar:~/$ curl http://192.168.10.108:5000/update_sentence -d "cid=7"
7
foo@bar:~/$ curl http://192.168.10.108:5000/update_sentence -d "cid=8"
check your status again
```    
database 에서 cid 7 의 content_level과 update_time 업데이트 <br>
<img src="https://i.imgur.com/4EiSSFO.png" width="50%" />
<hr>
### 4. 프로젝트 후기

##### 느낀점
 remote server에서 이용되는 library나 module의 가용성을 계속 체크해야해서 local 에서 개발할 때보다 더 많은 시간이 소요되었고 권한 문제나 보안상의 이유로 파일의 설정 또한 로컬에서 단독으로 개발 할 때보다 복잡했음 혼자서 기능을 구현하는 것과 실무에서 이용할 수 있는 코드를 만드는 것은 또 다른 문제라는 것을 알게됨
이번 프로젝트에서 예외 케이스 처리나 scalability 같은 완성도는 아쉽지만 redis-server 을 다뤄보고 협업이 이루어졌다는 점에서 유익한 프로젝트였다고 생각함
