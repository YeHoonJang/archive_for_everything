package com.example.bottomnavigation04.lotto


import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.CalendarView
import android.widget.DatePicker
import kotlinx.android.synthetic.main.fragment_constellation.view.*
import com.example.bottomnavigation04.MainActivity

import com.example.bottomnavigation04.R
import java.util.*

class ConstellationFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_constellation, container, false)
    }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.goResultButton.setOnClickListener {

            /* RandomFragment에서 MainActivity로 생성된 로또번호를 전송하기 위해 Bundle 객체 생성 */
            val bundle = Bundle()
            /* 별자리의 해시코드로 생성한 로또 번호를 ArrayList로 받아서"result" key로 번들객체에 저장
               - int 의 리스트를 전달하므로 putIntegerArrayListExtra 를 사용
            */
            bundle.putIntegerArrayList(
                "result",
                ArrayList(
                    LottoNumberMaker.getLottoNumbersFromHash(
                        makeConstellationString(
                            view.datePicker.month,
                            view.datePicker.dayOfMonth
                        )
                    )
                )
            )
            // 별자리를 추가로 전달한다.
            bundle.putString(
                "constellation",
                makeConstellationString(view.datePicker.month, view.datePicker.dayOfMonth)
            )
            // ResultActivity 를 시작하는 Intent 를 만들고 startActivity 로 실행
            (requireActivity() as MainActivity).moveToResultFragment(bundle)
        }
        // 현재 DatePicker 의 월, 일 정보로 별자리 텍스트 변경
        view.textView.text = makeConstellationString(view.datePicker.month, view.datePicker.dayOfMonth)
        // DatePicker 의 날짜가 변화하면 별자리를 보여주는 텍스트뷰도 변경
        val calendar = Calendar.getInstance()
        view.datePicker.init(
            calendar.get(Calendar.YEAR),
            calendar.get(Calendar.MONTH),
            calendar.get(Calendar.DAY_OF_MONTH),
            object : CalendarView.OnDateChangeListener, DatePicker.
            OnDateChangedListener {
                override fun onDateChanged(datePicker: DatePicker?, year: Int, monthOfYear: Int, dayOfMonth: Int) {
                    // 변경된 시점의 DatePicker 의 월, 일 정보로 별자리 텍스트 변경
                    view.textView.text = makeConstellationString(view.datePicker.month, view.datePicker.dayOfMonth)
                }

                override fun onSelectedDayChange(view: CalendarView?, year: Int, month: Int, dayOfMonth: Int) {
                }
            })
    }

    /**
     * 전달받은 월정보, 일정보 기준으로 별자리를 반환한다.
     */
    fun makeConstellationString(month: Int, day: Int): String {
        // 전달받은 월 정보와 일 정보를 기반으로 정수형태의 값을 만든다.
        // ex) 1월 5일 --> 105, 11월 1일 --> 1101
        val target = "${month + 1}${String.format("%02d", day)}".toInt()
        when (target) {
            in 101..119 -> return "염소자리"
            in 120..218 -> return "물병자리"
            in 219..320 -> return "물고기자리"
            in 321..419 -> return "양자리"
            in 420..520 -> return "황소자리"
            in 521..621 -> return "쌍둥이자리"
            in 622..722 -> return "게자리"
            in 723..822 -> return "사자자리"
            in 823..923 -> return "처녀자리"
            in 924..1022 -> return "천칭자리"
            in 1023..1122 -> return "전갈자리"
            in 1123..1224 -> return "사수자리"
            in 1225..1231 -> return "염소자리"
            else -> return "기타별자리"
        }
    }
}
