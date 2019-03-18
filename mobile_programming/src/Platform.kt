fun main(args: Array<String>) {
    printJavaClass(JavaClass("platform type test!!"))
    printJavaClass(JavaClass(null))

}

fun printJavaClass(jClass: JavaClass) {
//    println(jClass.platformVar.toUpperCase())
    println((jClass.platformVar ?: "It is null!!").toUpperCase())
}
