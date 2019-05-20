package com.example.coroutinetest01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* Activity 최초 생성시 MainListFragment() add
           - add(containerViewId, fragment, tag);
         */
        if (savedInstanceState == null) {
            supportFragmentManager.beginTransaction()
                .add(R.id.fragmentContainer, MainListFragment(), MainListFragment.TAG)
                .commit()
        }
    }

    // 뒤로가기 버튼("<-") 버튼 처리 메서드
    override fun onBackPressed() {
        if (!supportFragmentManager.popBackStackImmediate()) super.onBackPressed()
    }
}
