package com.example.mynaverapp1.network

import okhttp3.HttpUrl
import okhttp3.OkHttpClient
import okhttp3.Request

/* object 키워드로 NetworkModule 객체를 생성(Singleton 구현)
  - 코틀린에서는 object를 이용하여 클래스를 정의함과 동시에 객체를 생성
  - 객체 이름을 통해 property나 메서드에 직접 접근 가능함
 */
object NetworkModule {
    /* OKhttp client (실제로 네트워크를 호출하는 부분) 생성 */
    val clinent: OkHttpClient by lazy {
        OkHttpClient.Builder().build()
    }

    /* App 등록시 발급받은 클라이언트 아이디 및 시크릿 값 */
    val clientId = "pSdUdOYZe4MoHnVROahp"
    val clientSecret = "9zitHbUbEF"

    /*String 검색어를 받아 Request를 리턴합니다. */
    fun getRequestFromQuery(query: String): Request {

        /* HttpUrl 객체 생성 */
        val httpUrl = makeHttpUrl(query)

        /* OkHttp Request 객체 생성 */
        val request = makeHttprequest(httpUrl)

        //Request 객체 반환
        return request
    }

    /* HttpUrl 객체 정의 함수 선언
       - HttpUrl.Builder()를 이용하여 HttpUrl 객체(URI 구조) 정의
    */
    fun makeHttpUrl(query: String): HttpUrl {
        //https://openapi.naver.com/v1/search/news.json&query=query
        return HttpUrl.Builder()
            .scheme("https")
            .host("openapi.naver.com")
            .addPathSegment("v1")
            .addPathSegment("search")
            .addPathSegment("news.json")
            .addQueryParameter("display", "10")//보여줄개수
            .addQueryParameter("start", "1")//시작위치
            .addQueryParameter("sort", "sim")//정렬기준
            .addQueryParameter("query", query)//
            .build()
    }

    /* OkHttp Request 생성 함수 선언
       - Request.Builder()를 사용하여 요청을 위한 Request 생성
       - header: Header 조립(설정)하는 부분
       - url: 요청서버 url + body
       - get/post: 전송방식
    */
    fun makeHttprequest(httpUrl: HttpUrl): Request {
        return Request.Builder()
            /* App 등록시 발급받은 클라이언트 아이디 값 */
            .header("X-Naver-Client-Id", clientId)
            /* App 등록시 발급받은 클라이언트 시크릿 값 */
            .header("X-Naver-Client-Secret", clientSecret)
            .url(httpUrl)
            .get().build();
    }
}