package com.example.mobileprogramming

import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class RentActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_rent)

        supportActionBar?.title = "해당학과"
    }
}