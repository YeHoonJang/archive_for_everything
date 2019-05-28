package com.example.mynaverapp1.dialog

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.DialogFragment
import kotlinx.android.synthetic.main.dialog_news_search.view.*
import com.example.mynaverapp1.MainActivity
import com.example.mynaverapp1.R

class NewsSearchDialog : DialogFragment() {

    //프래그먼트에 표시될 뷰(rootView)를 생성하여 반환
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        val rootView = inflater.inflate(R.layout.dialog_news_search, container, false)

        /* 검색 키워드 입력 다이얼로그창에서 검색버튼을 클릭한 경우 이벤트 처리
           - loadNewsDataFromAPI(this) 함수를 이용하여 검색 요청(서버에 요청)
         */
        rootView.btn_search_news.setOnClickListener {

            with(rootView.edit_search_news.text.toString()) {
                if (isNotBlank()) {
                    /* Fragment에서 Activity로 네트워크 요청을 위임하는 부분*/
                    (requireActivity() as MainActivity).loadNewsDataFromAPI(this)
                    dismiss()
                } else {
                    android.widget.Toast.makeText(requireContext(), "메세지를 입력해주세요.", android.widget.Toast.LENGTH_LONG).show()
                }
            }

        }
        return rootView
    }
}