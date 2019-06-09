package com.example.dbtest.model

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy.REPLACE
import androidx.room.Query

@Dao
interface  ItemDao {
    @Query("SELECT * FROM item")
    fun getAll(): List<Item>

    @Insert(onConflict = REPLACE)
    fun insert(item: Item)

    @Query("DELETE FROM item")
    fun deleteAll()
}