package com.example.mobileprogramming2.model

import android.arch.persistence.room.Database
import android.arch.persistence.room.Room
import android.arch.persistence.room.RoomDatabase
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