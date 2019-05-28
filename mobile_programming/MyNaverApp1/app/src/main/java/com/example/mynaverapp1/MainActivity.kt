package com.example.mynaverapp1

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import com.example.mynaverapp1.dialog.NewsSearchDialog
import com.example.mynaverapp1.list.News
import com.example.mynaverapp1.list.NewsAdpater
import com.example.mynaverapp1.network.NetworkModule
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    //나중에 초기화
    val newsAdapter by lazy {
        NewsAdpater(ArrayList())
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* - 뉴스 리사이클러뷰에 어댑터 및 레이아웃메니저 설정 */
        recycle_news.adapter = newsAdapter
        recycle_news.layoutManager = LinearLayoutManager(this)

        //fab 버튼을 클릭하면 NewsSearchDialog 프래그먼트 실행
        fab_search_news.setOnClickListener {
            NewsSearchDialog().show(supportFragmentManager, null)
        }
    }

    //todo1 - 사용자에게 쿼리할 데이터를 받습니다. - NewsSearchDialog
    //todo2 - 요청받은 데이터를 기반으로 HTTP/HTTPS 요청을 만듭니다. - loadNewsDataFromAPI에서부터 runBlocking 이전까지
    //todo3 - 코루틴을 통해서 백그라운드로 API를 호출합니다. - OkHttpClient를 통해 Naver 검색 서버에 검색 요청
    //todo4 - response로 받은 String(JSON구조)를 우리에게 필요한 data class(DAO)로 변환합니다. - mapppingStringToNews
    //todo5 - 변환한 DAO로 어댑터의 데이터를 Refresh하여 NewsList를 리사이클러뷰에 카드뷰 형태로 표시

    /* 뉴스정보를 쿼리하는 함수 선언
       - MainActivity에서 사용하지 않고 NewsSearchDialog에서 사용 */
    fun loadNewsDataFromAPI(query: String) {

        //newsList를 ArrayList로 생성
        var newsList: ArrayList<News>? = null

        /* HTTP reqeust 객체 생성
           - 입력한 검색 키워드(query)를 NetworkModule.getRequestFromQuery(query)를 통해
             reqeust 객체 생성
        */
        val request = NetworkModule.getRequestFromQuery(query)

        /* Coroutine을 이용하여 IO 스레드에서 서버에 검색 요청(ayns task를 사용)
           - Blocking 이하의 작업들은 IO 스레드에서만 작동(Main Thread에 영향을 주지 않음)
        */
        runBlocking(Dispatchers.IO) {

            /* OkHttpClient를 통해 Naver 검색 서버에 검색 요청
               - client(OKhttp)의 newCall을 통해서 실행시킴(요청)
               - runBlocking에서 Async와 wait을 만나면 async 블록안의 작업이 끝날때까지 기다립니다
             */
            val response = async { NetworkModule.clinent.newCall(request).execute() }.await()

            /* 서버로부터 요청에 대한 응답을 성공으로 받았으면 데이터를 작성*/
            if (response.isSuccessful) {
                /*  response의 body에서 응답(response) 정보를 String 테이터(JSON 포멧)로 추출 */
                val msgBody = response.body()?.string()!!
                Log.d("MSG", "msgBody: $msgBody")

                /* msgBody의 String 데이터를  ArrayList<News> 형태의 newsList(JSON 포멧) 생성 */
                newsList = mapppingStringToNews(msgBody)

                Log.d("MSG", "newsList: $newsList")
            } else {
                /* 성공하지 못한경우대한 에러 처리 */
            }
        }

        /* newsList가 있다면 맵핑시켜 리사이클러뷰  갱신
           - newsArray를 newsAdapter의 newsList에 맵핑하고,
           - notifyDataSetChanged() 메서드를 이용하여 리사이클러뷰를 갱신함
        */
        newsList?.let {
            newsAdapter.newsList = it
            newsAdapter.notifyDataSetChanged()
        }
    }

    /* 검색한 뉴스 String 데이터를 newsList(ArrayList<News>)로 반환
       - Moshi, Gson 라이브러리를 사용하면 좀더 간편하지만 구조를 이행하기 위해서 low하게 처리함
    */
    fun mapppingStringToNews(jsonBody: String): ArrayList<News> {

        //newsList 생성
        val newsList: ArrayList<News> = ArrayList()

        /* JSON형태의 데이터를 JSONObject로 변환한 후 Items를 가져와서 newsItemArray에 할당 */
        val newsItemArray = JSONObject(jsonBody).getJSONArray("items")

        /* newsItemArray를 Loop문을 사용하여 뉴스를 아이템(newsItem)별로 추출 */
        for (i in 0 until newsItemArray.length() - 1) {
            with((newsItemArray[i] as JSONObject)) {
                /*각 JSON마다 News 인스턴스를 만듭니다.*/
                News(
                    title = getString("title"),
                    originalLink = getString("originallink"),
                    link = getString("link"),
                    description = getString("description"),
                    pubDate = getString("description")
                ).run {
                    /* News 인스턴스를 만든 후 run으로 받아 newsList에 추가합니다.*/
                    newsList.add(this)
                }
            }
        }
        /* 생성한 newsList 반환 */
        return newsList
    }
}
