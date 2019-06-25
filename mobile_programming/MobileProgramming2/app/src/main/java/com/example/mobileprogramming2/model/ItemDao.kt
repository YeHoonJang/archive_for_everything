package com.example.mobileprogramming2.model

import android.arch.persistence.room.Dao
import android.arch.persistence.room.Insert
import android.arch.persistence.room.Query
import android.arch.persistence.room.OnConflictStrategy.REPLACE

@Dao
interface  ItemDao {
    @Query("SELECT * FROM item")
    fun getAll(): List<Item>

    @Insert(onConflict = REPLACE)
    fun insert(item: Item)

    @Query("DELETE FROM item")
    fun deleteAll()
}