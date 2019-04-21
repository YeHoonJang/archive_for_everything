fun main() {
    val s1: String? = null
    val s4: String = "Kotlin"
    val s5: String? = s4

    var s6: Int? = null
    s6 = 100

    var s7: String? = "Kotlin"
    if (s7 != null) println(s7.length)
    println(s7?.length)

    var s8: String? = "코틀린을 배우자"
    println(s8?.substring(5))
    println(s8?.substring(5)?.length)

    if (s8 != null) {
        val b: String? = s8.substring(5)
        if (b != null) {
            println(b.length)
        }
    }

    val s9 = s8?.length ?: 0
    println("s9: $s9")


}