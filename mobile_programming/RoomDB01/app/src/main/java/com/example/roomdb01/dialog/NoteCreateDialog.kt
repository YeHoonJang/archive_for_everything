package com.example.roomdb01.dialog


import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.DialogFragment
import kotlinx.android.synthetic.main.dialog_note_create.*
import kotlinx.android.synthetic.main.dialog_note_create.view.*
import kotlinx.coroutines.*
import com.example.roomdb01.R
import com.example.roomdb01.room.AppDatabase
import com.example.roomdb01.room.Note

//Create 다이얼로그 프래그먼트
class NoteCreateDialog : DialogFragment() {

    /* Lazy 키워드를 이용하여 처음 호출될때 초기화하도록 설정 */
    //job
    private val job by lazy { Job() }
    //noteDao
    private val noteDao by lazy { AppDatabase.getDatabase(requireContext()).noteDao() }

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        /* 추가/수정 다이얼로그 위한 레이아웃(dialog_note_create.xml) inflate */
        val rootView = inflater.inflate(R.layout.dialog_note_create, container, false)

        /* 추가/수정 버튼 클릭시 데이터베이스에 값을 저장하는 이벤트 처리 */
        rootView.btn_new_note.setOnClickListener {

            /* 메인쓰레드로 런쳐를 시작합니다. */
            GlobalScope.launch(Dispatchers.Main + job) {
                /* 쓰레드를 바꾸어 데이터를 데이터베이스에 insert 합니다. */
                createNote(Note(noteContent = edit_new_note.text.toString()))
                /* 다시 메인쓰레드로 돌아오면 데이터를 넣거나 혹은 dismiss(다이얼로그 종료)하는 UI작업을 합니다. */
                Toast.makeText(requireContext(), "데이터가 저장되었습니다.", Toast.LENGTH_SHORT).show()
                dismiss()//다이얼로그 종료
            }

        }
        return rootView
    }

    /* 데이터베이스에 insert 작업을 위한 suspend 함수(createNote) 선언
       - withContext coroutine builder를 사용하여 insert 작업을 IO스레드에서 수행하도록 설정
     */
    suspend fun createNote(note: Note) = withContext(Dispatchers.IO + job) {
        noteDao.insertNotes(note)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        job.cancel()//job cancel
    }
}