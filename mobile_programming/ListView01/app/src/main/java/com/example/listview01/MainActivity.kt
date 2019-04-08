package com.example.listview01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    var data = arrayOf("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var adaptor = ArrayAdapter(this, android.R.layout.simple_list_item_1, data)

        listView.adapter = adaptor

//        var listener = Listener()
//        listView.setOnItemClickListener(listener)

//      람다식으로 표현
        listView.setOnItemClickListener { parent, view, position, id ->
            textView.text = data[position]
            Toast.makeText(this, "${data[position]} 선택", Toast.LENGTH_LONG).show()
        }
    }
        inner class Listener: AdapterView.OnItemClickListener{
            override fun onItemClick(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
                textView.text = data[position]
                Toast.makeText(this@MainActivity, "${data[position]} 선택", Toast.LENGTH_LONG).show()
            }
        }
    }
