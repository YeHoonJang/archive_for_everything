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

### Video Delete 및 Managing
#### Wordpress

- mysql update 됨
- server에는 crontab으로 매일 자정 비디오 삭제
- mysql에는 event scheduler 만들어서 한달에 한번씩 db 업데이트
