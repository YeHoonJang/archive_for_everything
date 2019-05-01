package com.example.bottomnavigation02.lotto
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_name.*
import com.example.bottomnavigation02.R
import java.util.ArrayList

class NameActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_name)

        // 번호 생성 버튼의 클릭이벤트 리스너 설정
        goButton.setOnClickListener {
            // 입력된 이름이 없으면 토스트 메세지 출력후 리턴
            if (TextUtils.isEmpty(editText.text.toString())) {
                Toast.makeText(applicationContext, "이름을 입력하세요.", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            // ResultActivity 를 시작하는 Intent 생성
            val intent = Intent(this, ResultActivity::class.java)
            /*  intent에 생성된 로또번호(ArrayList type)를  "result" key로 저장
                 - 리스트를 전달하므로 putIntegerArrayListExtra 를 사용
                 - 전달하는 리스트는 이름의 해시코드로 생성한 로또 번호
             */
            intent.putIntegerArrayListExtra("result", ArrayList(LottoNumberMaker.getLottoNumbersFromHash(editText.text.toString())))
            // 입력받은 이름을 추가로 전달한다.
            intent.putExtra("name", editText.text.toString())
            // ResultActivity 를 시작하는 Intent 를 만들고 startActivity 로 실행
            startActivity(intent)
        }
        // 뒤로가기 버튼의 클릭이벤트 리스너 설정
        backButton.setOnClickListener {
            // 액티비티 종료
            finish()
        }
    }
}