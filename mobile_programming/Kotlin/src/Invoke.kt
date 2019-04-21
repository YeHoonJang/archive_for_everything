fun main(args: Array<String>) {
    val obj1 = Person("홍길동")
    obj1("010-1234-5678", "hong999@gmail.com")
}
class Person(val name: String) {
    operator fun invoke(phone: String, email: String) {
        println(" name: $name\n phone: $phone\n email: $email")
    }
}