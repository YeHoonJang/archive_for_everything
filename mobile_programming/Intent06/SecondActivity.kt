package kr.ac.gachon.ugkang.intent06

import android.app.Activity
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import kotlinx.android.synthetic.main.activity_second.*

class SecondActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_second)

        //============ MainActivity에서 인텐트로 보낸 객체(ParcelCless)를 복원 =============
        /* getParcelableExtra() 메서드를 이용하여 MainActivity에서 보낸 인텐트에서 객체를 복원하여 t1객체에 할당
           - 이때 ParcelCless의 createFromParcel() 메서드가 호출되어 객체의 속성값을 복원하여
             객체를 반환(객체를 복원할 때 <ParcelTestCless>로 형 변환)
         */
        var t1 = intent.getParcelableExtra<ParcelCless>("parcel1")

        Log.d("INTENT6", "SecondActivity")

        //t1 객체에서 id, name 속성값을 getter하여 textView2에 표시
        textView2.text = "MainActivity에서 보낸 객체\n\n"
        textView2.append("t1.id : ${t1.id}\n")
        textView2.append("t1.name : ${t1.name}")

        button2.setOnClickListener {
            //MasinActivity로 보낼 객체를 생성
            val p2 = ParcelCless()
            p2.id = 2019002
            p2.name = "이승우"

            // 인텐트 생성 및 객체 저장
            var intent = Intent()
            intent.putExtra("parcel2", p2)

            //MainActivity로 응답
            setResult(Activity.RESULT_OK, intent)
            finish()
        }
    }
}
