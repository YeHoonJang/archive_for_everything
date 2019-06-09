package com.example.mobileprogramming.list_reservation

import androidx.recyclerview.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.mobileprogramming.R
import kotlinx.android.synthetic.main.item_list_reservation.view.*
import java.lang.IllegalArgumentException

class RecyclerAdapter_reservation : RecyclerView.Adapter<RecyclerAdapter_reservation.ItemViewHolder>() {

    override fun getItemCount() = ItemDataReservation.values().size

    override fun getItemViewType(position: Int): Int {
        return ItemDataReservation.values()[position].itemType
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val view = when (viewType) {
            ITEM -> LayoutInflater.from(parent.context).inflate(
                R.layout.item_list_reservation, parent, false)
            else -> throw IllegalArgumentException(Error("매칭되는 뷰타입이 없습니다."))
        }
        return ItemViewHolder(view)
    }

    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        when (holder.itemViewType) {
            ITEM -> {
                holder.bindItem(ItemDataReservation.values()[position].itemContent)
            }
        }
    }

    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bindItem(itemContent: ItemContent2) {
            itemView.img_list_item_reservation.setImageResource(itemContent.imageId)
            itemView.text_list_item_name_reservation.text = itemContent.itemName
            itemView.text_list_amount_reservation.text = itemContent.itemAmount
        }
    }

    companion object {
        const val ITEM = 0
    }

}
