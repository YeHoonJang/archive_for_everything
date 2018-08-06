# **DB process**
## DB Class - process 내에서 필요한 db sql class 생성
### 1. select
: 본 프로젝트의 API와 DB 간 데이터 상호 교환 시 **반복 사용되는 MySQL select query 문을 모듈화 한 것** 으로 인자는 `table`, `column`, `where_clause`, `order_by`가 있다. `table`과 `column`은 필수 인자이다.  
### 2. insert_contents
: 본 프로젝트에서 콘텐츠가 새로 업로드 될 때 **콘텐츠에 대한 정보를 MySQL contents table에 insert 해주는 기능을 모듈화 한 것** 이다. min_count가 0인 level이 default `level`이 된다. `generate time`은 insert query의 실행 시점이 적용되므로 본 함수는 콘텐츠가 업로드 됨과 동시에 실행되어야 한다.
### 3. update_level
: 콘텐츠의 view count가 계속 올라가서 특정 레벨로 relocate 되고 api server가 본 함수를 호출하면 **MySQL contents table에서 content_level을 update 하는 query문을 모듈화 한 것** 이다. update 하고자 하는 콘텐츠의 `cid`와 relocate 된 `contet_level`이 필수 인자이다. 본 함수가 실행되면 contents table에서 content_level과 update_time column이 update 된다.

## DB trigger
  - contents table이 update되면  trigger가 작동되고 update_history에 기록됨
