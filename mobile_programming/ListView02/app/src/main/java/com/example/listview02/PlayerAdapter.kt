package com.example.listview02

import android.content.Context
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView
import java.util.zip.Inflater

class PlayerAdapter(val context: Context) : BaseAdapter() {
    private val myInflater: LayoutInflater = LayoutInflater.from(context)

//    가장 중요!! ListView 에 몇명을 뿌릴건데 하는거
    override fun getCount(): Int {
        return PlayerData.values().size
    }

    override fun getItem(position: Int) = PlayerData.values()[position]

    override fun getItemId(position: Int) = position.toLong()

//  뿌린 데이터를 각각의 UI에 맞게 만들어 주는 애
    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        if(convertView != null) {
            Log.i("CONVERT-VIEW", "convertView is not null(convertView 사용), position: ${position.toString()}")
        }else{
            Log.i("CONVERT-VIEW", "convertView is null(아이템뷰 사용), position: ${position.toString()}")
        }

        val view = convertView ?: myInflater.inflate(R.layout.list_item_player, parent, false)

        view.findViewById<TextView>(R.id.playerName).text = getItem(position).playName
        view.findViewById<TextView>(R.id.birthYear).text = getItem(position).birthYear.toString()
        view.findViewById<TextView>(R.id.agency).text = getItem(position).agency

        return view

    }
}
