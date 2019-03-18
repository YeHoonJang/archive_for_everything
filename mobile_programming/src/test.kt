fun main(args: Array<String>) {
    var sub1 = SubClass()
    println("sub1.subMember : $(sub1.subMember)")
    sub1.subMethod()

    println("===========================")

    println("sub1.superMember : $(sbu1.superMember)")
    sub1.superMethod()
}

open class SuperClass {
    var superMember = 100
    fun superMethod() {
        println("Super Class Method 호출")
    }
}

class SubClass: SuperClass {
    constructor() : super()
    
    var subMember = 200
    fun subMethod() {
        println("Sub Class Method 호출")
    }
}