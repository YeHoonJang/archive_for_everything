package com.example.restapiex01.model

/* Fruits enum class
   - 과일 상수명(과일명, 중분류코드)
 */
enum class Fruits(val holder: String, val mcode: String) {

    APPLE("사과", "0601"),
    PEAR("복숭아", "0602"),
    GRADPE("포도", "0603"),
    PEACK("복숭아", "0604"),
    PERSIM("단감", "0605"),
    FLICKPERSIM("떪은감", "0606"),
    DRYPERSIM("곶감", "0607"),
    PLUM("자두", "0608"),
    QUINCE("모과", "0609"),

}