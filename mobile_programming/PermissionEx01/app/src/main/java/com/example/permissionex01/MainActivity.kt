package com.example.permissionex01

import android.content.pm.PackageManager
import android.os.Build
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    var permissionList = arrayOf (
        android.Manifest.permission.WRITE_EXTERNAL_STORAGE,
        android.Manifest.permission.READ_CONTACTS,
        android.Manifest.permission.WRITE_CONTACTS
        )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        checkPermission()
    }
    fun checkPermission() {
        if(Build.VERSION.SDK_INT < Build.VERSION_CODES.M) { return }

        for (pms: String in permissionList) {
            var permission_chk = checkSelfPermission(pms)

            if (permission_chk == PackageManager.PERMISSION_DENIED) {
                requestPermissions(permissionList, 0)
                break
            }
        }
    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)

        for (idx in grantResults.indices) {
            if (grantResults[idx] == PackageManager.PERMISSION_GRANTED) {
                textView.append("${permissions[idx]} : 권한 허용\n")
            } else {
                textView.append("${permissions[idx]} : 권한 미허용\n")
            }
        }
    }
}
