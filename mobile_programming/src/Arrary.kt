fun main(args: Array<String>) {
    val item = arrayOf("사과", "복숭아", "배")
    for (fruit in item) {
        println("fruit: $fruit")
    }
    println()

    val arr1 = arrayOfNulls<Int>(3)
    arr1[0] = 10
    arr1[1] = 20
    arr1[2] = 30
    for (i in arr1) {
        print("$i, ")
    }

    val arr2 = arrayOfNulls<String>(3)
    for (value in arr2) {
        print("$value, ")
    }
    println()

    arr2[0] = "Kotlin"
    arr2[1] = "Java"
    arr2[2] = "Swift"
    for (value in arr2) {
        println("arr2: $value")
    }
    println()

    val num = Array<Int>(10, {i -> i})
    for (value in num) {
        print("$value ")
    }
    println()

    val num2 = Array<String>(10, {i -> (i*2).toString()})
    for (value in num2) {
        print("$value ")
    }
    println()

    val num3 = Array(10) {i -> 0}
    num3.forEach{print("$it, ")}
    println()

    val intArray = arrayOf(arrayOf(0,0,0), arrayOf(0,0,0))
    for (x in 0..intArray.size-1) {
        for(y in 0..intArray[x].size-1) {
            print("${intArray[x][y]}")
        }
    }
    println()

 }