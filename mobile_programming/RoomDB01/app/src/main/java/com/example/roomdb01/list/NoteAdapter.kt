package com.example.roomdb01.list


import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.paging.PagedListAdapter
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.list_item_note.view.*
import kotlinx.coroutines.*
import com.example.roomdb01.R
import com.example.roomdb01.dialog.NoteUpdateDialog
import com.example.roomdb01.room.Note
import com.example.roomdb01.room.NoteDao

/* NoteAdapter 선언
  - PagedListAdapter: 페이징을 처리하기 위한 RecyclerView.Adapter
  - PagedListAdapter는 PagedList를 들고있고, 다음 데이터가 필요하면 PagedList에 요청합니다.
    또한 불러온 데이터의 중복을 검사합니다.
    DiffUtil에 기준을 정의해 PagedListAdapter의 Consturstor에 넘겨주면,
    기준에 걸리는 중복 아이템은 UI에 보여주지 않습니다.
 */
class NoteAdapter(val job: Job, val noteDao: NoteDao) : PagedListAdapter<Note, NoteAdapter.ItemViewHolder>(DIFF_CALLBACK) {

    //뷰홀더에 데이터를 바인딩
    override fun onBindViewHolder(holder: NoteAdapter.ItemViewHolder, position: Int) {
        //뷰홀더에 데이터를 바인딩하는 bindItems() 메서드 호출
        holder.bindItems(getItem(position))
    }

    /*뷰홀더 생성하여 반환*/
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.list_item_note, parent, false)

        /* 뷰를 데이터와 맵핑하기위해 생성한 뷰홀더를 반환*/
        return ItemViewHolder(itemView)
    }

    /* ItemViewHolder 클래스 선언
       - itemView를 인자로 받아 mapping
    */
    inner class ItemViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        /* bindItems() 함수 선언
           - 데이터 바인딩
         */
        fun bindItems(note: Note?) {
            /* note가 있을 경우에만 바인딩 */
            note?.let {
                /* itemView(list_item_note.xml)의 txt_note_content 뷰에
                   note 테이블의 noteContent 컬럼값을 표시
                 */
                itemView.txt_note_content.text = it.noteContent

                /* "수정" 버튼 클릭시 업데이트 */
                //NoteUpdateDialog
                itemView.btn_update_note.setOnClickListener { _ ->
                    //추가/수정 다이얼로그 생성
                    val dialog = NoteUpdateDialog().apply {
                        arguments = Bundle().apply { putInt("NOTE_KEY",it.noteIdx!!) }
                    }

                    //프래그먼트 다이얼로그(NoteUpdateDialog) 출력
                    dialog.show((itemView.context as AppCompatActivity).supportFragmentManager, null)
                }

                /* "삭제" 버튼 클릭시 삭제 */
                itemView.btn_delete_note.setOnClickListener { _ ->

                    /* 메인쓰레드로 런쳐를 시작합니다. */
                    GlobalScope.launch(Dispatchers.Main + job) {
                        /* 데이터베이스에서 해당 row를 삭제하는 suspend 함수(deleteNoteFromDao) 호출
                          - 삭제작업은 IO 쓰레드에서 수행
                       */
                        deleteNoteFromDao(it)
                        /* 다시 메인쓰레드로 돌아오면 데이터를 넣거나 혹은 dismiss하는 UI작업을 합니다. */
                        Toast.makeText(itemView.context, "데이터가 삭제되었습니다.", Toast.LENGTH_SHORT).show()
                    }
                }
            }
        }
    }

    /* 데이터베이스의 해당 row 삭제를 위한 suspend 함수(deleteNoteFromDao) 선언
       - withContext coroutine builder를 사용하여 삭제 작업을 IO스레드에서 수행하도록 설정
     */
    suspend fun deleteNoteFromDao(note: Note) = withContext(Dispatchers.IO + job) {
        // 데이터베이스에서 해당 row 삭제
        noteDao.deleteNots(note)
    }

    /* final static으로 데이터를 비교하는  RecyclerView DiffUtil 클래스 구현
       - DiffUtil 클래스는 두 목록간의 차이점을 찾고 업데이트 되어야 할 목록을 반환
         (기존에 PagedList 가 존재하면 그 차이를 비교한 후 리사이클러뷰를 새로운 페이지로 갱신)
       - RecyclerView 어댑터에 대한 업데이트를 알리는데 사용
       - areItemsTheSame() : 두 객체가 같은 항목인지 여부를 결정
       - areContentsTheSame() : 두 항목의 데이터가 같은지 여부를 결정
       - 기존:  1,3,5,6
       - 현재:  1,2,3,5,6
     */
    companion object {
        private val DIFF_CALLBACK = object : DiffUtil.ItemCallback<Note>() {
            override fun areItemsTheSame(oldConcert: Note, newConcert: Note): Boolean = oldConcert.noteIdx == newConcert.noteIdx
            override fun areContentsTheSame(oldConcert: Note, newConcert: Note): Boolean = oldConcert.noteContent == newConcert.noteContent
        }
    }
}
