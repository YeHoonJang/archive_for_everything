package com.example.bottomnavigation04.lotto


import android.os.Bundle
import android.support.v4.app.Fragment
import android.text.TextUtils
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import kotlinx.android.synthetic.main.fragment_name.view.*
import com.example.bottomnavigation04.MainActivity

import com.example.bottomnavigation04.R

class NameFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_name, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // 번호 생성 버튼의 클릭이벤트 리스너 설정
        view.goButton.setOnClickListener {
            // 입력된 이름이 없으면 토스트 메세지 출력후 리턴
            if (TextUtils.isEmpty(view.editText.text.toString())) {
                Toast.makeText(requireContext(), "이름을 입력하세요.", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            /* RandomFragment에서 MainActivity로 생성된 로또번호를 전송하기 위해 Bundle 객체 생성 */
            val bundle = Bundle()
            /* 이름의 해시코드로 생성한 로또 번호를 ArrayList로 받아서"result" key로 번들객체에 저장
               - int 의 리스트를 전달하므로 putIntegerArrayListExtra 를 사용
            */
            bundle.putIntegerArrayList(
                "result",
                ArrayList(LottoNumberMaker.getLottoNumbersFromHash(view.editText.text.toString()))
            )
            // 입력받은 이름을 추가로 전달한다.
            bundle.putString("name", view.editText.text.toString())
            /* resultFragment로 FrameLayout(id:frame_main)을 갱신하기위해,
               생성한 로또번호를 가지고 있는 bundle 객체를

              - requireActivity(): 자신을 호출한 액티비티를 가져오는 메서드
              - requireContext(): 자신을 호출한 컨텍스트를 가져오는 메서드
             */
            (requireActivity() as MainActivity).moveToResultFragment(bundle)
        }
    }
}
