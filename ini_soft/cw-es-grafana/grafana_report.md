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
- URI: [`localhost:3000`](http://192.168.10.135:3005)
- Admin Name: `admin`
- Admin Password: `admin`


## CloudWatch - Grafana
### Data Source
- Type: CloudWatch
- Auth Provider: Access & secret key
  * Access key ID & Secret access key 는 AWS에서 부여 받은 Key 입력
-
#### 지원 기능
#### 제한 사항
#### 기타

### Elasticsearch - Grafana
#### 지원 기능
#### 제한 사항
#### 기타
