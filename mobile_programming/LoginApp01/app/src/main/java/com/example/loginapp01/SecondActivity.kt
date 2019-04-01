package com.example.loginapp01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_second.*

class SecondActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        intent.getStringExtra(MainActivity.USER_NAME).run {
            text_msg.text = this + "님!!"
        }

        btn_finish.setOnClickListener {
            finish()
        }
    }
}
