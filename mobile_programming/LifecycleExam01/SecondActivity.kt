package com.example.admin.lifecycleexam01

import android.content.Context
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.AttributeSet
import android.util.Log
import android.view.View
import kotlinx.android.synthetic.main.activity_second.*

class SecondActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        Log.d("LIFECYCLE","SecondActivity onCreate")

        /* MainActivity에서 보낸 인텐트에서 USER_NAME 추출 */
        intent.getStringExtra(MainActivity.USER_NAME).run {
            text_msg.text = this + "님!!"
        }

        /* 뒤로가기를 누르면 앱을 종료합니다.*/
        btn_finish.setOnClickListener {
            finish()
        }
    }

    override fun onStart() {
        super.onStart()
        Log.d("LIFECYCLE", "SecondActivity onStart")
    }

    override fun onPause() {
        super.onPause()
        Log.d("LIFECYCLE", "SecondActivity onPause")
    }

    override fun onResume() {
        super.onResume()
        Log.d("LIFECYCLE", "SecondActivity onResume")
    }

    override fun onStop() {
        super.onStop()
        Log.d("LIFECYCLE", "SecondActivity onStop")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("LIFECYCLE", "SecondActivity onRestart")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("LIFECYCLE", "SecondActivity onDestroy")
    }
}
