package com.example.preffragmentexactivity

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v14.preference.PreferenceFragment
import android.support.v7.preference.PreferenceFragmentCompat

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        supportFragmentManager.beginTransaction().replace(android.R.id.content, PrefFragment()).commit()
    }
}
class PrefFragment : PreferenceFragmentCompat() {
    override fun onCreatePreferences(p0: Bundle?, p1: String?) {
        addPreferencesFromResource(R.xml.settings_preference)
    }
}
