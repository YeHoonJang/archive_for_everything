fun main() {
    whenUsage(2, 50, "서울특별시")
    }

fun whenUsage(inputType: Int, score: Int, city: String) {
    when (inputType) {
        1 -> println("Type-1")
        2, 3 -> println("Tpye-2-3")
        else -> {
            println("Type-Unidentified")
        }
    }
    when(inputType) {
        checkInputType(inputType) -> {
            println("Type Normal")
        }
        else -> println("Type Abnormal")
    }
    val start = 0; val end = 100
    when(score) {
        in start..(end/4) -> println("be within 25%")
        50 -> println("average")
        in start..end -> println("be within range")
        else -> println("out of range")
    }

    val isSeoul = when(city) {
        is String -> city.startsWith("서울")
        else -> false
    }
    println(isSeoul)

    when {
        city.length == 0 -> println("도시명을 입력하세요")
        city.substring(0, 2).equals("서울") -> println("city : $city")
        else -> println(city)
    }
}

fun checkInputType(inputType: Int) : Int {
    if (inputType >= 1 && inputType <= 3) {
        return inputType
    }
    return -1
}

