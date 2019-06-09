package com.example.dbtest2.model

import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import android.content.Context

@Database(entities = [Item::class], version = 1)
abstract class ItemDB: RoomDatabase() {
    abstract fun itemDao(): ItemDao

    companion object {
        private var INSTANCE: ItemDB? = null

        fun getInstance(context: Context): ItemDB? {
            if (INSTANCE == null) {
                synchronized(ItemDB::class) {
                    INSTANCE = Room.databaseBuilder(context.applicationContext,
                        ItemDB::class.java, "item.db")
                        .fallbackToDestructiveMigration()
                        .build()
                }
            }
            return INSTANCE
        }

        fun destroyInstance() {
            INSTANCE = null
        }
    }
}