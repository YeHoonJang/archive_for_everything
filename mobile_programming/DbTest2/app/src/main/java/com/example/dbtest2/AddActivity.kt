package com.example.dbtest2

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.dbtest2.model.Item
import com.example.dbtest2.model.ItemDB
import kotlinx.android.synthetic.main.activity_add.*

class AddActivity : AppCompatActivity() {

    private var itemDb : ItemDB? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add)

        itemDb = ItemDB.getInstance(this)

        val addRunnable = Runnable {
            val newItem = Item()
            newItem.itemName = addItem.text.toString()
            newItem.itemCount = addCount.text.toString().toInt()
            itemDb?.itemDao()?.insert(newItem)
        }

        addBtn.setOnClickListener {
            val addThread = Thread(addRunnable)
            addThread.start()

            val i = Intent(this, MainActivity::class.java)
            startActivity(i)
            finish()
        }
    }

    override fun onDestroy() {
        ItemDB.destroyInstance()
        super.onDestroy()
    }
}
