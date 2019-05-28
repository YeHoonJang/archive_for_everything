package com.example.restapiex01.result

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.list_item_fresh.view.*
import com.example.restapiex01.R
import com.example.restapiex01.model.FreshData

/* ResultActivity에서 리사이클러뷰에 데이터를 보여주는 어댑터 */
class ResultAdapter(var newsList: ArrayList<FreshData>) : RecyclerView.Adapter<ResultAdapter.ItemViewHolder>() {

    /* 뷰홀더를 생성하여 반환 */
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val rootView = LayoutInflater.from(parent.context).inflate(R.layout.list_item_fresh, parent, false)
        return ItemViewHolder(rootView)
    }

    //뷰홀더에 데이터 바인딩(bindItems() 함수를 호출)
    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        holder.bindItems(newsList[position])
    }

    //어댑터에서 관리할 아이템 갯수를 반환
    override fun getItemCount() = newsList.size

    //뷰홀더 클래스 선언
    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        // 검색한 경락가격정보를 아이템뷰에 바인딩하는 함수
        fun bindItems(fresh: FreshData) {
            itemView.txt_gongpan_info.text = fresh.gongpanName
            itemView.txt_unit.text = fresh.grade
            itemView.txt_min_price.text = "최저: " + String.format("%,d", fresh.minPrice)
            itemView.txt_avg_price.text = "수량: " + String.format("%,d", fresh.tradeAmt)
            itemView.txt_max_price.text = "최고: " + String.format("%,d", fresh.maxPrice)
        }
    }
}
