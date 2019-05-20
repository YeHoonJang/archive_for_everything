package com.example.coroutinetest01



import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v4.app.ListFragment
import android.widget.ArrayAdapter
import com.example.coroutinetest01.fragment.ExceptionFragment
import com.example.coroutinetest01.fragment.LaunchFragment
import com.example.coroutinetest01.fragment.LaunchParallelFragment
import com.example.coroutinetest01.fragment.LaunchSequentiallyFragment

/*  ListFragment를 이용하여

 */
class MainListFragment : ListFragment() {

    companion object {
        const val TAG = "MainListFragment"

        private const val SAMPLE_LAUNCH = "1. 코루틴 launch"
        private const val SAMPLE_SEQUENTIALLY = "2. 코루틴 동기호출"
        private const val SAMPLE_PARALLEL = "3. 코루틴 비동기호출"
        private const val SAMPLE_EXCEPTION = "6. 코루틴 에러처리"
    }

    /* Fragment 생성 이후 호출 하는 함수
       - 화면에 출력할 UI 작업을 수행
     */
    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        //ListView의 아이템으로 사용할 list 배열 선언
        val list = arrayListOf(
            SAMPLE_LAUNCH,
            SAMPLE_SEQUENTIALLY,
            SAMPLE_PARALLEL,
            SAMPLE_EXCEPTION
        )

        //ArrayAdapter 설정(context, layout(simple_list_item_1), data(list)
        listAdapter = ArrayAdapter<String>(context, android.R.layout.simple_list_item_1, list)

        /* listView의 아이템 클릭시 이벤트 처리를 위한 리스너 등록
           - onItemClick(parent, view, position, id)
         */

        listView.setOnItemClickListener { _, _, position, _ ->
            when (list[position]) {
                SAMPLE_LAUNCH -> showFragment(LaunchFragment(), LaunchFragment.TAG)//태그를 사용하기 위해 태그도 전달
                SAMPLE_SEQUENTIALLY -> showFragment(LaunchSequentiallyFragment(), LaunchSequentiallyFragment.TAG)
                SAMPLE_PARALLEL -> showFragment(LaunchParallelFragment(), LaunchParallelFragment.TAG)
                SAMPLE_EXCEPTION -> showFragment(ExceptionFragment(), ExceptionFragment.TAG)
            }
        }
    }

    /* 액티비티 레이아웃(activity_main.xml)의 FrameLayou view(fragmentContainer)를
       인자로 전달된 Fragment로 교체.
   */
    private fun showFragment(fragment: Fragment, tag: String) {
        requireActivity().supportFragmentManager.beginTransaction()
            .replace(R.id.fragmentContainer, fragment, tag) //새로운 Fragment로 replace
            .addToBackStack(tag) //백스텍에 추가
            .commit()
    }
}
