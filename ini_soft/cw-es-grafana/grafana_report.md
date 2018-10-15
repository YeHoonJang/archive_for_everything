## Grafana - Monitoring Tool

### Version
- Docker: 18.6.1-ce
- Grafana: 5.2.4 (Docker Default)

### Grafana with Docker
#### Docker Command
```bash
$ docker run -d -p 3000:3000 --name=grafana --restart=always \
  -e "GF_INSTALL_PLUGINS=grafana-piechart-panel" \
  -e "GF_SMTP_ENABLED=true"\
  -e "GF_SMTP_HOST=smtp.test.com:25"\
  -e "GF_SMTP_FROM_ADDRESS=admin@grafana.localhost"\
  -e "GF_SMTP_USER=user_name"\
  -e "GF_SMTP_PASSWORD=user_pw"\
  -e "GF_SMTP_SKIP_VERIFY=true"\
  --privileged grafana/grafana
```
#### Grafana
- URI: [`localhost:3000`](http://localhost:3005)
- Admin Name: `admin`
- Admin Password: `admin`

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
