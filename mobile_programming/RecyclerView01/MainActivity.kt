package kr.ac.gachon.ugkang.recyclerview01

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.GridLayoutManager
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.StaggeredGridLayoutManager
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //리사이클러뷰에 어댑터 설정
        recycle_shop.adapter = ShopRecyclerAdapter()

        /* 리사이클러뷰에 레이아웃메니저 설정
           - 리사이클러뷰의 각 아이템을 배치하고, 뷰홀더 재사용 결정
           - 리사이클러뷰의 리스트출력할 때 모양을 설정할 수 있음(가로,세로,격자,불규칙 모양 지정)
           - 안드로이드에서 지원하는 레이아웃메니저
             1) LinearLayoutManager, 2) GridLayoutManager, 3) staggeredGridLayoutManager
         */
        recycle_shop.layoutManager = LinearLayoutManager(this)
        //recycle_shop.layoutManager = LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        //recycle_shop.layoutManager = GridLayoutManager(this, 2)
        //recycle_shop.layoutManager = StaggeredGridLayoutManager(2, StaggeredGridLayoutManager.VERTICAL)
    }
}
