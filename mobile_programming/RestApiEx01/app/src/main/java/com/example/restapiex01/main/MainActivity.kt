package com.example.restapiex01.main

import android.app.DatePickerDialog
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*
import com.example.restapiex01.R
import com.example.restapiex01.database.DatabaseModule
import com.example.restapiex01.model.Fruits
import com.example.restapiex01.result.ResultActivity
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    /* 사용자가 공공DB에 요청시 사용할 과일 및 날짜 입력값을 null로 초기화
       - selectedFruit: 과일의 상수명(APPLE, PEAR, GRADPE, ...)
       - selectedDate:  날짜(YYYY-MM-DD)
    */
    var selectedFruit: String? = null
    var selectedDate: String? = null


    /* todo2 - 사용자가 클릭할때 분류(과일)를 선택하는 Dialog 설정
     - alertDialog를 사용하여 과일을 선택하는 Dialog 설정
     - AlertDialog에 setItems(컬렉션, 리스너)를 사용하면 SingleChoice Dialog를 만들 수 있음
     - setItems(CharSequence[] items, final OnClickListener listener)
   */
    /* -----------------------Alert Dialog------------------------*/
    /* 과일 선택을 위한 Dialog 설정입니다. */
    val alertDialog by lazy {

        /* Dialog의 builder 클래스를 초기화 */
        val builder = AlertDialog.Builder(this)
        /* builder에 Dialog 제목을 설정 */
        builder.setTitle("분류를 선택해주세요.")

        /* 분류 Dialog에서 과일을 선택하면, 해당 과일의 상수명을 반환하도록 builder 설정
            - map: 컬렉션 내 인자를 변환하여 반환
            - toTypedArray(): 컬렉션을 배열로 변환
            - OnClickListener를 통해 선택된 아이템의 index를 넘겨 받아, Fruits.values()[index]로
              선택한 과일의 상수명을 selectedFruit에 저장
        */
        builder.setItems(Fruits.values().map { it.holder }.toTypedArray()) { dialog, index ->
            /*  선택한 Enum의 키값(상수명)을 String 형태로 리턴해줍니다. */
            with(Fruits.values()[index]) {
                selectedFruit = this.name

                /* 선택한 과일명을 선택창에 표시 */
                text_type.text = this.holder
            }
            Log.i("FRESH", "which: $index - $selectedFruit")//0 - APPLE

            /* 검색버튼의 색상을 변경하는 함수 호출 */
            checkCondition()

            //changeInputTextBydate()
        }

        /* builder에 취소 버튼을 설정(이벤트는 Null로 설정) */
        builder.setNegativeButton("취소", null)

        /* 만든 builder를 리턴합니다. */
        builder.create() //return 되는 value
    }
    /* -----------------------Alert Dialog------------------------*/


    /* 데이터베이스를 가져옵니다.*/
    val database by lazy {
        /* DatabaseModule.getDatabase(싱글톤)를 이용하여 데이터베이스를 가져옵니다.*/
        DatabaseModule.getDatabase(this)
    }

    /* Main 화면을 위한 mainAdpater를 초기화합니다.*/
    val mainAdpater by lazy {
        /*emptyList()를 사용하여 MainAdapter를 빈값으로 초기화합니다.*/
        MainAdapter(emptyList())
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 리사이클러뷰의 구분선(Divider)를 만들어줍니다. */
        DividerItemDecoration(applicationContext, LinearLayoutManager(this).orientation).run {
            //리사이클러뷰(list_save)에 구분선(Divider) 추가
            list_save.addItemDecoration(this)
        }

        /* 리사이클러뷰에 어댑터 및 레이아웃메니저 설정 */
        list_save.adapter = mainAdpater
        list_save.layoutManager = LinearLayoutManager(this)


        /* todo1 - 사용자가 layout_type([분류를선택해주세요] 레이아웃)을 클릭한 경우 이벤트 처리
            - [분류를선택해주세요] 레이아웃을 클릭하면 과일을 선택하는 Dialog를 출력하는 alertDialog를 실행
        */
        layout_type.setOnClickListener { alertDialog.show() }


        //todo3 - 날짜 Dialog를 띄워줍니다.
        /*[날짜를선택해주세요] 레이아웃을 클릭했을경우 */
        layout_date.setOnClickListener {
            /*현재날짜를 가져옵니다.*/
            val currentCaldenar = Calendar.getInstance().apply { time = Date(System.currentTimeMillis()) }

            /* 날짜를 선택하는 다이얼로그를 만듭니다.*/
            DatePickerDialog(
                this, DatePickerDialog.OnDateSetListener { _, year, month, dayOfMonth ->
                    currentCaldenar.apply {
                        set(Calendar.YEAR, year)
                        set(Calendar.MONTH, month)
                        set(Calendar.DAY_OF_MONTH, dayOfMonth)
                    }.run {
                        /* 선택한 데이터를 2019-01-01와 같은 형식으로 가져옵니다.*/
                        selectedDate = SimpleDateFormat("yyyy-MM-dd").format(currentCaldenar.time)
                        /* 날짜 선택 여부를 체크하여 처리하기 위한 함수 호출
                           - 선택한 날짜를 선택창에 표시 */
                        changeInputTextBydate()
                    }
                },
                /* DatePickerDialog의 Date를 오늘 날짜로 초기화)*/
                currentCaldenar.get(Calendar.YEAR),
                currentCaldenar.get(Calendar.MONTH),
                currentCaldenar.get(Calendar.DAY_OF_MONTH)
            ).show()
        }

        /* todo4 - 사용자가 검색 버튼(btn_search)을 클릭했을경우 이벤트 처리 */
        btn_search.setOnClickListener {
            /* 분류와 날짜를 선택했는지 검증합니다.
               - selectedFruit: 과일의 상수명(APPLE, PEAR, GRADPE, ...)
               - selectedDate:  날짜(YYYY-MM-DD)
            */
            if (selectedDate == null || selectedFruit == null) {
                /* 선택이 안된 경우 에러메세지를 띄웁니다.*/
                Toast.makeText(this, "분류와 날짜를 입력해주세요.", Toast.LENGTH_LONG).show()
            } else {
                /* 정상적으로 선택했다면 데이터를 Intent에 담아 ResultActivity로 넘깁니다.*/
                startActivity(
                    Intent(this, ResultActivity::class.java)
                        .putExtra("selectedFruit", selectedFruit!!)
                        .putExtra("selectedDate", selectedDate)
                )
            }
        }
    }

    override fun onStart() {
        super.onStart()
        /* local DB에 저장된 데이터를 가져와서 메인화면의 리사이클러뷰를 갱신하는 loadSaveListFromDB() 함수 호출
           - 이전에 경락가격정보를 검색하여 local DB에 저장한 데이터를 가져와서 Main 화면에 표시
        */
        loadSaveListFromDB()
    }

    /* local DB에 저장한 데이터를 가져와서 메인화면의 리사이클러뷰를 갱신하는 함수 */
    private fun loadSaveListFromDB() {
        /* 어댑터(mainAdpater)의 데이터를 변경합니다.
           - freshDao().loadSaveItems() 쿼리 함수를 호출하여 DB에서 데이터를 가져옵니다.
        */
        mainAdpater.saveItems = database.freshDao().loadSaveItems()
        /*  notifyDataSetChanged() 메서드를 이용하여 리사이클러뷰를 갱신함 */
        mainAdpater.notifyDataSetChanged()
    }

    /* 날짜 선택 여부를 체크하여 선택한 날짜를 선택창에 표시하는 함수*/
    private fun changeInputTextBydate() {
        /* 분류와 날짜를 모두 선택하면 검색버튼의 색상을 변경하는 함수호출 */
        checkCondition()
        /*Date이 선택되었다면 날짜 선택창에 날짜 표시*/
        selectedDate?.let { txt_gongpan.text = it }
    }

    /* 분류와 날짜를 모두 선택하면 검색버튼과 글자의 색상을 변경하는 함수 */
    private fun checkCondition() {
        if (selectedDate != null && selectedFruit != null) {
            btn_search.setBackgroundColor(resources.getColor(android.R.color.holo_green_dark))
            btn_search.setTextColor(resources.getColor(android.R.color.white))
        }
    }
}
