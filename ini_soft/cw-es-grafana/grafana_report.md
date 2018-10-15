# Grafana - Monitoring Tool

## Version
- Docker: 18.6.1-ce
- Grafana: 5.2.4 (Docker Default)

## Grafana with Docker
### Docker Command
```bash
$ docker run -d -p 3000:3000 --name=grafana --restart=always \
  -e "GF_INSTALL_PLUGINS=grafana-piechart-panel" \
  -e "GF_INSTALL_PLUGINS=alexanderzobnin-zabbix-app"
  -e "GF_SMTP_ENABLED=true"\
  -e "GF_SMTP_HOST=smtp.test.com:25"\
  -e "GF_SMTP_FROM_ADDRESS=admin@grafana.localhost"\
  -e "GF_SMTP_USER=user_mail"\
  -e "GF_SMTP_PASSWORD=user_pw"\
  -e "GF_SMTP_SKIP_VERIFY=true"\
  --privileged grafana/grafana
```

### Run Grafana
- URI: [`localhost:3000`](http://localhost:3005)
- Admin Name: `admin`
- Admin Password: `admin`


## Grafana
### Data Source - CloudWatch
- Type: **CloudWatch**
- CloudWatch details
  * Auth Provider: **Access & secret key**  
  (Access key ID & Secret access key 는 AWS에서 부여 받은 Key 정보 입력)
  * Default Region: 모니터링 할 Instance가 있는 Region으로 선택  
  (Dash Board 그릴 때 다른 Region 선택 가능)
  * Custom Metrics: 사용자 지정 메트릭 이 **다시 봐!!!**
- `Save & Test` 버튼 누른 후 **Data source is working** 이라는 문구가 뜨면 연동 성공
- Access Key ID와 Secret Key만 입력하면 해당 계정으로 수집하는 데이터 모두 열람 및 사용 가능

### Data Source - Elasticsearch
- Type: **Elasticsearch**
- HTTP
  * URL: 모니터링 할 Elasticsearch URI 입력, 반드시 Port 번호 입력
- Elasticsearch details
  * Index name: 모니터링 할 index 입력
  * Pattern: index의 날짜 pattern에 맞게 선택
  * Time field name: 로그의 time field 입 (default는 \@timestamp)


### Dash Board 지원 기능
- 메트릭 자동 쿼리
  * region, namespace, metric, Demensions
  *
- 쿼리문 Duplicate

### 제한 사항
### 기타

## Elasticsearch - Grafana
#### 지원 기능
#### 제한 사항
#### 기타
