package com.example.roomdb01.room


import androidx.room.Entity
import androidx.room.PrimaryKey

/* Entity Annotation으로 테이블 정의
   - Entity 어노테이션을통해 테이블에 들어갈 row 를 정의합니다.
   - tableName은 생략가능합니다.(생략할경우 data class의 이름이 tablename이 됩니다.)
 */
@Entity(tableName = "Note")
data class Note(

    /*복합 Primary Key를 사용하는경우 이때 프라이머리키와 변수선언자의 이름이 동일해야합니다.*/
    //@Entity(primaryKeys = arrayOf("firstName", "lastName"))

    /* Primary Key를 직접 설정하는경우 */
    //@PrimaryKey
    //var ExName: String,

    /* Primary Key를 자동 생성
       - PrimaryKey Annotation으로 Primary Key 정의.
       - 이때 반드시 Long 혹은 Int 타입이여합니다.
   */
    @PrimaryKey(autoGenerate = true)
    var noteIdx: Int? = null,


    /*칼럼명을 별도로 주는 경우*/
    //@ColumnInfo(name = "note_content")
    //val NoteContent: String

    /* 칼럼명을 별도로 주지 않으면 변수명을 칼럼명으로 사용합니다.*/
    val noteContent: String


    /* ignore은 데이터베이스에 저장하지 않습니다.*/
    //@Ignore
    //var picture: Bitmap?
)