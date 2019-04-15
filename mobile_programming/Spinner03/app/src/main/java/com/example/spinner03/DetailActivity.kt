package com.example.spinner03


import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_detail.*

//상세보기 액티비티
class DetailActivity : AppCompatActivity() {
    /* lateinit : 늦은 초기화 선언(var)
      - 클래스 생성과 동시에 사용되지 않는 프로퍼티(변수)에 대해서 늦은 초기화를 선언할 수 있음
      - Non-null 프로퍼티가 생성자 단계에서 값이 초기화되지 않은 상태를
        컴파일러가 인정하도록 하여 정상적으로 컴파일이 되도록 함
        (선언된 프로퍼티는 생성자 단계에서 초기화해야 함)
      - lateinit은 이 프로퍼티는 절대로 Null이 될 수 없는 프로퍼티인데
        선언과 동시에 초기화를 해줄 수 없거나 성능이나 기타 다른 조건들로 인해
        최대한 초기화를 미뤄야 할 때 사용
      - var로 선언한 프로퍼티에만 사용할 수 있으며, 클래스 몸체, Top-Level,
        함수 내부에 선언한 프로퍼티만 사용할 수 있음(주 생성자에서는 사용할 수 없음)
      - null 허용 프로퍼티와 기초 타입 프로퍼티에는 사용할 수 없음
    */
    lateinit var singer: SingerData

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detail)

        //인텐트에서 "SINGER_IDX"라는 이름으로 전달된 가수의 position(인텍스) 정보를 추출
        val singerIdx = intent.getIntExtra(SINGER_IDX, -1)

        /*넘어온 값이 없어 디폴트 값 -1일경우 */
        if (singerIdx == -1) {
            Toast.makeText(this, "등록된 가수정보가 없습니다.", Toast.LENGTH_LONG).show()
        } else {
            /* singerIdx(인덱스값)를 이용하여 전체 가수 데이터에서 해당 인덱스값에 해당하는 가수의 정보(SingerData)를
               singer 객체에 저장(singer 객체 초기화)
            */
            singer = singerDatas[singerIdx]
        }

        //해당 가수의 정보(singer 객체)를 이용하여 상세보기 레이아웃(activity_detail.xml)에 데이터를 바인딩
        img_singer_photo.setImageResource(singer.imgRes)
        txt_singer_name.text = singer.singer
        txt_singer_song.text = singer.song

    }

    //"SINGER_IDX"를 전역상수로 사용하기 위해 final static으로 선언
    companion object {
        const val SINGER_IDX = "SINGER_IDX"
    }
}