package com.example.bottomnavigation04.lotto

import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_result.view.*

import com.example.bottomnavigation04.R
import java.text.SimpleDateFormat
import java.util.*

class ResultFragment : Fragment() {
    // 로또 1번 공 이미지의 아이디를 사용
    val lottoImageStartId = R.drawable.ball_01

    /* 프래그먼트로 출력할 View를 생성하여 반환
       - 반환된 View는 onViewCreated() 메서드로 인자로 전달됨
     */
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_result, container, false)
    }
    // 프래그먼트로 출력할 View에 데이터 바인딩 및 필요한 로직처리
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // 전달받은 결과 배열을 가져온다.
        val result = arguments?.getIntegerArrayList("result") ?: ArrayList()
        // 전달받은 이름을 가져온다.
        val name = arguments?.getString("name")
        // 전달받은 별자리를 가져온다
        val constellation = arguments?.getString("constellation")
        // 결과화면 기본 텍스트
        view.resultLabel.text = "랜덤으로 생성된\n로또번호입니다"
        // name 이 전달된 경우 결과화면의 텍스트를 변경
        if (!name.isNullOrEmpty()) {
            view.resultLabel.text = "${name} 님의\n${SimpleDateFormat("yyyy년 MM월 dd일").format(Date())}\n로또 번호입니다"
        }
        // 별자리가 전달된 경우 텍스트 변경
        if (!constellation.isNullOrEmpty()) {
            view.resultLabel.text = "${constellation} 의\n${SimpleDateFormat("yyyy년 MM월 dd일").format(Date())}\n로또 번호입니다"
        }
        // 전달받은 결과가 있는 경우에만 실행
        result.let {
            // 결과에 맞게 로또 공 이미지를 업데이트한다.
            // 전달받은 결과는 정렬되어 있지않으므로 정렬해서 전달한다.
            updateLottoBallImage(result.sortedBy { it }, view)
        }
    }

    //로또번호 이미지뷰 설정 함수 선언
    fun updateLottoBallImage(result: List<Int>, rootView: View) {
        // 결과의 사이즈가 6개 미만인경우 에러가 발생할 수 있으므로 바로 리턴한다.
        if (result.size < 6) return
        // ball_01 이미지 부터 순서대로 이미지 아이디가 있기 때문에
        // ball_01 아이디에 결과값 -1 을 하면 목표하는 이미지가 된다
        // ex) result[0] 이 2번 공인 경우 ball_01 에서 하나뒤에 이미지가 된다.
        rootView.imageView01.setImageResource(lottoImageStartId + (result[0] - 1))
        rootView.imageView02.setImageResource(lottoImageStartId + (result[1] - 1))
        rootView.imageView03.setImageResource(lottoImageStartId + (result[2] - 1))
        rootView.imageView04.setImageResource(lottoImageStartId + (result[3] - 1))
        rootView.imageView05.setImageResource(lottoImageStartId + (result[4] - 1))
        rootView.imageView06.setImageResource(lottoImageStartId + (result[5] - 1))
    }
}
