package com.example.spinner03

import android.app.Activity
import android.content.Intent
import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.list_item_singer.view.*
import com.example.spinner03.DetailActivity.Companion.SINGER_IDX

class SingerAdapter(var singerData: Array<SingerData>) : RecyclerView.Adapter<SingerAdapter.ItemViewHolder>() {
    //어댑터에서 관리하는 아이템의 개수를 반환(최초에 한번 호출)
    override fun getItemCount() = singerData.size

    // 뷰홀더(ItemViewHolder)를 생성하여 반환(뷰홀더가 새로 만들어지는 시점에만 호출)
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val adapterView = LayoutInflater.from(parent.context).inflate(R.layout.list_item_singer, parent, false)
        return ItemViewHolder(adapterView)
    }

    //뷰홀더에 데이터를 바인딩
    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        holder.bindSingerData(singerData[position])
    }

    /* 뷰홀더(ItemViewHolder) 클래스 선언
       - itemView : 리사이클러뷰에 List로 출력될 아이템뷰(뷰객체)
   */
    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        //아이템뷰(list_item_singer 레이아웃)에 SingerData 데이터 바인딩
        fun bindSingerData(singerData: SingerData) {
            itemView.txt_item_singer.text = singerData.singer
            itemView.txt_item_song.text = singerData.song
            itemView.txt_item_photo.setImageResource(singerData.imgRes)

            //리사이클러뷰의 itemView를 클릭하면 상세보기 화면 생성(DetailActivity)
            itemView.setOnClickListener {

                /* 전체 데이터에(배열)서 선택한 아이템(singerData)을 찾아 인덱스값을 반환
                   - indexOf(요소): 배열에서 지정된 요소를 찾아 그 요소의 인덱스값을 반환
                */
                val idx = singerDatas.indexOf(singerData)
                Log.d("ITEM", "idx : ${idx}")

                /*인텐트 생성하고, "SINGER_IDX" Key에 idx 값을 저장하여 DetailActivity로 전송   */
                val intent = Intent(itemView.context, DetailActivity::class.java)
                intent.putExtra(SINGER_IDX, idx)
                itemView.context.startActivity(intent)

                /*액티비티 이동 애니메이션 정의.*/
                //(itemView.context as Activity).overridePendingTransition(R.anim.fade_in, R.anim.fade_out);
            }
        }
    }
}