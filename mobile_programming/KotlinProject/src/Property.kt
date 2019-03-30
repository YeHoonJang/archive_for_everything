//fun main(args: Array<String>) {
//    var result = f1(100, 100)
//    println(result)
//}
//
//fun f1 (a1: Int, a2: Int): Int {
//    var count = a1+ a2 //필드s
//    return count
//}

fun main(args: Array<String>) {
    val result = MyCalcu(100, 200)
    println(result.sum)
}

class MyCalcu constructor(_p1: Int, _p2: Int) {
    var p1: Int
    var p2: Int
    val sum: Int

    init {
        this.p1 = _p1
        this.p2 = _p2
        sum = p1 + p2
    }
}