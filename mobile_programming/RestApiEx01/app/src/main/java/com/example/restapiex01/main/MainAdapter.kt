package com.example.restapiex01.main

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.activity_save.view.*
import com.example.restapiex01.R
import com.example.restapiex01.local.LocalDbSearchActivity
import com.example.restapiex01.model.SaveItem

/* 메인화면에서 저장된 데이터를 리사이클러뷰에 보여주는 어댑터 */
class MainAdapter(var saveItems: List<SaveItem>) : RecyclerView.Adapter<MainAdapter.ItemViewHolder>() {

    /* 뷰홀더를 생성하여 반환 */
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val rootView = LayoutInflater.from(parent.context).inflate(R.layout.activity_save, parent, false)
        return ItemViewHolder(rootView)
    }

    //뷰홀더에 데이터 바인딩(bindItems() 함수를 호출)
    override fun onBindViewHolder(holder: ItemViewHolder, position: Int) {
        holder.bindItems(saveItems[position])
    }

    //어댑터에서 관리할 아이템 갯수를 반환
    override fun getItemCount() = saveItems.size

    //뷰홀더 클래스 선언
    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bindItems(saveItem: SaveItem) {
            /* local DB에 저장된 경락가격정보의 목록을 리사이클러뷰로 보여줄 때 아이템뷰의 텍스트를 설정
               -  SaveItem 테이블에 저장된 경락가격정보 타이틀(saveTitle)을 itemView.txt_save_subject에 설정
             */
            itemView.txt_save_subject.text = saveItem.saveTitle

            /* 메인화면 리사이클러뷰의 아이템을 클릭하면, id를 saveId에 저장하여 인텐트를 생성하여
               LocalDbSearchActivity를 실행하여 선택한 아이템의 상세화면을 보여준다.
            */
            itemView.setOnClickListener {
                /* 액티비티를 시작합니다.*/
                itemView.context.startActivity(
                    /*액티비티에 saveId를 넣습니다. */
                    Intent(itemView.context, LocalDbSearchActivity::class.java).putExtra("saveId", saveItem.id)
                )
            }
        }
    }
}
