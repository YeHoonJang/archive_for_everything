package com.example.restapiex01.database


import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import com.example.restapiex01.model.FreshDao
import com.example.restapiex01.model.FreshData
import com.example.restapiex01.model.SaveItem


/* 데이터베이스 클래스 선언
  - 데이터베이스의 구조가 바뀌면 Version이 바뀌어야합니다.
  - 선언된 데이터베이스 엔티티들을 entitries 어노테이션으로 가져옵니다.*/
@Database(entities = [FreshData::class, SaveItem::class], version = 4)
abstract class DatabaseModule : RoomDatabase() {

    /* Query 문에 사용하는 Dao들을 가져옵니다. */
    abstract fun freshDao(): FreshDao


    /* Companin Onject는 클래스의 static한 데이터를 선언하는 영역으로 싱글톤으로 사용할
       인스턴스를 메모리에 저장하거나 전역으로 이용할 변수등을 선언합니다.*/
    companion object {
        // database 변수 선언
        private var database: DatabaseModule? = null
        //database 이름 상수 선언
        private const val ROOM_DB = "room.db"

        /* 정의한 Database 객체를 가져오는 함수 선언 */
        fun getDatabase(context: Context): DatabaseModule {
            if (database == null) {
                database = Room.databaseBuilder(
                    context.applicationContext,
                    DatabaseModule::class.java, ROOM_DB
                    /*원칙적으로 메인쓰레드에서는 Room을 사용할 수 없지만 실습을 위해 허가합니다.*/
                ).allowMainThreadQueries().fallbackToDestructiveMigration().build()
            }
            /* 안전한 강제 캐스팅 */
            return database!!
        }
    }
}