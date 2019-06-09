package com.example.dbtest

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.dbtest.model.Item

class ItemAdaptor(val context: Context, val items: List<Item>) : RecyclerView.Adapter<ItemAdaptor.ItemViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemAdaptor.ItemViewHolder {
        val view = LayoutInflater.from(context).inflate(R.layout.item_list, parent, false)
        return ItemViewHolder(view)
    }

    override fun getItemCount(): Int {
        return items.size
    }

    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        holder.bindItems(items[position])
    }

    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val name = itemView?.findViewById<TextView>(R.id.itemName)
        val counts = itemView?.findViewById<TextView>(R.id.itemCount)

        fun bindItems(item: Item) {
            name?.text = item.itemName
            counts?.text = item.itemCount.toString()
        }
    }
}
