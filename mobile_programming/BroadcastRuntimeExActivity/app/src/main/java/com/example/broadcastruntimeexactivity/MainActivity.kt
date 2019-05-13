package com.example.broadcastruntimeexactivity

import android.content.Intent
import android.content.IntentFilter
import android.support.v7.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {

    var screenOffReceiver : ScreenOffReceiver?= null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (screenOffReceiver == null) {
            screenOffReceiver = ScreenOffReceiver()
            var intentFilter = IntentFilter(Intent.ACTION_SCREEN_OFF)

            registerReceiver(screenOffReceiver, intentFilter)
        }
    }
}
