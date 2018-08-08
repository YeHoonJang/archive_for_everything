# INI Intern First Project - Wordpress & PHP
**장예훈 (Video Delete)
18.07.02 Mon - 18.07.17 Tue**

### 개발 환경
- Ubuntu 16.04.5 LTS
- Wordpress
- Apache 2
- MySQL 5.7.23
- PHP 7.1
- Anaconda 4.3.11

### 개발 서버 구축
팀원들이 맡은 각 기능을 구현 후 통합하고, 프로젝트의 전반적인 요구사항 이행을 위한 환경이 요구됨에 따라 각 기능들의 개발 환경 버전 이슈가 발생하지 않도록 개발 서버를 구축하였음

**개발 서버 환경**
- Ubuntu 16.04.5 LTS
- Wordpress
- Apache 2
- MySQL 5.7.23
- PHP 7.1

### 비디오 삭제 및 비디오 파일 관리
#### 비디오 삭제
##### 1. 프로세스
- 사용자가 비디오 리스트 화면에서 `delete` 버튼을 누르면 페이지에 내장된 php 코드가 서버의 `update_video_status.php` 파일을 호출
- `update_video_status.php` 파일에서는 MySQL wordpress db에 접속하여 wp-uploaded_video 테이블에서 삭제요청 받은 비디오의 status를 `delete`로 변경
- db 업데이트가 정상적으로 완료되면 다시 비디오 리스트 화면을 띄움  

##### 2. 실행 결과
- `delete` 버튼 누르기 전 비디오 리스트 화면
<img src="https://i.imgur.com/rJI8Iea.png"/>
- `delete` 버튼 누른 후 비디오 리스트 화면
<img src="https://i.imgur.com/KdjTyRy.png"/>
- `update_video_status.php` 호출 전 MySQL wp-uploaded_video 테이블
<img src="https://i.imgur.com/IYqgzN9.png"/>
- `update_video_status.php` 호출 후 MySQL wp-uploaded_video 테이블
<img src="https://i.imgur.com/ax9Mgqi.png"/>

#### 비디오 파일 관리
##### 1. 프로세스
- 서비스 관리 차원에서 wordpress에서 `delete` 버튼을 누른 즉시 서버와 DB에서 비디오 관련 정보를 삭제하지 않음
- 삭제된 비디오의 모든 정보를 저장하고 있으면 서버 메모리 이슈가 발생하기 때문에 서버 관리자 측의 별도 관리 프로세스가 필요함
- db에서는 event scheduler를 등록하여 한 달에 한 번 비디오의 status가 'delete' 인 데이터들을 삭제
- 서버에서는 매일 자정 실행되는 crontab을 이용하여 db 내에 status가 'delete' 인 비디오 파일을 삭제

##### 2. 실행 결과
- MySQL에 등록된 event scheduler
<img src="https://i.imgur.com/67Y9EEm.png"/>
- 서버에 등록된 crontab
```bash
 * 0 * * * sh /var/www/html/delete_video_from_server.sh
```
- crontab이 실행되기 전
<img src="https://i.imgur.com/Wb5Hbir.png"/>
- crontab이 실행된 후
<img src="https://i.imgur.com/4enTPuO.png"/>
