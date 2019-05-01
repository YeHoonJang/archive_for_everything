package com.example.bottomnavigation04

import android.os.Bundle
import android.support.design.widget.BottomNavigationView
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*
import com.example.bottomnavigation04.lotto.*


class MainActivity : AppCompatActivity() {

    /*  BottomNavigationView.OnNavigationItemSelectedListener 인터페이스를 구현 */
    private val mOnNavigationItemSelectedListener = BottomNavigationView.OnNavigationItemSelectedListener { item ->
        /* 사용자가 BottomNavigationView의 메뉴 아이템을 클릭했을 때 처리할 코드 작성 */
        when (item.itemId) {
            R.id.navigation_main -> {
                /* Fragment를 교체하기 위해선 supportFragmentManger에서 트랜잭션을 시작한 후 replace 시켜야함. */
                supportFragmentManager.beginTransaction().replace(R.id.frame_main, RandomFragment()).commit()
            }
            R.id.navigation_contellation -> {
                supportFragmentManager.beginTransaction().replace(R.id.frame_main, ConstellationFragment()).commit()
            }
            R.id.navigation_name -> {
                supportFragmentManager.beginTransaction().replace(R.id.frame_main, NameFragment()).commit()
            }
        }
        false
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //BottomNavigationView(navigation)에 선택 리스너를 설정
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener)

        /* 기본 화면 설정해주기*/
        /* 아래 코드가 없다면 액티비티 최초 실행시 (메뉴 누르기 전까지) 아무런 화면도 보이지 않습니다.*/
        supportFragmentManager.beginTransaction().replace(R.id.frame_main, StartFragment()).commit()
    }

    /* 각 프레그먼트에서 생성한 로또번호를 bundle로 받아 ResultFragment로 FrameLayout(id:frame_main)을 갱신 */
    fun moveToResultFragment(bundle: Bundle) {
        //인자로 받은 bundle객체를 ResultFragment의 arguments 프로퍼티에 할당
        val resultFragment = ResultFragment().apply {
            arguments = bundle
        }
        //resultFragment로 FrameLayout(id:frame_main)을 갱신
        supportFragmentManager.beginTransaction().add(R.id.frame_main, resultFragment, "resultFragment").commit()
    }

    //사용자가 뒤로가기 버튼("<-")을 클릭하면 호출되는 메서드
    override fun onBackPressed() {
        //
        var resultFragment = supportFragmentManager.findFragmentByTag("resultFragment")
        if (resultFragment != null) {
            supportFragmentManager.beginTransaction().remove(resultFragment).commit()
        } else {
            super.onBackPressed()
        }
    }
}
