package com.example.navigationdrawer01


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
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.app_bar_main.*
import kotlinx.android.synthetic.main.content_main.*

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {
    // 탭 제목으로 사용할 문자열
    val tabTitles = arrayOf("홈", "도서", "설정")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        //fab에 클릭이벤트 리스너 등록
        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()
        }

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

    // 옵션 Menu 생성 메서드
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.main, menu)
        return true
    }

    // 옵션 Menu의 item 선택시 처리 메서드
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId)  {
            R.id.action_settings ->
                Toast.makeText(this, "Settings 선택 ", Toast.LENGTH_SHORT).show()
            else -> return super.onOptionsItemSelected(item)
        }
        return true
    }

    // 네비게이션뷰의 메뉴 아이템을 클릭했을 떄 처리를 위한 리스너 설정
    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.
        when (item.itemId) {
            R.id.nav_camera -> {
                Toast.makeText(this, "Import 선택 ", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_gallery -> {
                Toast.makeText(this, "Gallery 선택 ", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_slideshow -> {
                Toast.makeText(this, "slideshow 선택 ", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_manage -> {
                Toast.makeText(this, "Tools 선택 ", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_share -> {
                Toast.makeText(this, "Share 선택 ", Toast.LENGTH_SHORT).show()
            }
            R.id.nav_send -> {
                Toast.makeText(this, "Send 선택 ", Toast.LENGTH_SHORT).show()
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
                0 -> return TabFragment.newInstance("홈화면")
                1 -> return TabFragment.newInstance("도서화면")
                2 -> return TabFragment.newInstance("설정화면")
                else -> return TabFragment.newInstance("")
            }
        }

        // 각 페이지의 타이틀 반환
        override fun getPageTitle(position: Int): CharSequence? {
            Log.d("LOG", "getPageTitle:"+position)
            return tabTitles[position]
        }
    }
}
