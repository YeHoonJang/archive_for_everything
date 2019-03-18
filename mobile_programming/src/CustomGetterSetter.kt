fun main(args: Array<String>) {
    val f1 = MyFriend()
    println("$(f1.name), $(f1.tel), $(f1.type)")
//    println("$f1.name, $f1.tel, $f1.type")c
    f1.name = "홍길동"
    f1.tel = "010-1234-5678"
    f1.type = 2
    println("$(f1.name), $(f1.tel), $(f1.type)")
//    println("$f1.name, $f1.tel, $f1.type")
}

// field 는 속성의 값을 가지고 있음
class MyFriend {
    var name: String = ""
    get() {
        println("name 속성의 게터 호출")
        if (field != "") return field
        else return "이름없음"
    }
    set(value) {
        field = value
        println("name 속성의 세터 호출 name = $field")
    }

    var tel: String = ""
        get() {
            println("tel 속성의 게터 호출")
            if (field != "") return field
            else return "전화번호 없음"
        }
        set(value) {
            field = value
            println("tel 속성의 세터 호출 tel = $field")
        }

    var type: Int = 4
        get() {
            println("type 속성의 게터 호출")
            return field
        }
        set(value: Int) {
            if(value>4) field = value
            else field = 4
            println("type 속성의 세터 호출 type = $field")
        }
}