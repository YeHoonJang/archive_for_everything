package com.example.mynaverapp1.list

/*응답 데이터형식 예시*/
//{
//    "title": "[현장스케치] 정영채 NH투자증권 사장 &quot;손님에게 신뢰주는 회사 선택하라&quot;",
//    "originallink": "http://www.consumernews.co.kr/?mod=news&act=articleView&idxno=527223",
//    "link": "http://www.consumernews.co.kr/?mod=news&act=articleView&idxno=527223",
//    "description": "ⓒNH투자<b>증권정</b> 사장은 21일 오후에 열린 NH투자증권 채용간담회에서... ",
//    "pubDate": "Tue, 21 Aug 2018 15:46:00 +0900"
//},

/* News 데이터 클래스 선언 */
data class News(
    val title: String,
    val originalLink: String,
    val link: String,
    val description: String,
    val pubDate: String
)
