package com.example.admin.lifecycleexam01


import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle

import android.util.Log

import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    val PREFS_FILENAME = "data"
    var username: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("LIFECYCLE", "MainActivity onCreate")

        btn_login.setOnClickListener {
            if (!edit_username.text.toString().isNullOrBlank()) {
                val myIntent = Intent(this, SecondActivity::class.java)

                //입력한 username 저장
                username = edit_username.text.toString()

                //인텐트에 username 저장
                myIntent.putExtra(USER_NAME, username)
                startActivity(myIntent)
            } else {
                Toast.makeText(this, "아이디를 입력하세요", Toast.LENGTH_LONG).show()
            }
        }
    }

    override fun onStart() {
        super.onStart()
        Log.d("LIFECYCLE", "MainActivity onStart")
    }

    override fun onPause() {
        super.onPause()
        Log.d("LIFECYCLE", "MainActivity onPause")
        setString(this, "username", username)
    }

    override fun onResume() {
        super.onResume()
        Log.d("LIFECYCLE", "MainActivity onResume")
        var t1 = getString(this, "username")
        Toast.makeText(this, "username : $t1", Toast.LENGTH_LONG).show()
    }

    override fun onStop() {
        super.onStop()
        Log.d("LIFECYCLE", "MainActivity onStop")
    }

    override fun onRestart() {
        super.onRestart()
        Log.d("LIFECYCLE", "MainActivity onRestart")
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d("LIFECYCLE", "MainActivity onDestory")
    }

    /* companion object 불럭({}) 안에 static 접근을 허용할 변수(프로퍼티)와 메서드(함수) 등을 선언
           - 코틀린에서는 static 키워드가 없음
           - Companion object 를 내에 선언한 변수와 메서드는 java 에서 사용하는 static 형태로 사용할 수 있음
           - Companion object 내에 선언된 변수와 메서드 접근 방법 : 클래스명.변수명(또는 메서드명)
    */
    companion object {
        const val USER_NAME = "USER_NAME"
    }

    //username을 SharedPreferences 파일로 저장
    fun setString(context : Context, key : String, value : String) {
        /* SharedPreferences 객체 참조
           - PREFS_FILENAME : file name
           - MODE_PRIVATE : 이 앱에서만 사용하도록 모드 설정
         */
        val prefs = context.getSharedPreferences(PREFS_FILENAME, Context.MODE_PRIVATE)
        //SharedPreferences Editor 객체 참조
        val editor = prefs!!.edit()
        /* 데이터 저장(key-vlaue 구조로 저장)
           - apply() : 비동기방식으로 백그라운드 스레드에서 SharedPreferences를 저장
           - commit() : : 메인 스레드에서 SharedPreferences를 저장
         */
        editor.putString(key, value).apply()
    }

    //SharedPreferences 파일에서 username을 읽어온다.
    fun getString(context : Context, key : String) : String {
        //SharedPreferences 객체 참조
        val prefs = context.getSharedPreferences(PREFS_FILENAME, Context.MODE_PRIVATE)
        //저장된 key값을 가져온다.
        return prefs.getString(key, "")
    }
}



