package com.example.mobileprogramming

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.ViewParent
import kotlinx.android.synthetic.main.item_list.view.*
import java.lang.IllegalArgumentException

// 어댑터 클래스 선언
// 어댑터 클래스를 선언하고, 그 안에 뷰홀더 클래스를 선언
// 리사이클러뷰의 어댑터는 RecyclerView.Adapter를 상속하고, <>에 선언된 뷰홀더 클래스를 넣어야 함
class RecyclerAdapter: RecyclerView.Adapter<RecyclerAdapter.ItemViewHolder>() {

    // 어댑터에서 관리하는 아이템의 개수를 반환(한번 호출)
    override fun getItemCount() = ItemData.values().size

    // 현재 아이템뷰의 position에 해당하는 뷰타입 반환
    override fun getItemViewType(position: Int): Int {
        return ItemData.values()[position].itemType
    }

    // 뷰홀더를 생성하여 반환(인플레이트)
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val view = when (viewType) {
            ITEM -> LayoutInflater.from(parent.context).inflate(R.layout.item_list, parent, false)
            else -> throw IllegalArgumentException(Error("매칭되는 뷰타입이 없습니다."))
        }
        return ItemViewHolder(view)
    }

    // 뷰홀더에 데이터를 바인딩
    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        when (holder.itemViewType) {
            ITEM -> {
                holder.bindItem(ItemData.values()[position].itemContent as ItemContent)
            }
        }
    }

    // 뷰홀더 클래스 선언
    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bindItem(itemContent: ItemContent) {
            itemView.img_umbrella.setImageResource(itemContent.imageId)
            itemView.text_item_name.text = itemContent.itemName
            itemView.text_amount.text = itemContent.itemAmount
        }
    }

    companion object {
        val ITEM = 0
    }
}