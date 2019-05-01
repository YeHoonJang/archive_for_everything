package com.example.bottomnavigation02

import android.content.Intent
import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.v7.app.AppCompatActivity
import android.view.LayoutInflater
import kotlinx.android.synthetic.main.activity_main.*
import com.example.bottomnavigation02.lotto.ConstellationActivity
import com.example.bottomnavigation02.lotto.LottoNumberMaker
import com.example.bottomnavigation02.lotto.NameActivity
import com.example.bottomnavigation02.lotto.ResultActivity

class MainActivity : AppCompatActivity() {

    /*  BottomNavigationView.OnNavigationItemSelectedListener 인터페이스를 구현 */
    private val mOnNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        /* 사용자가 BottomNavigationView의 메뉴 아이템을 클릭했을 때 처리할 코드 작성 */
        when (item.itemId) {
            R.id.navigation_random -> {
                // ResultActivity를 시작하는 Intent 생성
                val intent = Intent(this, ResultActivity::class.java)
                /*  intent에 생성된 로또번호(ArrayList type)를  "result" key로 저장
                    - 리스트를 전달하므로 putIntegerArrayListExtra 를 사용
                */
                intent.putIntegerArrayListExtra("result", ArrayList(LottoNumberMaker.getShuffleLottoNumbers()))
                // startActivity 로 실행
                startActivity(intent)
            }
            R.id.navigation_constellation -> {
                // ConstellationActivity를 시작하는 Intent 를 만들고 startActivity 로 실행
                startActivity(Intent(this, ConstellationActivity::class.java))
            }
            R.id.navigation_name -> {
                // NameActivity를 시작하는 Intent 를 만들고 startActivity 로 실행
                startActivity(Intent(this, NameActivity::class.java))
            }
        }
        /* 버튼이 클릭된 후 다른 버튼으로 active 시키려면 true , 버튼 누른 효과를 주지 않으려면 false를 준다.*/
        false
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 시작화면을 표시하는 레이아웃 파일(activity_start.xml)을 인플레이션하여
           프레임레이아웃(frame_main in activity_main.xml)에 추가(addView)
        */
        //=============================================================
        LayoutInflater.from(this).inflate(R.layout.activity_start, frame_main)
        //=============================================================

        /* BottomNavigationView(id:navigation)에 선택 리스너를 설정 */
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener)
    }
}
