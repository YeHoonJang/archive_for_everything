package kr.ac.gachon.ugkang.viewpager02

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.design.widget.TabLayout
import android.support.v4.view.ViewPager
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* 뷰페이저에 어댑터 설정 */
        viewpager_main.adapter = WisePagerAdapter()

        /* 뷰페이저 항목(아이템)이 변경되었을때 이벤트를 처리하도록 리스너 등록  */
        viewpager_main.addOnPageChangeListener(object : ViewPager.OnPageChangeListener {
            /* 스크롤 상태가 변경되었을때 */
            override fun onPageScrollStateChanged(p0: Int) {}

            /* 스크롤이 끝나 화면에 나타났을 때 */
            override fun onPageScrolled(position: Int, positionOffset: Float, positionOffsetPixels: Int) {
                Toast.makeText(this@MainActivity, "${position}번째 뷰가 화면에 표시되었음.", Toast.LENGTH_LONG).show()
            }

            /* 페이지뷰가 선택되었을떄*/
            override fun onPageSelected(position: Int) {
                //페이지뷰가 선택되었을 때 배경색을 변경
                viewpager_main.setBackgroundColor(resources.getColor(WiseSayingData.values()[position].colorId))
            }
        })

        /* 뷰페이저 백그라운드 색상의 기본값을 첫번째 상수의 컬러 데이터로 설정*/
        viewpager_main.setBackgroundColor(resources.getColor(WiseSayingData.values().first().colorId))

        /* tablayout과 viewpager가 서로 연동하도록 리스너 등록*/
        viewpager_main.addOnPageChangeListener(TabLayout.TabLayoutOnPageChangeListener(tablayout_main))
        tablayout_main.addOnTabSelectedListener(TabLayout.ViewPagerOnTabSelectedListener(viewpager_main))

        /* tablayout_main에 Tab menu 설정
           - WiseSayingData의 크기많큼 반복문을 실행하여 "writer"로 Tab menu 설정
        */
        WiseSayingData.values().forEach {
            //newTab() 메서드를 이용하여 tab-item 생성
            val newTab = tablayout_main.newTab();
            newTab.text = it.writer//writer로 Tab menu 설정
            //탭 레이아웃(tablayout_main)에 tab-item 추가(add)
            tablayout_main.addTab(newTab)
        }
    }
}
