package com.example.mobileprogramming2.modify

import android.content.Context
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView
import android.widget.TextView
import com.example.mobileprogramming2.R

class ModifyAdapter(val context: Context): BaseAdapter() {
    private val mInflater: LayoutInflater = LayoutInflater.from(context)

    override fun getCount(): Int {
        return ModifyData.values().size
    }

    override fun getItem(position: Int) = ModifyData.values() [position]

    override fun getItemId(position: Int) = position.toLong()

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        if(convertView != null) {
            Log.i("CONVERT-VIEW", "convertView is not null(convertView 사용), position: ${position.toString()}")
        } else {
            Log.i("CONVERT-VIEW", "convertView is null(아이템 생성), position: ${position.toString()}")
        }

        val view = convertView ?: mInflater.inflate(R.layout.item_list_main, parent, false)

        view.findViewById<ImageView>(R.id.img_list_item).setImageResource(getItem(position).imageId)
        view.findViewById<TextView>(R.id.text_list_item_name).text = getItem(position).itemName
        view.findViewById<TextView>(R.id.text_list_amount).text = getItem(position).itemAmount

        return view
    }
}