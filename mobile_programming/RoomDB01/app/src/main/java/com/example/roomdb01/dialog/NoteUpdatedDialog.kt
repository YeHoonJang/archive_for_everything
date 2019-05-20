package com.example.roomdb01.dialog


import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.DialogFragment
import kotlinx.android.synthetic.main.dialog_note_create.view.*
import kotlinx.coroutines.*
import com.example.roomdb01.R
import com.example.roomdb01.room.AppDatabase
import com.example.roomdb01.room.Note

//Update 다이얼로그 프래그먼트
class NoteUpdateDialog : DialogFragment() {

    /* Lazy 키워드를 이용하여 처음 호출될때 초기화하도록 설정 */
    //job
    private val job by lazy { Job() }
    //noteDao
    private val noteDao by lazy { AppDatabase.getDatabase(requireContext()).noteDao() }
    //noteId
    private val noteId by lazy {
        arguments?.getInt("NOTE_KEY") ?: throw IllegalArgumentException("전달받은 Note값이 없습니다.")
    }

    /* 추가/수정 다이얼로그 위한 레이아웃(dialog_note_create.xml) inflate */
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return inflater.inflate(R.layout.dialog_note_create, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        /* 메인쓰레드로 런쳐를 시작합니다. */
        GlobalScope.launch(Dispatchers.Main + job) {
            /* 쓰레드를 바꾸어 데이터를 조회합니다.. */
            val noteResult = withContext(Dispatchers.IO) { noteDao.selectNote(noteId) }
            //조회한 데이터를 해당 뷰에 표시
            view.edit_new_note.setText(noteResult.noteContent)
        }

        /* 업데이트 버튼 누른경우*/
        view.btn_new_note.setOnClickListener {

            /* update 작업을 위한 코루틴 수행
               - withContext() 빌드를 이용하여 스레드를 io 바꾸어 update 작업 수행
             */
            GlobalScope.launch(Dispatchers.Main + job) {
                withContext(Dispatchers.IO) { noteDao.updateNote(
                    Note(noteIdx = noteId,
                        noteContent = view.edit_new_note.text.toString())
                ) }
                dismiss()//다이얼로그 종료
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        job.cancel()//코루틴 cancel
    }
}