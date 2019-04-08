package com.example.listview02

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        supportActionBar?.title = "축구대표팀 선수명단"

        var adapter = PlayerAdapter(this)
        listView.adapter = adapter

        listView.setOnItemClickListener { parent, view, position, id ->
            var curItem = adapter.getItem(position)
            Toast.makeText(this, "${curItem.playName} 선택", Toast.LENGTH_LONG).show()
        }
    }
}
