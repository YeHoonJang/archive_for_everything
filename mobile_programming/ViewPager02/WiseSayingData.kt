package kr.ac.gachon.ugkang.viewpager02

enum class WiseSayingData(val wiseText: String, val writer: String, val colorId: Int) {
    RED("변화에서 가장 힘든 것은 새로운 것을 생각해내는 것이 아니라 이전에 가지고 있던 틀에서 벗어나는 것이다.", "존메이너드 케인즈", R.color.redCategory),
    BLUE("30분을 티끌과 같은 시간이라고 말하지 말고 그동안이라도 티끌과 같은 일을 처리하는 것이 현명한 방법이다.", "괴테", R.color.blueCategory),
    GREEN("인생이 힘들다고? 그렇지 않다! 우여곡절도 겪고 발버둥치기도 하며 항상 가난했지만 그럴만한 가치가 있었다.", "윌리엄 서머셋", R.color.greenCategory),
    YELLOW("꽃에 향기가 있듯 사람에겐 품격이 있다. 꽃이 싱싱할 때 향기가 신선하듯이 사람도 마음이 밝을 때 품격이 고상하다 .", "섹스피어", R.color.yellowCategory),
    VIOLET("오늘 배우지 아니하고서 내일이 있다고 말하지 말며, 올해에 배우지 아니하고서 내년이 있다고 말하지 말라.", "명신보감", R.color.violetCategory),
    DEEPBLUE("우리는 성공보다 실패를 통해 더 많은 것을 배운다. 하지 말아야 할 것을 발견함으로써 해야할 것을 발견한다.", "밀턴", R.color.deepBlueCategory),
    LIGHTBLACK("인간은 항상 시간이 모자란다고 불평을 하면서 마치 시간이 무한정 있는 것처럼 행동한다..", "세네카", R.color.lightBlackCategory)
}