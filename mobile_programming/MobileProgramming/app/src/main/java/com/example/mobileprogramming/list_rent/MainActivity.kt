package com.example.mobileprogramming.list_rent

import android.content.Intent
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import com.example.mobileprogramming.list_reservation.Main2Activity
import com.example.mobileprogramming.R
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        supportActionBar?.title = "해당학과" // 안뜸

        var adapter = ListviewAdapterRent(this)
        list_item_rent.adapter = adapter

        button_main_reservation.setOnClickListener {
            val intent = Intent(this, Main2Activity::class.java)
            startActivity(intent)
        }



        /*
        list_item_rent.setOnItemClickListener { parent, view, position, id ->
            // getItem()을 이용해 어댑터에서 사용자가 클릭한 현재 아이템을 가져옴
            var curItem = adapter.getItem(position)
            Toast.makeText(this, "${curItem.itemName}선택", Toast.LENGTH_LONG).show()
            // 대여버튼을 누른 아이템의 대여화면이 보여지도록 DB설정
            /*


             */
            val intent = Intent(this,RentActivity::class.java)
            startActivity(intent)
        }
        */
    }

}

