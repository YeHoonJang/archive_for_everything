package com.example.mobileprogramming2.lend_demand

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.app.AlertDialog
import android.view.LayoutInflater
import android.widget.Toast
import com.example.mobileprogramming2.R
import kotlinx.android.synthetic.main.activity_lend_list.*
import kotlinx.android.synthetic.main.start_page.view.*

class LendDemandActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lend_demand)

        var adapter = LendDemandAdapter(this)
        listView.adapter = adapter

        supportActionBar?.title = "대여요청"

        listView.setOnItemClickListener { parent, view, position, id ->
            demand()
        }
    }

    fun demand() {
        val cInflater = LayoutInflater.from(this).inflate(R.layout.lend_demand_page, null)

        val cBuilder = AlertDialog.Builder(this).setView(cInflater)

        val cAlertDialog = cBuilder.show()
        cInflater.button3.setOnClickListener{
            cAlertDialog.dismiss()

            Toast.makeText(applicationContext, "확인을 선택했습니다", Toast.LENGTH_LONG).show()

        }
        cInflater.button2.setOnClickListener{
            cAlertDialog.dismiss()

            Toast.makeText(applicationContext, "취소를 선택했습니다", Toast.LENGTH_LONG).show()
        }
    }
}
