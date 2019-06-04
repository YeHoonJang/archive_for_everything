package com.example.mobileprogramming.list_reservation

import com.example.mobileprogramming.R

interface ListItem2 {
    val imageId: Int
    val itemName: String
    val itemAmount: String
}

data class ItemContent2(
    override val imageId: Int,
    override val itemName: String,
    override val itemAmount: String
) : ListItem2

enum class ItemDataReservation(val itemType: Int, val itemContent: ItemContent2) {
    ITEM1(
        RecyclerAdapter_reservation.ITEM,
        ItemContent2(
            R.drawable.umbrella,
            "우산",
            "3명 대기"
        )
    ),
    ITEM2(
        RecyclerAdapter_reservation.ITEM,
        ItemContent2(
            R.drawable.calculator,
            "공학용 계산기",
            "5명 대기"
        )
    )
}