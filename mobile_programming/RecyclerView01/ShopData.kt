package kr.ac.gachon.ugkang.recyclerview01

//ShopContent interface
interface ShopContent {
    val imageId: Int
}

//ShopBanner data class 선언(ShopContent 인터페이스 구현)
data class ShopBanner(
    override val imageId: Int
) : ShopContent

//ShopItem data class 선언(ShopContent 인터페이스 구현)
data class ShopItem(
    override val imageId: Int,
    val itemName: String,
    val itemPrice: Int
) : ShopContent

/* RecyclerView의 item에 사용할 enum class 선언
   - shopType: BANNER, ITEM 구분
   - shopContent: item 컨텐츠(ShopBanner 또는 ShopItem)
 */
enum class ShopData(val shopType: Int, val shopContent: ShopContent) {
    SHOP_ITEM1(ShopRecyclerAdapter.BANNER, ShopBanner(R.drawable.banner_1)),
    SHOP_ITEM2(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop1, "샐러드", 2000)),
    SHOP_ITEM3(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop2, "닭가슴살", 2500)),
    SHOP_ITEM4(ShopRecyclerAdapter.BANNER, ShopBanner(R.drawable.banner_2)),
    SHOP_ITEM5(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop3, "한과", 1500)),
    SHOP_ITEM6(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop4, "새우요리", 1700)),
    SHOP_ITEM7(ShopRecyclerAdapter.BANNER, ShopBanner(R.drawable.banner_3)),
    SHOP_ITEM8(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop5, "과자", 2000)),
    SHOP_ITEM9(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop6, "과일주스", 1500)),
    SHOP_ITEM10(ShopRecyclerAdapter.BANNER, ShopBanner(R.drawable.banner_4)),
    SHOP_ITEM11(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop7, "사골육계장", 5000)),
    SHOP_ITEM12(ShopRecyclerAdapter.ITEM, ShopItem(R.drawable.shop8, "자몽", 2000));
}