# Grafana - AWS

### Data Source
- Type: **CloudWatch**
- CloudWatch details
  * Auth Provider: **Access & secret key** (Access key ID & Secret access key 는 AWS에서 부여 받은 Key 정보 입력)
  * Default Region: 모니터링 할 Instance가 있는 Region으로 선택 (Dash Board 그릴 때 다른 Region 선택 가능)
- `Save & Test` 버튼 누른 후 **Data source is working** 이라는 문구가 뜨면 연동 성공

- <img src="https://i.imgur.com/nODsguQ.png?2"/>

### Grafana - AWS Dash Board
- Panel
  * Graph, Singlestat, Table, Heatmap, Alert List 등
  * Axes, Legend, Display, Alert, Time Range 설정
- Row 패널을 활용하여 Dash Board 내에 카테고리 생성 및 접기 가능
- Pie Chart로 Ratio 표현 가능
- Alert list
- Graph panel에서 여러 Data Source, 여러 지표 혼합 가능
  > **e.g.1.**  
  > CloudWatch version 1 과 version 2 에 있는 모든 EC2 instance에 대한 NetworkIn 정보 모두를 한 graph에 표시 가능
  > <img src="https://i.imgur.com/xzdq0mH.png"/>

  > **e.g.2.**  
  > 하나의 LoadBalancer에 대한 모든 지표(HTTPcode_Target_2XX, 3XX, 4XX, 5XX 등)를 하나의 graph에 표시 가능
  > <img src="https://i.imgur.com/WpVhG0K.png?1"/>


- Playlist를 통해 기존에 있던 여러 Dash Board를 묶어서 한번에 모니터링 가능

### 그 외 Dash Board 지원 기능
- Dash Board에 생성할 수 있는 Graph 개수 제한 없음 (Loading 및 Dash Board 설정을 바꿀 시 적용 시간이 김)
- Data Source에 대한 계정 정보만 입력하면 해당 계정으로 수집하는 데이터 모두 열람 및 사용 가능
- Snapshot 기능을 제공하여 Dash Board 백업 지원
- Dash Board Settings
  * Dash Board refresh time custom → 0.5초까지 확인
  * Monitoring time range custom → 1초까지 가능
  * Versions - Dash Board 저장 시점을 기록하여 버전 관리
  * Permissions - 사용자들에게 Admin, Editor, Viewer 역할을 부여하여 Dash Board 접근 권한 관리
  * JSON Model - 해당 Dash Board의 settings 관련 데이터는 json 형태로 제공

#### CloudWatch
- Data Source Type에 맞게 Metric 지표 자동 쿼리
  * region, namespace, metric, Demensions 순
  * 입력된 Access Key에 상응하는 계정의 CloudWatch가 리포팅 하는 모든 EC2/LoadBalancer의 지표를 사용자에게 모두 표시 → 사용자가 선택한 지표에 대하여 데이터가 없는 EC2/LoadBalancer의 InstanceID/LoadBalancerName는 표시하지 않음
    > **e.g.**  
    > CloudWatch Version2 EC2 Instance 중 License_W_1 인스턴스가 수집하지 않는 지표인 CPUCreditBalance 지표를 선택 후 InstanceID로 검색하면 License_W_1의 InstanceID(i-09182f05b3e2bf0d3)를 표시하지 않음
    > <img src="https://i.imgur.com/4ZofZ2f.png?2"/>

### 제한 사항
- 지표 list를 따로 보여주는 기능 없음
