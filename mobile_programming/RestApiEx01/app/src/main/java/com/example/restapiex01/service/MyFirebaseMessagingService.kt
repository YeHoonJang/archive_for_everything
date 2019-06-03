package com.example.restapiex01.service

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.media.RingtoneManager
import android.os.Build
import android.util.Log
import androidx.core.app.NotificationCompat
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage
import com.example.restapiex01.R
import com.example.restapiex01.main.MainActivity

class MyFirebaseMessagingService : FirebaseMessagingService() {

    /* 푸시 알림 메시지를 받으면 호출되는 콜백 메서드
       - 받은 알림 메시지(FCM 푸시 알림 메시지)를 앱 자체에서 알림을 표시하기 위한 코드 작성
     */
    override fun onMessageReceived(remoteMessage: RemoteMessage?) {
        super.onMessageReceived(remoteMessage)

        Log.d(TAG, "From: ${remoteMessage?.from}")

        // Check if message contains a notification payload.
        remoteMessage?.notification?.let {
            Log.d(TAG, "Message Notification Body: ${it.body}")

            //앱 자체에서 알림 표시를 위한 함수 호출
            sendNotification(it.body!!)
        }
    }

    /* 앱 자체에서 알림 표시를 위한 함수 선언
       - pendingIntent: notification을 MainActivity의 상태알림창에 띄울 인텐트
       - notificationManager: notification(상태알림창의 알림)을 사용하기 위한 객체
       - notificationBuilder: Notification 내용을 설정하기 위한 빌더(빌더 생성)
     */
    private fun sendNotification(messageBody: String) {
        /* intent 생성 및 플래그 설정
           - FLAG_ACTIVITY_CLEAR_TOP : 스택에 기존에 사용하던 Activity가 있다면 그 위의 스택을 전부 제거
         */
        val intent = Intent(this, MainActivity::class.java)
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP)

        /* notification을 MainActivity의 상태알림창에 띄울 pendingIntent 선언
           - getActivity(Context, int, Intent, int): Activity를 시작하는 인텐트를 생성
           - PendingIntent.FLAG_ONE_SHOT : 1회용 PendingIntent
         */
        val pendingIntent = PendingIntent.getActivity(this, 0 /* Request code */, intent,
            PendingIntent.FLAG_ONE_SHOT)

        //오레오 버전부터는 사용자가 channel을 통해 Notification을 관리할 수 있기 때문에 반드시 선언해야 함
        val channelId = getString(R.string.default_notification_channel_id)
        //알림 Sound 설정
        val defaultSoundUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION)

        /* Notification 빌더를 이용하여 Notification 내용을 설정(빌더 생성) */
        val notificationBuilder = NotificationCompat.Builder(this, channelId)
            .setSmallIcon(R.drawable.ic_notification_event)
            .setContentTitle(getString(R.string.fcm_message))//제목설정
            .setContentText(messageBody)//내용 설정
            .setAutoCancel(true)
            .setSound(defaultSoundUri)
            .setContentIntent(pendingIntent)

        // Notification 서비스 객체 가져오기
        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

        // Since android Oreo notification channel is needed.- foreground service
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            //Notification Channel 생성 및 설정
            val channel = NotificationChannel(channelId,
                "Fresh FCM Service",
                NotificationManager.IMPORTANCE_DEFAULT)
            notificationManager.createNotificationChannel(channel)
        }

        //notificationManager.notify() 메서드를 이용하여 알림 공지
        notificationManager.notify(0 /* ID of notification */, notificationBuilder.build())
    }

    companion object {
        private const val TAG = "MyFirebaseMsgService"
    }
}
