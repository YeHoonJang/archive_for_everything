package com.example.mobileprogramming

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        supportActionBar?.title = "해당학과" // 안뜸

        recycle_item.adapter = RecyclerAdapter()

        recycle_item.layoutManager = LinearLayoutManager(this)
    }
}
