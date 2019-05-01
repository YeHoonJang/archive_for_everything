package com.example.bottomnavigation04.lotto


import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.bottomnavigation04.MainActivity


import com.example.bottomnavigation04.R

class RandomFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_random, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        /* RandomFragment에서 MainActivity로 생성된 로또번호를 전송하기 위해 Bundle 객체 생성 */
        val bundle = Bundle()

        /* 생성된 랜덤으로 생성된 로또번호를 ArrayList로 받아서"result" key로 번들객체에 저장
           - int 의 리스트를 전달하므로 putIntegerArrayListExtra 를 사용
        */
        bundle.putIntegerArrayList(
            "result",
            ArrayList(LottoNumberMaker.getShuffleLottoNumbers())
        )

        /* MainActivity에 선언된 moveToResultFragment(bundle)함수를 호출하여
           ResultFragment를 통해 생성된 로또번호를 출력함
           - MainActivity에 선언된 moveToResultFragment(bundle)함수를 호출하기 위해
             Activity를 가져와서 MainActivity로 강제 캐스팅
           - requireActivity(): 자신을 호출한 액티비티를 가져오는 메서드
           - requireContext(): 자신을 호출한 컨텍스트를 가져오는 메서드
         */
        (requireActivity() as MainActivity).moveToResultFragment(bundle)
    }
}
