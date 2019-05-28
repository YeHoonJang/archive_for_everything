package com.example.restapiex01.model


import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.PrimaryKey

@Entity(
    tableName = "Fresh",
    foreignKeys = arrayOf(
        ForeignKey(
            /*같이 삭제되도록 합니다.*/
            onDelete = ForeignKey.CASCADE,
            entity = SaveItem::class,
            parentColumns = arrayOf("id"),
            childColumns = arrayOf("saveId")
        )
    )
)

data class FreshData(

    @PrimaryKey(autoGenerate = true)
    var id: Long? = null,
    var saveId: Long? = null,
    var grade: String,
    var date: String,
    var gongpanName: String,
    var maxPrice: Int,
    var minPrice: Int,
    var tradeAmt: Int
)

//1:M
// foreign key

@Entity(tableName = "SaveItem")
data class SaveItem(

    @PrimaryKey(autoGenerate = true)
    var id: Long? = null,

    var saveTitle: String
)