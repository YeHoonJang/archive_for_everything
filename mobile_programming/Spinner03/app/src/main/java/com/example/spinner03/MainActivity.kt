package com.example.spinner03

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    /* lazy: 읽기 전용 프로퍼티의 최기화 지연(val)
       - by lazy { ... }가 포함하는 코드는 정의된 프로퍼티가 사용되는 최초의 지점에서 초기화 과정을 실행
       - lazy는 프로퍼티의 값에 접근하는 최초 시점에 초기화를 수행하고,
         이 결과를 저장한 뒤 기록된 값을 재반환하는 인스턴스를 생성하는 함수
     */
    val recycleAdpater by lazy {
        SingerAdapter(singerDatas)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 리사이클러뷰에 어댑터 설정 */
        recycle_singer.adapter = recycleAdpater
        /* 리사이클러뷰에 레이아웃메니저 설정 */
        recycle_singer.layoutManager = LinearLayoutManager(this)


        /*스피너 어댑터 및 OnItemSelectedListener 리스너 설정
         - ArrayAdapter<String>(Context, Item-Layout, Data)
           1) Context: Context
           2) Item-Layout: 스피너의 Item 레이아웃(simple_list_item_1)
           3) Data: 스피너의 Item 데이터
              * Months.values().map { it.holder }: map() 메서드를 이용하여 Months 객체의 모든 상수값을 모아 배열로 반환
        */
        spinner.adapter = ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, Months.values().map { it.holder })
        spinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onNothingSelected(parent: AdapterView<*>?) { }

            /*스피너 아이템이 선택되었을 때 호출되는 메서드 */
            override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                //선택한 스피너 아이템의 position으로 Months 객체에서 해당 상수값을 가져와서 month에 저장
                val month = Months.values()[position]

                Log.d("MON", "month : ${month}")

                /* 전체를 선택 한경우 */
                if (month.name == "ALL") {
                    /* 모든 가수 정보를 할당 */
                    recycleAdpater.singerData = singerDatas
                } else {
                    /* 스피너 아이템에서 선택된 월에 해당하는 가수를 필터링하여 배열로 반환
                      - toTypedArray() : 배열로 변환
                    */
                    recycleAdpater.singerData = singerDatas.filter { it.featured == month }.toTypedArray()
                }

                /* 리사이클뷰 갱신 */
                recycleAdpater.notifyDataSetChanged()
            }
        }
    }
}
