package com.example.dbtest2.model

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "item")
class Item(@PrimaryKey(autoGenerate = true) var id: Long?,
           @ColumnInfo(name = "itemname") var itemName: String?,
           @ColumnInfo(name = "itemcount") var itemCount: Int
){
    constructor():this(null, "", 0)
}