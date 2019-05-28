package com.example.mynaverapp1.list


import android.content.Intent
import android.net.Uri
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.list_item_news.view.*
import com.example.mynaverapp1.R

/* NewsAdpater 클래스 선언 */
class NewsAdpater(var newsList: ArrayList<News>) : RecyclerView.Adapter<NewsAdpater.ItemViewHolder>() {

    /* 뷰홀더를 생성하여 반환 */
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val rootView = LayoutInflater.from(parent.context).inflate(R.layout.list_item_news, parent, false)
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
        //뉴스 데이터 바인딩
        fun bindItems(news: News) {
            itemView.txt_news_title.text = news.title
            itemView.txt_news_content.text = news.description
            itemView.setOnClickListener {
                val myIntent = Intent(Intent.ACTION_VIEW, Uri.parse(news.link))
                ContextCompat.startActivity(itemView.context, myIntent, null)
            }
        }
    }
}
