package com.example.coroutine

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        blockingTest()
    }

    fun blockingTest() {
        GlobalScope.launch {
            delay(1000L)
            println("World")
        }
        println("Hello,")
        Thread.sleep(1000L)
    }
}
