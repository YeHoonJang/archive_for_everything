package com.example.whoami

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        fav_btn.setOnClickListener {
            val myIntent = Intent(this, FavoriteActivity::class.java)
            startActivity(myIntent)
        }
    }
}

