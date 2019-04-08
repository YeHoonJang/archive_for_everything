package kr.ac.gachon.ugkang.recyclerview02

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_detail.*

//상세보기 액티비티
class DetailActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        //인텐트에서 "SINGER"라는 이름으로 전달된 가수의 상수명을 문자열로 추출
        val singerName = intent.getStringExtra(SINGER)
        //추출한 상수명으로 SingerData(enum class)에서 해당 가수의 상수(객체)를 가져옴
        val singerData = SingerData.valueOf(singerName)

        //해당 가수의 정보를 상세보기 레이아웃(activity_detail.xml)에 바인딩
        img_singer_photo.setImageResource(singerData.imgRes)
        txt_singer_name.text = singerData.singer
        txt_singer_song.text = singerData.song
    }

    //"SINGER"를 전역상수로 사용하기 위해 final static으로 선언
    companion object {
        const val SINGER = "SINGER"
    }
}
