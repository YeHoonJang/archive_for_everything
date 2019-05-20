package com.example.roomdb01

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.LifecycleObserver
import androidx.lifecycle.LifecycleOwner
import androidx.lifecycle.Observer
import androidx.paging.LivePagedListBuilder
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.Job
import com.example.roomdb01.dialog.NoteCreateDialog
import com.example.roomdb01.list.NoteAdapter
import com.example.roomdb01.room.AppDatabase

/* LifecycleOwner: 라이프사이클 자신(Activity, Fragment)
   - Activity, fragment에서 생명주기를 분리하여 Lifecycle 객체에 담는다.
   - Lifecycle 객체를 통해 다른 곳에서 해당화면의 생명주기를 모니터링 할 수 있음
   - 자신의 생명주기(Lifecycle)를 담은 Lifecycle 객체가 LifecycleOwner 입니다.

  LifecycleObserver: 라이프사이클을 모니터링할 수 있는 인터페이스
    - 화면 밖에서도 생명주기에 따른 정의하기 위해서는 원하는 클래스에
      LifecyclerObserver 인터페이스를 구현하고, 넘겨받은 LifecycleOwner 객체에
      구현한 LifecycleObserver를 등록해야 함
    - LifecycleObserver를 구현한 클래스는 onResume() 등의 생명주기 메서드를 정의할 수 있음
    - 이 메소드들은 등록한 LifecycleOwner가 해당 생명주기 상태가 되면
      자동으로 수행되면서, 객체가 화면과 동일한 생명주기를 가진 것처럼 동작함

   ** androidx 버전에서는 LifecycleOwner, LifecycleObserver 인터페이스 선언을 생략해도 됨
 */
class MainActivity : AppCompatActivity(), LifecycleOwner, LifecycleObserver{

    /* MainActivity가 생성될때 Context가 아직 초기화되지 않았기때문에 Lazy 키워드를 이용하여
       처음 호출될때 초기화하도록 설정
   */
    // database
    val database: AppDatabase by lazy { AppDatabase.getDatabase(this) }
    //job
    val job by lazy { Job() }

    //noteDao
    val noteDao by lazy { AppDatabase.getDatabase(this).noteDao() }

    //notiAdapter
    val notiAdapter by lazy { NoteAdapter(job, noteDao) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        /* RecycleView Initialize*/
        recycle_note.adapter = notiAdapter
        recycle_note.layoutManager = LinearLayoutManager(this)

        /* Query 할 때 반환값을 DataSource.Factory<Int, Note> 형태로 지정하고,
           사용자가 반환값 대해서 DB의 값을 바꾸면 Observer 콜백들이 자동으로 실행되어,
           사용자가 DB를 바꾸면 UI도 자동으로 갱신됨
        */

        /* LivePagedListBuilder(data-Source, page-size)로 PageList 생성
           - 반환값이 LiveData로 Observable 패턴과 같이 데이터의 변동사항이 있을때 계속 데이터를 갱신
           - LivePagedListBuilder에 Page 속성과 DataSource를 정의하고 빌드하면,
             LiveData<PagedList<Item>로 pageList를 반환
        */
        val getDataFromDB = LivePagedListBuilder(database.noteDao().selectNotes(), 20).build()

        /* LiveDta로부터 변경된 PageList가 넘어오면 값을 Adapter에 전달
           - param owner : Observer를 제어하는 LifecycleOwner -
           - param Observer : LiveDta 로부터 이벤트를 수신(데이터가 변경되면 호출됨)
        */
        getDataFromDB.observe(this, Observer {

            /* 변경된 pageList를 PagedAdapter에 전달
               - PagedList 를 submit하면 PagedListAdapter 의 AsyncPagedListDiffer 는
                 기존에 PagedList가 존재하면 그 차이를 비교한 후 리사이클러뷰를 새로운 페이지로 갱신
           */
            notiAdapter.submitList(it)
        })

        /* "+"(fab_add_note) 버튼을 클릭하면 NoteCreateDialog 출력  */
        fab_add_note.setOnClickListener {
            NoteCreateDialog().show(supportFragmentManager, null)
        }
    }

    //종료시 job cencel
    override fun onDestroy() {
        job.cancel()
        super.onDestroy()
    }
}
