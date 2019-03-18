fun main(args: Array<String>) {
    val cl = Child("검정", "검정")
    println("Child: ${cl.hairColor}, ${cl.eyeColor}")

    cl.hairColor = "파랑"
    println("Child: ${cl.hairColor}, ${cl.eyeColor}")
}

open class Father(var hairColor: String, var eyeColor: String)

class Child: Father {
    constructor(hairColor: String, eyeColor:String) : super(hairColor, eyeColor) {
        this.hairColor = hairColor
        this.eyeColor = eyeColor
    }
}   