package com.example.roomdb01.room


import androidx.paging.DataSource
import androidx.room.*

/* DAO(Database Access Object) 정의
   - 데이터베이스에 엑세스하는데 사용되는 메소드(insert, query, update, delete) 선언
*/
@Dao
interface NoteDao {

    /* Insert Annotation으로 Insert를 정의
       - key 중복시 Strategy 설정
       - 파라미터로 객체 그대로를 넘깁니다. 값 매칭은 Room이 인스턴스 변수를 보고 알아서 해줌
     */
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insertNotes(vararg notes: Note)

    /* Query Annotation으로 쿼리를 정의한다.
       - 파라미터로 전달할 값을 : 기호 다음에 같은 이름으로 선언한다.
       - FROM 절로 넘긴 테이블과 매칭되는 모델로 반환값을 선언하면 알아서 맞는 객체로 매핑해준다
    */
    /* DataSource.Factory<Int, Note> : DataSource를 감싸 LivePagedListBuilder 로 반환
       - DataSource: Network, Memory, DB로 부터 페이징 데이터를 질의하는 역할의 추상 클래스
       - DataSource는 Local 또는 Network에서 Page 단위로 데이터를 가져옵니다.
       - PageKeyedDataSource, ItemKeyedDataSource, PositionalDataSource 3가지가 있으며,
         키 속성에 따라 맞는 클래스를 상속받아 쿼리를 구현해야 합니다.
       - Room을 사용하면 반환 타입을 DataSource를 하여 PositionalDataSource를 자동으로 생성할 수 있습니다.
    */
    @Query("SELECT * FROM Note")
    fun selectNotes(): DataSource.Factory<Int, Note>

    /* Query Annotation으로 쿼리를 정의한다.
       - 파라미터로 전달할 값을 : 기호 다음에 같은 이름으로 선언한다(:noteIdx)
       - FROM 절로 넘긴 테이블과 매칭되는 모델로 반환값을 선언하면 알아서 맞는 객체로 매핑해준다
     */

    @Query("SELECT * FROM Note WHERE noteIdx = :noteIdx")
    fun selectNote(noteIdx: Int): Note

    /* Update Annotation으로 Update를 정의
      - 파라미터로 객체 그대로를 넘기면, 값 매칭은 Room이 인스턴스 변수를 보고 알아서 해줍니다.
    */
    @Update
    fun updateNote(vararg notes: Note)

    /*Delete Annotation으로 Delete를 정의
     - 파라미터로 객체 그대로를 넘기면, 값 매칭은 Room이 인스턴스 변수를 보고 알아서 해줍니다.
   */
    @Delete
    fun deleteNots(vararg note: Note)
}


//    /* onConflicStrategy란 중복된 Primary Key가 있을때 어떻게 할지에 대한 내용입니다.*/
//    @Insert(onConflict = OnConflictStrategy.REPLACE)
//    fun insertNote(note: Note): Long?
//
//    /* insert문인데 return이 없는경우 */
//    @Insert(onConflict = OnConflictStrategy.REPLACE)
//    fun insertNote(note: Note)
//
//    @Insert(onConflict = OnConflictStrategy.REPLACE)
//    fun insertNotes(vararg notes: Note): Array<Long>
//
//    @Update(onConflict = OnConflictStrategy.REPLACE)
//    fun updateNotes(vararg note: Note): Int
//
//    @Delete
//    fun deleteNotes(vararg notes: Note): Int
//
//    @Query("SELECT * FROM note WHERE updatedAt >= :arg0")
//    fun findNotesByDate(updatedAt: Date): List<Note>
//
//    @Query("SELECT id, text, isDone FROM note ORDER BY updatedAt ASC")
//    fun findAllResumedNotesFilteredByUpdateDate(): List<Note.Resumed>
//
//    @Query("SELECT id, text, isDone FROM note WHERE isDone == 1 ORDER BY updatedAt ASC")
//    fun findAllResumedNotesNotDoneFilteredByUpdateDate(): List<Note.Resumed>
//
//    @Query("SELECT * FROM note ORDER BY isDone, updatedAt DESC")
//    fun findAllNotesGroupedByDoneStatus(): List<Note>
//
//    @Query("SELECT * FROM note WHERE id = :arg0 LIMIT 1")
//    fun findById(id: Long?): Note