fun main() {
    var ob1 = SubClass()
    ob1.method1()
    ob1.method2()
}

open abstract class Super1 {
    fun method1() {
        println("Super method1 호출")
    }
    open abstract fun method2()
}

class SubClass: Super1() {
    override fun method2() {
        println("Super1의 method2() 오버라이딩")
    }
}s