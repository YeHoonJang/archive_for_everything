package kr.ac.gachon.ugkang.recyclerview02

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.DividerItemDecoration
import android.support.v7.widget.GridLayoutManager
import android.support.v7.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* RecyclerView의 Divider 구분선 넣기 */
        val divider = DividerItemDecoration(this, DividerItemDecoration.VERTICAL)
        recyclerView_singer.addItemDecoration(divider)

        //리사이클러뷰에 어댑터 설정
        recyclerView_singer.adapter = SingerAdapter()

        //리사이클러뷰에 레이아웃메니저 설정
        recyclerView_singer.layoutManager = LinearLayoutManager(this)
    }
}
