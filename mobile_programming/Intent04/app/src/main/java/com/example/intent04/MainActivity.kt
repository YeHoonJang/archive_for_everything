package com.example.intent04

import android.content.Intent
import android.net.Uri
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        call_btn.setOnClickListener {
            val intent = Intent(Intent.ACTION_DIAL)

            intent.data = Uri.parse("tel: " + phone_no.text.toString())

            if (intent.resolveActivity((packageManager) != null)) {
                startActivity(intent)
            }
        }
    }
}
