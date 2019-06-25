package com.example.mobileprogramming2.model

import android.arch.persistence.room.ColumnInfo
import android.arch.persistence.room.Entity
import android.arch.persistence.room.PrimaryKey

@Entity(tableName = "item")
class Item(@PrimaryKey(autoGenerate = true) var id: Long?,
           @ColumnInfo(name = "itemname") var itemName: String?,
           @ColumnInfo(name = "itemamount") var itemAmount: Int
){
    constructor():this(null, "", 0)
}