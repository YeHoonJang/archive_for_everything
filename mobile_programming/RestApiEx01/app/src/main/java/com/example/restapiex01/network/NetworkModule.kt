package com.example.restapiex01.network


import okhttp3.HttpUrl
import okhttp3.OkHttpClient
import okhttp3.Request

/* object 키워드로 NetworkModule 객체를 생성
   - 공공DB 서버에 요청할 OkHttp Request 객체 생성
 */
object NetworkModule {

    /* OKhttp client (실제로 네트워크를 호출하는 부분) 생성 */
    val clinent: OkHttpClient by lazy {
        OkHttpClient.Builder().build()
    }

    /* HttpUrl 객체 정의 함수 선언
       - HttpUrl.Builder()를 이용하여 HttpUrl 객체(URI 구조) 정의
       - 공공DB API 명세에 맞춰 선언
    */
    fun makeHttpUrl(mcode: String, date: String): HttpUrl {
        //http://openapi.epis.or.kr/openapi/service/PcInfoService/getFrmprdPrdlstPcList/query
        return HttpUrl.Builder()
            .scheme("http")
            .host("openapi.epis.or.kr")
            .addPathSegment("openapi")
            .addPathSegment("service")
            .addPathSegment("PcInfoService")
            .addPathSegment("getFrmprdPrdlstPcList")
            .addQueryParameter("dates", date.replace("-", "")) //-를 삭제 날짜
            .addQueryParameter("lcode", mcode.substring(0, 2))//대분류(06)
            .addQueryParameter("mcode", mcode)//중분류(0601)
            .addQueryParameter("_type", "json")//리턴타입
            .addQueryParameter(
                "serviceKey",
                "hlg9hNPuFREAlmQoI0NkQ6YnPryihmRpWngfslm6B3t0enqQ8uqt9PKZk7XvzmqnTIoH6GiSgfeA0JTltXXRwQ%3D%3D"
            )//서비스키
            .build()
    }

    /* OkHttp Request 생성 함수
       - Request.Builder()를 사용하여 요청을 위한 Request 생성
       - url: 요청서버 url
       - get/post: 전송방식
    */
    fun makeHttprequest(httpUrl: HttpUrl): Request {
        return Request.Builder()
            .url(httpUrl)
            .get().build();
    }
}