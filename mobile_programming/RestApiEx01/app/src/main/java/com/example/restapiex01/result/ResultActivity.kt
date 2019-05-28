package com.example.restapiex01.result

import android.os.Bundle
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NavUtils
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_result.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import com.example.restapiex01.R
import com.example.restapiex01.database.DatabaseModule
import com.example.restapiex01.model.FreshData
import com.example.restapiex01.model.Fruits
import com.example.restapiex01.model.SaveItem
import com.example.restapiex01.network.NetworkModule
import org.json.JSONObject

/* 공공DB 서버에 검색 요청 및 검색 결과를 처리하는 ResultActivity */
class ResultActivity : AppCompatActivity() {
    /* 데이터베이스를 가져옵니다.*/
    val database by lazy {
        DatabaseModule.getDatabase(this)
    }
    /* Result 화면을 위한 resultAdpater를 초기화합니다.*/
    val resultAdpater by lazy {
        ResultAdapter(ArrayList())
    }

    /* Result 화면의 actionBarTitle 위한 intent 생성
       - 날짜 + 과일명
    */
    val actionBarTitle by lazy {
        intent.getStringExtra("selectedDate") +
                " " +
                /* selectFruits의경우 APPLE, GRAPE와 같은 String으로 받기때문에
                   Enum Data로의 변환을 위해 valueof를 사용합니다. */
                Fruits.valueOf(intent.getStringExtra("selectedFruit")).holder
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        /* ActionBar에 뒤로가기("<-") 버튼 표시 설정
           - ActionBar에 표시만 되고 뒤로가기 액션은 이뤄지지 않음.
             따라서 onOptionsItemSelected 콜백 메서드에서 뒤로가기 로직을 구현해야 함
        */
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        //todo5 네트워크 call을 수행 - 서버에 검색 요청
        loadDataFromURL()

        /* Actionbar의 타이틀을 변경합니다. */
        supportActionBar?.title = actionBarTitle

        /*  리사이클러뷰에 구분선 설정 */
        recycle_reesult.addItemDecoration(DividerItemDecoration(this, DividerItemDecoration.VERTICAL));
        /* 리사이클러뷰에 어댑터 및 레이아웃메니저 설정 */
        recycle_reesult.adapter = resultAdpater
        recycle_reesult.layoutManager = LinearLayoutManager(this)
    }

    /* actionbar에 save버튼을 만들어줍니다. */
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_remote_result_save_actionbar, menu)
        return true
    }


    /* Actionbar에서 저장 아이템을 클릭하면 검색한 경락가격정보를 DB에 저장하는 콜백함수
       - item에 들어오는 id값으로 어떤 버튼을 클릭했는지 분기처리합니다.
       - SaveItem 테이블과 Fresh 테이블에 경락가격정보 저장
       - 1:M구조
    */
    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        //클릭한 아이템이 저장 아이템(save_list)이면
        if (item?.itemId == R.id.save_list) {

            /* SaveItem 테이블과 Fresh 테이블에 경락가격정보 저장
              - database Dao를 형태로 가져옵니다.
              - 먼저 저장 항목리스트를 만들어서 autoGenerated된 ID값을 받은다음,
              - freshdata(각각의 개별 데이터)를 리스트 ID값과 함께 저장해줍니다.
            */
            database.freshDao().insertSave(
                SaveItem(id = null, saveTitle = actionBarTitle)
            ).run {
                //리턴값으로 데이터를 받아 Fresh 테이블에 경락가격정보 저장
                resultAdpater.newsList.let { datas ->
                    datas.forEach { it.saveId = this }
                    database.freshDao().insertFresh(datas)
                }
            }
            Toast.makeText(this, "데이터가 저장되었습니다.", Toast.LENGTH_LONG).show()
        }

        // ActionBar 뒤로가기 로직을 구현
        when (item?.groupId){
            android.R.id.home -> {
                NavUtils.navigateUpFromSameTask(this)
            }
            else -> {
                return super.onOptionsItemSelected(item)
            }
        }
        return true
    }

    /* 경락정보를 쿼리하는 함수 선언
        - 과일 중분류 코드와 날짜를 가지고 서버에 요청하는 함수
    */
    fun loadDataFromURL() {
        /* Blocking 이하의 작업들은 IO쓰레드에서만 작동합니다.*/
        /* 따라서 Main Thread에 영향을 받지 않는 작업을 합니다.*/

        /* OkHttp Reques 객체를 생성하는 함수를 호출하여 HttpUrl 객체 생성 */
        val httpUrl = NetworkModule.makeHttprequest(
            NetworkModule.makeHttpUrl(
                /* 서버에 요청을 위해 인텐트에서 중분류코드와 날짜를 추출하여 변수에 저장 */
                mcode = intent.getStringExtra("selectedFruit").run { Fruits.valueOf(this).mcode },
                date = intent.getStringExtra("selectedDate")
            )
        )

        /* Coroutine을 이용하여 IO 스레드에서 서버에 요청(ayns task를 사용)
          - Blocking 이하의 작업들은 IO 스레드에서만 작동(Main Thread에 영향을 주지 않음)
        */
        runBlocking(Dispatchers.IO) {
            try {
                /* runBlocking에서 async와 awit을 만나면 async 블록안의 작업이 끝날때까지 기다립니다.*/
                val response = async { NetworkModule.clinent.newCall(httpUrl).execute() }.await()
                /* response의 body에서 응답(response) 정보를 String 테이터(JSON 포멧)로 추출 */
                with(response.body()?.string()) {

                    /* 서버로부터 요청에 대한 응답을 성공으로 받았으면 데이터를 작성*/
                    if (response.isSuccessful && !this.isNullOrBlank()) {
                        /* JSON으로 맵핑한 경락정보를 resultAdpater의 freshList에 전달 */
                        resultAdpater.newsList = mappongToData(this)
                        //notifyDataSetChanged() 메서드를 이용하여 리사이클러뷰를 갱신함
                        resultAdpater.notifyDataSetChanged()
                    }
                }
            } catch (e: Error) {
                Log.i("", e.message)
            }

        }
    }

    //todo6 - 서버에서 응답한 경락정보를  JSON Object로 맵핑합니다.
    fun mappongToData(jsonBody: String): ArrayList<FreshData> {
        //freshList 생성
        val freshList: ArrayList<FreshData> = ArrayList()

        Log.i("FRESH", "jsonBody: $jsonBody")

        /* jsonBody: {"response":{"header":{"resultCode":"00","resultMsg":"NORMAL SERVICE."},
           "body":{"items":{"item":
           [{"avgprice":16796,"coname":"강서청과","dates":"2019\/05\/10","gradename":"없음",
           "marketname":"서울강서도매","maxprice":19000,"mclassname":"사과",
           "minprice":12000,"rnum":1,"sclassname":"후지","sumamt":108,"unitname":"10kg"},{},{},...]
       */

        /* JSON Object 생성(응답한 경락정보의 item 배열값을 추출)
           - freshItemArray: [{"avgprice":16796,"coname":"강서청과","dates":"2019\/05\/10",
                              "gradename":"없음","marketname":"서울강서도매","maxprice":19000,
                              "mclassname":"사과","minprice":12000,"rnum":1,"sclassname":"후지",
                              "sumamt":108,"unitname":"10kg"},{},{},{}...]
        */

        try {
            val freshItemArray = JSONObject(jsonBody)
                .getJSONObject("response")
                .getJSONObject("body")
                .getJSONObject("items")
                .getJSONArray("item")

            //결과가 없으면
            if (freshItemArray.length() == 0) {
                return ArrayList()
            }

            /* 검색한 경락가격정보를 리사이클러뷰에 표시하기 위한 각 아이템을 만든다.
               - JSON Object에서는 Array의 Length만 알 수 있어 한개씩 데이터를 빼는 방법으로 진행합니다.
             */
            for (i in 0 until freshItemArray.length() - 1) {
                with((freshItemArray[i] as JSONObject)) {
                    /*각 JSON마다 News 인스턴스를 만듭니다.*/
                    FreshData(
                        grade = getString("gradename"),//등급
                        date = getString("dates"),//날짜
                        gongpanName = getString("coname") + " " + getString("marketname"),//도매법인+도매시장
                        maxPrice = getInt("maxprice"),//최고가
                        minPrice = getInt("minprice"),//최저가
                        tradeAmt = getInt("sumamt")//거래량
                    ).run {
                        /* FreshData 인스턴스를 만든 후 run으로 받아 freshList에 추가합니다.*/
                        freshList.add(this)
                    }
                }
            }
        } catch (e: Exception) {  }
        //freshList 반환
        return freshList
    }
}
