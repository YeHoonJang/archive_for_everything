package com.example.textview01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        textView.text = "Kotlin"

        var listener1 = BtnListener()
        button.setOnClickListener(listener1)

        var listener2 = BtnListener2()
        button2.setOnClickListener(listener2)
        button3.setOnClickListener(listener2)

        button4.setOnClickListener { v: View? ->
            textView.text = "4번째 버튼"
        }

        button5.setOnClickListener { v ->
            textView.text = "5번째 버튼"
        }

        var listener3 = View.OnClickListener { v: View? ->
            when(v?.id) {
                R.id.button6 -> textView.text = "6번째 버튼"
                R.id.button7 -> textView.text = "7번째 버튼"
        }
    }

        button6.setOnClickListener(listener3)
        button7.setOnClickListener(listener3)
}

    inner class BtnListener: View.OnClickListener {
        override fun onClick(v: View?) {
            textView.text = "버튼 클릭"
        }
    }

    inner class BtnListener2: View.OnClickListener {
        override fun onClick(v: View?) {
            when(v?.id) {
                R.id.button2 -> textView.text = "2번째 버튼"
                R.id.button3 -> textView.text = "3번째 버튼"
            }
        }
    }
}
