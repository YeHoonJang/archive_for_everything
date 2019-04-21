fun main(args: Array<String>) {
    val userID: String? = getUserID()
//    var str: String = "hi"

    if (userID != null) sendNotification(userID)

    userID?.let { userID -> sendNotification(userID) }

    userID?.let { sendNotification(it) }

    userID.let {
        println("$userID 님에게 알림 메시지를 보냈습니다.")
        println("$it 님에게 알림 메시지를 보냈습니다.")
    }
}

fun getUserID(): String {
    return "user01"
}

fun sendNotification(userID: String) {
    println("$userID 님에게 알림 메시지를 보냈습니다.")
}