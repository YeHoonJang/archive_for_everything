package com.example.checkbox01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
         button.setOnClickListener {
             textView.text = ""

             if (checkBox.isChecked == true) {
                 textView.append("체크박스 1\n")
             }
             if (checkBox2.isChecked == true) {
                 textView.append("체크박스 2\n")
             }
             if (checkBox3.isChecked == true) {
                 textView.append("체크박스 3\n")
         }
        }
    }
}
