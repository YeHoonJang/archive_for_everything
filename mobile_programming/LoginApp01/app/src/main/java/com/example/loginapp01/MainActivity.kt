package com.example.loginapp01

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btn_login.setOnClickListener {
            if (!edit_username.text.toString().isNullOrBlank()) {
                val myIntent = Intent(this, SecondActivity::class.java)
                myIntent.putExtra(USER_NAME, edit_username.text.toString())
                startActivity(myIntent)
            } else {
                Toast.makeText(this, "아이디를 입력해주세요", Toast.LENGTH_LONG).show()
            }
        }
    }

    companion object {
        const val USER_NAME = "USER_NAME"
    }
}
