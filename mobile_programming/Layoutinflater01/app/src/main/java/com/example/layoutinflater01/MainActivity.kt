package com.example.layoutinflater01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.LayoutInflater
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.activity_sub.*
import kotlinx.android.synthetic.main.activity_sub.view.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* LayoutInflater 객체를 이용하여 부분화면(activity_sub)을 인플레이션
           - inflate(부분화면 layout, 메인화면에 선언된 부분화면을 넣을 뷰의 id )
         */
        LayoutInflater.from(this).inflate(R.layout.activity_sub, add_layout)
        //activity_sub 화면을 add_layout 부분에 넣으라는거

        //[방법-2]
        //val subView = LayoutInflater.from(this).inflate(R.layout.activity_sub, null)
        //add_layout.addView(subView)

        radioGroup.setOnCheckedChangeListener { group, checkedId ->
            when(checkedId) {
                R.id.radioButton1 ->
                    Toast.makeText(this, "여성입니다!!", Toast.LENGTH_LONG).show()
                R.id.radioButton2 ->
                    Toast.makeText(this, "남성입니다!!", Toast.LENGTH_LONG).show()
            }
        }

        checkBox1.setOnCheckedChangeListener { buttonView, isChecked ->
            if (isChecked == true) {
                Toast.makeText(this, "취미가 등산이군요!!", Toast.LENGTH_LONG).show()
            } else {
                Toast.makeText(this, "등산 체크박스 해제!!", Toast.LENGTH_LONG).show()
            }
        }

        checkBox2.setOnCheckedChangeListener { buttonView, isChecked ->
            if (isChecked == true) {
                Toast.makeText(this, "취미가 영화감상이군요!!", Toast.LENGTH_LONG).show()
            } else {
                Toast.makeText(this, "영화감상 체크박스 해제!!", Toast.LENGTH_LONG).show()
            }
        }

        checkBox3.setOnCheckedChangeListener { buttonView, isChecked ->
            if (isChecked == true) {
                Toast.makeText(this, "취미가 운동이군요!!", Toast.LENGTH_LONG).show()
            } else {
                Toast.makeText(this, "운동 체크박스 해제!!", Toast.LENGTH_LONG).show()
            }
        }
    }
}
