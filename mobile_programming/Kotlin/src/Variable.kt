fun main(args: Array<String>) {
    var a: Int = 100
    var b = 200
    var c: Int

    val d: Int = 0
    val e: String = "코틀린"

    println("a: " + a)
    println("b: $b")

    c = 1000
    println("c: ${c}")

    println("d: ${d}")
    println("e: ${e}")

    val s3 = "ture"
    val a7 = s3.toBoolean()

    println(a7)

    val s = """
        fun foo() {
        val x1 = 100
        val x2 = "kotlin"
        }
    """.trimIndent()

    println(s)
}