package com.example.coroutinetest01.fragment


import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.fragment_button.*
import kotlinx.coroutines.*
import com.example.coroutinetest01.R
import java.util.*
import java.util.concurrent.TimeUnit
import kotlin.system.measureTimeMillis


class LaunchParallelFragment : Fragment() {

    private val uiDispatcher: CoroutineDispatcher = Dispatchers.Main
    private val dataProvider = DataProvider()
    private lateinit var job: Job

    companion object {
        const val TAG = "LaunchParallelFragment"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        job = Job()
    }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        return inflater.inflate(R.layout.fragment_button, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        button.setOnClickListener { loadData() }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        job.cancel()

    }

    private fun loadData() = GlobalScope.launch(uiDispatcher + job) {
        showLoading()

        var data = ""

        /* suspend된 loadData()함수를 비동기 호출
           - 스레드는 loadData() 함수에서 값이 올 때까지 non-blocking 상태로 쉬고있음
           -  async는 블록{}에서 수행된 결과를 Deferred(지연된 값) 형태로 받음
           - Deferred 값에서 실제 값을 뽑아 내기 위해 result1.await()로 호출
           - async는 await이될 때까지 값이 실행되지않습니다. 때문에 리턴값이 Deferred 형태로 반환됩니다.
           - Deferred는 job을 상속 받기 때문애 cancel도 가능함
           - async : Coroutine builder
         */
        val runTime = measureTimeMillis {
            val result1 = async { dataProvider.loadData() } // defer 2초
            val result2 = async { dataProvider.loadData() } // 2초

            data = "${result1.await()}\n${result2.await()}" //두개의 데이터가 다 로드될때까지 기다립니다.
        }

        println("loadData() Completed in $runTime")

        showText(data)
        hideLoading()
    }

    private fun showLoading() {
        progressBar.visibility = View.VISIBLE
    }

    private fun hideLoading() {
        progressBar.visibility = View.GONE
    }

    private fun showText(data: String) {
        textView.text = data
    }

    class DataProvider(private val dispatcher: CoroutineDispatcher = Dispatchers.IO) {

        suspend fun loadData(): String = withContext(dispatcher) {
            /* 2 초동안 지연
               - TimeUnit.SECONDS.toMillis(2): 2초를 밀리세컨드로 변환
               - nextInt()메소드는 Random 클래스의 메소드로, 난수를 발생시키는 메서드
             */
            delay(TimeUnit.SECONDS.toMillis(5)) // imitate long running operation
            "Data is available: ${Random().nextInt()}"
        }
    }

}
