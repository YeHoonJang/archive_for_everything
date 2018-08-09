# INI Intern First Project - Wordpress & PHP
**장예훈 (Video Delete)
18.07.02 Mon - 18.07.17 Tue**
## 프로젝트 개요
### 1. 목적
### 2. DFD

**************************************

##  개발 서버 구축
- 팀원들이 맡은 각 기능을 구현 후 통합하고, 프로젝트의 요구사항 전체를 이행하기 위한 환경이 요구됨
- 각 기능들의 구현 환경과 개발 서버 환경의 버전 이슈를 방지하기 위해 개발 환경에 대한 컨벤션 설계

**개발 서버 환경**
- Ubuntu 16.04.5 LTS
- Wordpress
- Apache 2
- MySQL 5.7.23
- PHP 7.1
- API Star 0.5.40

> #### Issue of 개발 서버 구축
> **우분투 버전 이슈**
> 1. Issue 정의
>  -  처음 개발 서버에 AMP(Apache-MySQL-PHP) 설치 시 configuration 설정이 적용되지 않거나 명령어가 실행하지 않는 이슈 발생
>  - 여러 번의 에러 해결 시도 후 우분투가 18.04 버전인 것을 확인
>  - 우분투 18.04 버전에서 지원되지 않는 라이브러리 또는 패키지 내 모듈이 다소 존재
>  - 우분투에서는 버전 downgrade를 지원하지 않음
> 2. Issue 해결 방안
>  - 프로젝트 참여자들의 우분투 버전과 동일한 우분투 server 16.04.5 LTS 설치

## 비디오 삭제 및 비디오 파일 관리 프로세스
### 1. 개발 환경
- Ubuntu 16.04.5 LTS
- Wordpress
- Apache 2
- MySQL 5.7.23
- PHP 7.1
- Anaconda 4.3.11
- API Statr 0.5.40

### Wordpress 설치 및 세팅
#### 1. LAMP 설치
> #### Issue of 2.
> **Wordpress를 지원하는 AMP 버전이 정해져 있음**
> 1. Issue 정의
>  - 초반에 AMP를 모두 설치하고 Wordpress를 설치하려고 할 때 에러가 나거나 configuration이 적용되지 않음
>  - Wordpress를 지원 AMP 버전이 정해져 있음
> 2. Issue 해결 방안
>  - Wordpress를 지원하는 AMP 버전 확인 후 설치

#### 2. Wordpress 설치 및 세팅
##### 2.1. Wordpress 설치
##### 2.2. PlugIn 설치
Wordpress 환경에서 각 기능과 요구사항을 구현하기 위한 각종 플러그인 설치

- **SnapTube**
 - 프로젝트 진행 시 결과물이 실행 될 wordpress theme
 - SnapTube 화면
   <img src="https://i.imgur.com/nSKaHdb.png"/>

- **PHP code snippets(Insert PHP)**
 - 워드프레스 페이지 내에서 동작 할 PHP 코드 삽입을 위한 플러그인
 - `<? php ?>` 태그 대신 `[inset_php][/insert_php]` 태그 안에 php 코드를 내장

> #### Issue of 2.2. PHP code snippets(Insert PHP)
> **Wordpress 페이지 내 PHP 코드 삽입에 관련한 이슈**
> 1. Issue 정의
>  - Wordpress 페이지 내 PHP 코드를 삽입하여 서버와 연동하는 것이 요구됨
>  - Wordpress templates 디렉터리에 템플릿 파일을 추가 후 PHP 코드를 작성하는 방법이 존재하였으나, 해당 템플릿 파일에 SnapTube 테마가 적용되지 않아 해당 방법을 적용 불가
>  - Wordpress 페이지 내 숏코드로 PHP 코드를 삽입하였으나 Wordpress에서 PHP 언어를 숏코드 지원하지 않음
> 2. Issue 해결 방안
>  - Wordpress 페이지에 PHP 코드를 숏코드로 삽입 가능한 플러그인 설치
>  - `[insert_php] [/insert_php]` 태그 내에 있는 PHP 코드가 숏코드로 페이지 내에서 동작 가능

- **WP Mail SMTP**
  - Wordpress에서 회원 가입 시 가입 확인 메일을 보내기 위한 플러그인
  - 사용자 별 비디오 관리가 프로젝트의 목적이기 때문에 회원 가입을 통해 user를 생성해야 함


### 비디오 삭제 및 비디오 파일 관리
#### 1. 비디오 삭제
<img src="https://i.imgur.com/k7exUSo.png"/>

##### 1.1. 사용자 - 삭제 요청
- 사용자가 비디오 리스트 화면에서 `delete` 버튼을 누르면 링크된 경로로 routing
- routing 정보

|  Method  |  URI  |  Code  |  Description  |
|---|---|---|---|
|  GET  |  http://localhost/update_video_status.php?video_id=$video_id  |  200  |  localhost 서버에 있는 update_video_status.php 파일을 호출<br/>delete 하는 video_id를 전달  |

##### 1.2. Wordpress - 서버의 php 파일 호출
- `update_video_status.php` 파일에서는 MySQL wordpress db에 접속하여 wp-uploaded_video 테이블에서 삭제 요청 받은 비디오의 status를 `delete`로 변경
- db 업데이트가 정상적으로 완료되면 다시 비디오 리스트 화면을 띄움  

##### 1.2. 실행 결과
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
