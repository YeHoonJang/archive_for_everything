package com.example.restapiex01.local

import android.os.Bundle
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.NavUtils
import androidx.recyclerview.widget.LinearLayoutManager
import kotlinx.android.synthetic.main.activity_result.*
import com.example.restapiex01.R
import com.example.restapiex01.database.DatabaseModule
import com.example.restapiex01.result.ResultAdapter

//메인화면의 리사이클러뷰에서 검색한 아이템을 클릭하면, 상세정보를 표시하는 액티비티
class LocalDbSearchActivity : AppCompatActivity() {
    /* 데이터베이스를 가져옵니다.*/
    val database by lazy {
        DatabaseModule.getDatabase(this)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        /* ActionBar에 뒤로가기("<-") 버튼 표시 설정
           - ActionBar에 표시만 되고 뒤로가기 액션은 이뤄지지 않음.
             따라서 onOptionsItemSelected 콜백 메서드에서 뒤로가기 로직을 구현해야 함
         */
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        Log.i("SAVE ID DATA", intent.getLongExtra("saveId", 0).toString())

        //saveId로 쿼리(loadFreshData)하여 상세정보를 saveList에 할당
        val saveList = database.freshDao().loadFreshData(intent.getLongExtra("saveId", 0))

        Log.i("SAVE COUNTS", saveList.count().toString())

        /* 리사이클러뷰에 어댑터 및 레이아웃메니저 설정
           - activity_result.xml
        */
        recycle_reesult.adapter = ResultAdapter(ArrayList(saveList))
        recycle_reesult.layoutManager = LinearLayoutManager(this)
    }


    /* actionbar에 delete 버튼을 만들어줍니다. */
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_localdb_delete_actionbar, menu)
        return true
    }

    /* Actionbar에서 삭제 아이템을 클릭하면 검색한 경락가격정보를 DB에서 삭제하는 콜백함수 */
    override fun onOptionsItemSelected(item: MenuItem?): Boolean {
        //클릭한 아이템이 삭제 아이템(delete_item)이면
        if (item?.itemId == R.id.delete_item) {
            /* saveList 데이터를 삭제합니다.*/
            database.freshDao().deleteSaveData(intent.getLongExtra("saveId", 0))
            finish()
        }

        // ActionBar 뒤로가기 로직을 구현
        when (item?.groupId){
            android.R.id.home -> {
                NavUtils.navigateUpFromSameTask(this)
            }
            else -> {
                return super.onOptionsItemSelected(item)
            }
        }
        return true
    }
}
