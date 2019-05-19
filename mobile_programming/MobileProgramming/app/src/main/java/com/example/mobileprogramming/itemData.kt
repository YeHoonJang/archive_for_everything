package com.example.mobileprogramming

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

enum class ItemData(val itemType: Int, val itemContent:ItemContent) {
    ITEM1(RecyclerAdapter.ITEM, ItemContent(R.drawable.umbrella, "우산", "3개 남음")),
    ITEM2(RecyclerAdapter.ITEM, ItemContent(R.drawable.calculator, "공학용 계산기", "5개 남음"))
}