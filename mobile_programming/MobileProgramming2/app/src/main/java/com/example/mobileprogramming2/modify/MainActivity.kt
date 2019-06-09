package com.example.mobileprogramming2.modify

import android.content.Intent
import android.os.Bundle
import android.support.design.widget.NavigationView
import android.support.design.widget.Snackbar
import android.support.v4.view.GravityCompat
import android.support.v7.app.ActionBarDrawerToggle
import android.support.v7.app.AlertDialog
import android.support.v7.app.AppCompatActivity
import android.view.LayoutInflater
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import com.example.mobileprogramming2.R
import com.example.mobileprogramming2.add.AddActivity
import com.example.mobileprogramming2.lend_demand.LendDemandActivity
import com.example.mobileprogramming2.lend_list.LendListActivity
import kotlinx.android.synthetic.main.activity_nav.*
import kotlinx.android.synthetic.main.app_bar_nav.*
import kotlinx.android.synthetic.main.start_page.view.*

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_nav)
        setSupportActionBar(toolbar)

        supportActionBar?.title = "해당학과"

        var adapter = ModifyAdapter(this)
        listView.adapter = adapter

        listView.setOnItemClickListener { parent, view, position, id ->
            var curItem = adapter.getItem(position)
            Toast.makeText(this, "${curItem.itemName} 선택", Toast.LENGTH_LONG).show()

            modify()
        }

        imageButton.setOnClickListener {
            var intent = Intent(this, AddActivity::class.java)
            startActivity(intent)
        }

        val toggle = ActionBarDrawerToggle(
            this, drawer_layout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close
        )
        drawer_layout.addDrawerListener(toggle)
        toggle.syncState()

        nav_view.setNavigationItemSelectedListener(this)
    }

    fun modify() {
        val cInflater = LayoutInflater.from(this).inflate(R.layout.start_page, null)

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


    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.
        when (item.itemId) {
            R.id.lend_demand -> {
                Toast.makeText(this, "대여요청 선택 ", Toast.LENGTH_SHORT).show()

                var intent = Intent(this, LendDemandActivity::class.java)
                startActivity(intent)
            }
            R.id.lend_list -> {
                Toast.makeText(this, "대여목록 선택 ", Toast.LENGTH_SHORT).show()

                var intent2 = Intent(this, LendListActivity::class.java)
                startActivity(intent2)
            }
        }

        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }
}
