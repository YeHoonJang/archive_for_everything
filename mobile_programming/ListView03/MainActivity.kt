package kr.ac.gachon.ugkang.listview03

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //액션바 타이틀 설정
        supportActionBar?.title = "오늘의 운동"

        //어댑터 생성 및 리스트뷰에 어댑터 설정
        var adapter = WorkoutAdapter(this)
        listView.adapter = adapter
        //listView.adapter = PlayerAdapter(this)

        /* 리스트뷰의 아이템 클릭시 이벤트 처리를 위해 listView에 리스너 등록(람다식)
           - 리스트뷰에서 아이템을 클릭하면 토스트 메시지 출력
         */
        listView.setOnItemClickListener { parent, view, position, id ->
            //getItem()을 이용해 어댑터에서 사용자가 클릭한 현재 아이템을 가져옴
            var curItem = adapter.getItem(position)
            Toast.makeText(this, "${curItem.workName} 선택", Toast.LENGTH_LONG).show()
        }
    }
}
