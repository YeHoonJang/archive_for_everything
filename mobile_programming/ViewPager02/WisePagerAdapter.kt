package kr.ac.gachon.ugkang.viewpager02

import android.support.v4.view.PagerAdapter
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.list_item_pageview.view.*

class WisePagerAdapter(): PagerAdapter() {
    //어댑터에서 관리하는 아이템의 개수를 반환(뷰페이저의 전체 페이지 수를 결정)
    override fun getCount(): Int {
        return WiseSayingData.values().size
    }

    /* 현재 객체가 보여줄 객체와 일치하는지 확인하여 상태(true/false)를 반환
       - 화면에 보여줄 페이지뷰와 객체가 동일한지 여부를 검사하여 그 결과를 리턴
       - p0와 p1가 일치하는 경우에만 화면에 보여줌
   */
    override fun isViewFromObject(p0: View, p1: Any): Boolean {
        return p0 == p1
    }

    /* 화면에 표시할 페이지뷰 생성
       - 매개변수로 전달받은 position에 해당하는 페이지뷰(pageView)를 생성한 다음,
         또 다른 매개변수로 전달된 컨테이너(뷰페이저 객체)에 생성된 페이지뷰를 추가(addView)
       - 그런 다음, 페이지 식별을 위한 객체(pageView)를 반환
    */
    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        /* 뷰페이저에 출력할 페이지뷰(list_item_pageview.xml)를 인플레이트
           - 페이지뷰에 바인딩할 해당 데이터를 position을 이용하여 WiseSayingData에서 가져옴
        */
        val pageView = LayoutInflater.from(container.context).inflate(R.layout.list_item_pageview, container, false)
        val wiseData = WiseSayingData.values()[position]

        /* 페이지뷰에 해당 데이터 설정 */
        pageView.txt_wise.text = wiseData.wiseText
        pageView.txt_writer.text = wiseData.writer

        /* 뷰페이저에 페이지뷰 추가
           - 이때 pageView가 isViewFromObject()메서드의 매개변수 p0에 전달
        */
        container.addView(pageView)

        /* 페이지 식별을 위해 pageView 리턴
           - 이때 pageView가 isViewFromObject()메서드의 매개변수 p1에 전달
         */
        return pageView;
    }

    /* 화면에서 사라진 뷰를 삭제
       - 스크롤시 더이상 화면에서 안보이는 뷰를 제거
    */
    override fun destroyItem(container: ViewGroup, position: Int, `object`: Any) {
        /* `object`를 View로 형 변환하여 제거
           - `object` : 코틀린에서는 키워드를 변수로 사용할 수 있기 때문에 구분하기 위해
              `키워드`를 특수 문자로 묶어 처리(`object` 변수명을 사용자가 변경해도 됨, obj..)
        */
        container.removeView(`object` as View)
    }
}