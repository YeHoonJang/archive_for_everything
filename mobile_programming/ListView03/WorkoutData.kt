package kr.ac.gachon.ugkang.listview03

enum class WorkoutData(val workName: String, val firstImage: Int, val secondImage: Int) {
    WORKOUT1("[1] 점핑잭", R.drawable.workout11, R.drawable.workout12),
    WORKOUT2("[2] 스쿼드", R.drawable.workout21, R.drawable.workout22),
    WORKOUT3("[3] 잭킷", R.drawable.workout31, R.drawable.workout32),
    WORKOUT4("[4] 스탠드 앤 점프", R.drawable.workout41, R.drawable.workout42),
    WORKOUT5("[5] 사이드니킥", R.drawable.workout51, R.drawable.workout52),
    WORKOUT6("[6] 크로스 핸드 점핑잭", R.drawable.workout61, R.drawable.workout62),
    WORKOUT7("[7] 브릿지", R.drawable.workout71, R.drawable.workout72),
    WORKOUT8("[8] 로우어 바디 크런치", R.drawable.workout81, R.drawable.workout82),
    WORKOUT9("[9] 스트레칭", R.drawable.workout91, R.drawable.workout92)
}