package com.example.dbtest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.dbtest2.model.Item
import com.example.dbtest2.model.ItemDB
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    private var itemDb : ItemDB? = null
    private  var itemList = listOf<Item>()
    lateinit var mAdapter : ItemAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        itemDb = ItemDB.getInstance(this)
        mAdapter = ItemAdapter(this, itemList)

        val r = Runnable {
            itemList = itemDb?.itemDao()?.getAll()!!
            mAdapter = ItemAdapter(this, itemList)
            mAdapter.notifyDataSetChanged()

            mRecyclerView.adapter = mAdapter
            mRecyclerView.layoutManager = LinearLayoutManager(this)
            mRecyclerView.setHasFixedSize(true)
        }

        val thread = Thread(r)
        thread.start()

        mAddBtn.setOnClickListener {
            val i = Intent(this, AddActivity::class.java)
            startActivity(i)
            finish()
        }
    }

    override fun onDestroy() {
        ItemDB.destroyInstance()
        itemDb = null
        super.onDestroy()
    }
}
