package com.example.mobileprogramming.reservation_list

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.example.mobileprogramming.R
import com.example.mobileprogramming.delay_list.DelayListAdapter
import kotlinx.android.synthetic.main.activity_lend_list.*

class ReservationListActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_reservation_list)

        var adapter = ReservationListAdapter(this)
        listView.adapter = adapter

        supportActionBar?.title = "예약내역"
    }
}
