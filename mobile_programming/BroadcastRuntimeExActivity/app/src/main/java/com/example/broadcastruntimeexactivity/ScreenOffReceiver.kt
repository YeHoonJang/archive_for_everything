package com.example.broadcastruntimeexactivity

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log
import android.widget.Toast

class ScreenOffReceiver : BroadcastReceiver() {

    override fun onReceive(context: Context, intent: Intent) {
        when {
            intent?.action == Intent.ACTION_SCREEN_OFF -> {
                Log.d("BROADCAST", "화면이 OFF 되었습니다.")
                Toast.makeText(context, "화면이 OFF 되었습니다.", Toast.LENGTH_LONG).show()
            }
        }
    }
}
