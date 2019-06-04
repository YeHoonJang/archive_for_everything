package com.example.mobileprogramming.list_reservation

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.LinearLayoutManager
import com.example.mobileprogramming.R
import com.example.mobileprogramming.list_rent.MainActivity
import kotlinx.android.synthetic.main.activity_main2.*


class Main2Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        supportActionBar?.title = "해당학과"

        recycle_item_reservation.adapter = RecyclerAdapter_reservation()

        recycle_item_reservation.layoutManager = LinearLayoutManager(this)

        button_main2_rent.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }
}
