package com.example.mobileprogramming.list_rent


import android.content.Context
import android.os.Bundle
import android.support.v4.app.Fragment
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import com.example.mobileprogramming.R
import kotlinx.android.synthetic.main.fragment_rent.*
import kotlinx.android.synthetic.main.fragment_tab.*
import kotlinx.android.synthetic.main.nav_header_main.*

class RentFragment : Fragment() {

    /* 프래그먼트에 표시될 뷰를 생성하여 반환하는 메서드
       - 프래그먼트에 표시할 뷰를 생성(인플레이션)하여 반환
       - 인자로 전달된 inflater로 프래그먼트 xml 레이아웃 파일을 인플레이션하여 리턴(view를 반환)
    */
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        Log.d("LOG", "onCreateView")
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_rent, container, false)
    }


    /* 프래그먼트에 표시할 뷰에 데이터 바인딩
       - 프래그먼트에 표시할 뷰가 생성된 직후에 호출되며,
       - onCreateView에서 반환한 view를 인자로 받아 view에 데이터를 바인딩하고,
         필요한 기능을 구현하는 코드 작성
     */
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        Log.d("LOG", "onViewCreated" + arguments?.getString("title"))

        //Bundle 객체의 arguments 프로퍼티에 저장된 "title" key 값을 추출하여 프래그먼트 텍스트뷰에 설정
        textView.text = arguments?.getString("title")
    }

    /* 프래그먼트는 특수한 제약 때문에 팩토리 메서드를 사용하여 객체를 생성함
       - 팩토리 메서드:생성자가 아닌 메서드를 사용해 객체를 생성하는 코딩 패턴을 말함
       - 코틀린에서는 자바의 static처럼 정적인 메서드를 만들 수 있는 키워드를 제공하지 않기 때문에
         companion object로 정적인 메서드를 구현함
    */
    companion object {
        /* 프래그먼트에 데이터를 전달하는 일반적인 방법(bundle 객체 이용)
           - newInstance() 정적 메서드를 사용해서 Fragment 객체를 생성(팩토리 패턴)
           - Bundle 객체에 데이터를 저장한 후에 프래그먼트의 arguments 프로퍼티를 이용하여
             프래그먼트에 저장
        */
        fun newInstance(title: String): TabFragment {
            // bundle 객체 생성
            val bundle = Bundle()
            //인자로 전달받은 title("홈화면,...)을 bundle 객체에 "title"키로 저장
            bundle.putString("title", title)

            //tabFragment 생성
            val tabFragment = TabFragment()
            /* bundle 객체를 tabFragment의 arguments 프로퍼티에 저장 */
            tabFragment.arguments = bundle
            return tabFragment
        }
    }
}
