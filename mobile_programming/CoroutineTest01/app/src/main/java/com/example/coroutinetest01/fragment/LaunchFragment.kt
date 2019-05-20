package com.example.coroutinetest01.fragment


import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_button.*
import kotlinx.android.synthetic.main.fragment_button.view.*
import kotlinx.coroutines.*
import com.example.coroutinetest01.R
import java.util.*
import java.util.concurrent.TimeUnit


class LaunchFragment : Fragment() {

    /* 코루틴을 어떤 스레드에서 수행시킬지 지정(현재 Fragment의 Main 쓰레드를 지정)
      - Dispatchers는 어떤 스레드에서 코루틴을 수행시킬지 결정
      - Dispatchers.Main : 안드로이드의 Main 스레드를 의미함
    * */
    private val uiDispatcher: CoroutineDispatcher = Dispatchers.Main

    /*데이터를 로드하기위한 DataProvider 객체 생성 */
    private val dataProvider = DataProvider()

    /* 코루틴의 Job 스케쥴을 관리하는 객체를 독립적으로 선언
      - Job이란? : 현재 실행되고있는 코루틴({})의 상태값을 가지고 있는 인스턴스
      - Job을 바탕으로 코루틴의 상태를 확인할 수 있고, 취소할 수 있다.
      - Job은 N 개의 coroutines의 동작을 제어할 수도 있으며, 하나의 coroutines 동작을 제어할 수도 있다
      - 자식코루틴은 부모코루틴의 job이 취소되면 함께 취소되며 자식코루틴만 취소하고싶다면 별도의 job을 할당하여 취소해주면된다.
    */
    private lateinit var job: Job

    // final static 상수 선언
    companion object {
        const val TAG = "LaunchFragment"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        /* job 생성
           - 독립적인 job을 생성하여 "Dispatchers.Main + job" 형태로 함께 초기화하면,
             이 CoroutineScope의 child 까지 모두 제어할 수 있음
           - Dispatchers.Main + job : 기본 Main Thread 정의와 Job을 함께 초기화
       */
        job = Job()
    }

    // 프래그먼트에 표시될 뷰를 생성하여 반환
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        return inflater.inflate(R.layout.fragment_button, container, false)
    }

    //onCreateView에서 생성한 view를 인자로 받아 view에 데이터 바인딩
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        /* 버튼 클릭시 이벤트 처리를 위한 클릭 리스너 연결
           - 데이터를 로드하는 loadData() 함수 호출
       */
        view.button.setOnClickListener { loadData() }
    }

    /* view가 destory 될때 호출
       - view가 종료되면 코루틴도 함께 종료되도록 job.cancel()
     */
    override fun onDestroyView() {
        super.onDestroyView()
        /*만약 job을 끝내지않았는데 child job이 돌고있다면 job이 끝날때 에러가 발생합니다. */
        job.cancel()
    }

    /* 코루틴 수행
       - Dispatchers.Main + job : UI를 위한 쓰레드에 독립적으로 생성한 job을 할당
       - launch는 coroutine의 빌더이며 이를 이용해서 코루틴 수행
     */
    private fun loadData() = GlobalScope.launch(uiDispatcher) {
        println("My job is  ${coroutineContext}")
        println("1] I'm working in thread ${Thread.currentThread().name}")

        showLoading() // ui thread

        println("2] I'm working in thread ${Thread.currentThread().name}")

        /* suspend 된 loadData()함수 호출
           - 스레드는 loadData() 함수에서 값이 올 때까지 non-blocking 상태로 쉬고있음
         */

        // val result = async { dataProvider.loadData() } // non ui thread, suspend until finished
        val result = dataProvider.loadData() // non ui thread, suspend until finished

        println("3] I'm working in thread ${Thread.currentThread().name}, ${result}")

        showText(result) // ui thread
        hideLoading() // ui thread
    }

    //ui thread
    private fun showLoading() {
        progressBar.visibility = View.VISIBLE
    }
    //ui thread
    private fun hideLoading() {
        progressBar.visibility = View.GONE
    }
    //ui thread
    private fun showText(data: String) {
        textView.text = data
    }

    /* DataProvider class 선언
       - Dispatchers.IO : IO 연산을 위한 스레드
     */
    class DataProvider(private val dispatcher: CoroutineDispatcher = Dispatchers.IO) {

        /* withContext: 코루틴이 수행될 스레드(coroutineContext)를 변경하는 coroutine builder
           - 코루틴이 수행될 스레드를 IO 스레드(IO연산을 수행하는 스레드 풀)로 변경
           - withContext를 사용하는 이유는 io 작업과 같이 main(ui)스레드에서 수행할 수 없는 작업을 위해
             스레드를 잠시 전환하는 작업
           - withContext 수행이 완료되면 코루틴은 이전에 명시되었던 Dispatchers에서 계속 작업을 수행

           - suspend는 중단/재개 시점을 위한 continuation을 매핑하기 위한 키워드
           - continuation:중단 시점등의 실행 상태 기록/추적을 위한 인터페이스
        */
        suspend fun loadData(): String = withContext(dispatcher) {

            println("4]I'm working in thread ${Thread.currentThread().name}")

            /* 테스트를 위해 10초 동안 deley
               - 네트워크나 database와같은 비동기 작업을 이곳에서 수행
               - TimeUnit.SECONDS.toMillis(2): 2초를 밀리세컨드로 변환
               - nextInt()메소드는 Random 클래스의 메소드로, 난수를 발생시키는 메서드
             */
            delay(TimeUnit.SECONDS.toMillis(10)) // imitate long running operation
            "데이터 출력: ${Random().nextInt()}"
        }//end of withContext

    }//end of DataProvider
}
