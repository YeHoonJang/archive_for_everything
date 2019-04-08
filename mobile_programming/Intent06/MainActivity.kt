package kr.ac.gachon.ugkang.intent06

import android.app.Activity
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    val REQUEST_CODE = 1001

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        button.setOnClickListener {
            //ParcelCless() 객체를 생성하고 id, name 속성값 설정
            var p1 = ParcelCless()
            p1.id = 2019001
            p1.name = "손흥민"

            //SecondActivity를 호출할 인텐트 생성
            var intent = Intent(this, SecondActivity::class.java)

            // SecodeActivity에 보낼 p1 객체(ParcelCless()의 인스턴스)를 인텐트에 저장
            intent.putExtra("parcel1", p1)

            /* 객체를 담은 인텐트를 startActivityForResult()를 이용하여 안드로이드 OS에 전달하면,
              - P1 객체의  writeToParcel(dest: Parcel?, flags: Int)) 메서드가 호출되며,
                이때 dest 매개변수에 Parcel? 객체타입으로 p1 객체가 전달되어,
                id와 name의 속성값이 저장되어 SeconActivity로 전달하는 구조임
            */
            Log.d("INTENT6", "MainActivity")
            startActivityForResult(intent, REQUEST_CODE)
        }
   }

    //SecondActivity에서 보낸 인텐트 처리
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (resultCode == Activity.RESULT_OK) {
            var t2 = data?.getParcelableExtra<ParcelCless>("parcel2")

            textView.text = "SecondActivity에서 보낸 객체\n\n"
            textView.append("t2.id : ${t2?.id}\n")
            textView.append("t2.name : ${t2?.name}")
        }

    }
}
