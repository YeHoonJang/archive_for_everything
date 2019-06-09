package com.example.mobileprogramming.model

import android.arch.persistence.room.ColumnInfo
import android.arch.persistence.room.Entity
import android.arch.persistence.room.PrimaryKey

@Entity(tableName = "item")
class Item(@PrimaryKey(autoGenerate = true) var id: Long?,
           @ColumnInfo(name = "itemname") var itemName: String?,
           @ColumnInfo(name = "itemcount") var itemCount: Int
){

    constructor(): this(
        null,
        "",
        0
    )
}
