package com.example.mobileprogramming.list_rent

import android.content.Intent
import android.os.Bundle
import android.support.design.widget.NavigationView
import android.support.design.widget.Snackbar
import android.support.v4.app.Fragment
import android.support.v4.app.FragmentManager
import android.support.v4.app.FragmentStatePagerAdapter
import android.support.v4.view.GravityCompat
import android.support.v7.app.ActionBarDrawerToggle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import com.example.mobileprogramming.R
import com.example.mobileprogramming.delay_list.DelayListActivity
import com.example.mobileprogramming.lend_list.LendListActivity
import com.example.mobileprogramming.reservation_list.ReservationListActivity
import com.example.mobileprogramming.reservation_list.ReservationListAdapter
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.app_bar_main.*
import kotlinx.android.synthetic.main.content_main.*

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    // 탭 제목으로 사용할 문자열
    val tabTitles = arrayOf("대여", "예약")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        supportActionBar?.title = "해당학과" // 안뜸

        /*
        listView.setOnItemClickListener { parent, view, position, id ->
            // curItem : 내가 클릭한 아이템의 인덱스 값
            // 디비로 연결하여 원하는 값이 출력되도록 설정할 것
            var curItem = adapter.getItem(position)
            Toast.makeText(this, "${curItem.itemName} 선택", Toast.LENGTH_LONG).show()

            var intent = Intent(this, RentActivity::class.java)
            startActivity(intent)
        }
        */

        /*
        //fab에 클릭이벤트 리스너 등록
        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()
        }
        */

        //네비게이션바의 토글버튼 생성(드로어 열고 닫기)
        val toggle = ActionBarDrawerToggle(
            this, drawer_layout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close
        )

        // 토글버튼을 DrawerLayout에 추가
        drawer_layout.addDrawerListener(toggle)
        //토글버튼(햄버거 아이콘) sync 맞추기
        toggle.syncState()

        //레이아웃에 선언된 네비게이션뷰(nav_view)에 선택 리스너를 설정
        nav_view.setNavigationItemSelectedListener(this)

        // 탭 레이아웃에 탭 추가
        //tabLayout.addT
        tabLayout.addTab(tabLayout.newTab())
        tabLayout.addTab(tabLayout.newTab())
        tabLayout.addTab(tabLayout.newTab())

        // 탭 레이아웃을 ViewPager 와 연동. 터치 스와이프시 탭이동이 됨.
        tabLayout.setupWithViewPager(viewPager)

        // ViewPager 의 어댑터를 MyPagerAdapger 로 설정
        viewPager.adapter = MyPagerAdapter(supportFragmentManager)
    }

    //사용자가 뒤로가기 버튼("<-")을 클릭하면 호출되는 메서드
    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    // 네비게이션뷰의 메뉴 아이템을 클릭했을 떄 처리를 위한 리스너 설정
    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.
        when (item.itemId) {
            R.id.lend_list -> {
                Toast.makeText(this, "대여내역 선택", Toast.LENGTH_SHORT).show()
                val intent = Intent(this, LendListActivity::class.java)
                startActivity(intent)
            }
            R.id.reservation_list -> {
                Toast.makeText(this, "예약내역 선택", Toast.LENGTH_SHORT).show()

                val intent2 = Intent(this, ReservationListActivity::class.java)
                startActivity(intent2)
            }
            R.id.delay_list -> {
                Toast.makeText(this, "연체일 수 선택", Toast.LENGTH_SHORT).show()

                val intent3 = Intent(this, DelayListActivity::class.java)
                startActivity(intent3)
            }

        }

        //네비게이션뷰(drawer_layout)를 close
        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }

    // ViewPager 의 어댑터 class 선언
    inner class MyPagerAdapter(fragmentManager: FragmentManager): FragmentStatePagerAdapter(fragmentManager) {

        override fun getCount(): Int {
            return tabTitles.size
        }

        //ViewPager 의 각 포지션에서 그려야할 Fragment 를 반환
        override fun getItem(p0: Int): Fragment {
            // 프래그먼트에서는 newInstance() 메소드를 통해서 필요한 파라미터를 전달

            when (p0) {
                0 -> return RentFragment.newInstance("대여화면")
                1 -> return ReservationFragment.newInstance("예약화면")
                else -> return RentFragment.newInstance("")

            }
        }

        // 각 페이지의 타이틀 반환
        override fun getPageTitle(position: Int): CharSequence? {
            Log.d("LOG", "getPageTitle:"+position)
            return tabTitles[position]
        }
    }

}

