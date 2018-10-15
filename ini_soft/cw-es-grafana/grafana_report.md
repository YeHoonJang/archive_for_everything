## Grafana - Monitoring Tool

### Version
- Docker: 18.6.1-ce
- Grafana: 5.2.4
 > **다른 버전의 Grafana를 설치 하려면...**  
 >  Docker에 있는 기본 grafana/grafana repository는 Grafana 버전이 5.2.4로 고정되어 있음  
 >  Docker Run Command 에서 버전 옵션을 수정할 수 있는 repository를 사용하여 Docker를 실행하면 Grafana 버전을 바꿀 수 있음

### Grafana with Docker
#### Docker Command
```bash
$ docker run -d -p 3000:3000 --name=grafana --restart=always \
-e "GF_INSTALL_PLUGINS=grafana-piechart-panel" \
-e "GF_SMTP_ENABLED=true"\
-e "GF_SMTP_HOST=smtp.test.com:25"\
-e "GF_SMTP_FROM_ADDRESS=admin@grafana.localhost"\
-e "GF_SMTP_USER="\
-e "GF_SMTP_PASSWORD="\
-e "GF_SMTP_SKIP_VERIFY=true"\
--privileged grafana/grafana

```

### Data Source
-

### CloudWatch - Grafana
#### 지원 기능
#### 제한 사항
#### 기타

### Elasticsearch - Grafana
#### 지원 기능
#### 제한 사항
#### 기타
