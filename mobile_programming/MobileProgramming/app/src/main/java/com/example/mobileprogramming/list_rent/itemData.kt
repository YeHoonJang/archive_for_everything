package com.example.mobileprogramming.list_rent

import com.example.mobileprogramming.R

/*
interface ListItem {
    val imageId: Int
    val itemName: String
    val itemAmount: String
}

data class ItemContent(
    override val imageId: Int,
    override val itemName: String,
    override val itemAmount: String
) : ListItem
*/

/*
enum class ItemDataRent(val itemType: Int, val itemContent:ItemContent) {
    ITEM1(ListviewAdapterRent.ITEM, ItemContent(R.drawable.umbrella, "우산", "3개 남음")),
    ITEM2(ListviewAdapterRent.ITEM, ItemContent(R.drawable.calculator, "공학용 계산기", "5개 남음"))
}
*/

enum class ItemDataRent(val imageId: Int, val itemName: String, val itemAmount: String) {
    Item1(R.drawable.umbrella, "우산", "3개 남음"),
    Item2(R.drawable.calculator, "공학용 계산기", "5개 남음")
}