package com.example.restapiex01.login

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import com.google.firebase.auth.FirebaseAuth
import kotlinx.android.synthetic.main.activity_login.*
import com.example.restapiex01.R
import com.example.restapiex01.main.MainActivity

// FirebaseAuth를 이용한 사용자 login
class LoginActivity : AppCompatActivity() {

    //FirebaseAuth 인스턴스를 선언- FirebaseAuth 인스턴스를 초기화
    val firebaseAuth by lazy { FirebaseAuth.getInstance() }

    var lockButton = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        /* 사용자가 성공적으로 로그인 되어 있으면 MainActivity 이동 */
        firebaseAuth.currentUser?.let {
            moveToMainActivity()
        }

        /* 신규 회원가입 처리
           - createUserWithEmailAndPassword() 메서드를 사용하여
             이메일주소와 비밀번호를 가져와 유효성을 검사한 후 신규 사용자를 생성(회원가입)
        */
        btn_register.setOnClickListener {
            if (!lockButton) {
                /* 이메일주소와 비밀번호 입력여부 검사*/
                isValidateInputs()?.let { pair ->
                    lockButton = true
                    progressBar.visibility = View.VISIBLE
                    /* 이메일주소와 비밀번호를 가져와 유효성을 검사한 후 신규 사용자를 생성(회원가입) */
                    firebaseAuth.createUserWithEmailAndPassword(pair.first, pair.second)
                        .addOnCompleteListener { task ->
                            /* 성공한 경우*/
                            task.addOnSuccessListener {
                                lockButton = false
                                progressBar.visibility = View.GONE
                                Toast.makeText(this, "회원가입에 성공했습니다.", Toast.LENGTH_SHORT).show()
                            }

                            /* 실패한 경우*/
                            task.addOnFailureListener {
                                lockButton = false
                                progressBar.visibility = View.GONE
                                Toast.makeText(this, "에러발생: + ${it.message}", Toast.LENGTH_SHORT).show()
                            }
                        }
                }

            } else {
                Toast.makeText(this, "이전요청을 처리중입니다.", Toast.LENGTH_SHORT).show()
            }
        }

        /* 기존 사용자 로그인 처리
           - signInWithEmailAndPassword() 메소드를 사용하여 이메일 주소와 비밀번호를 가져와
             유효성을 검사한 후, 등록된 사용자인경우 Main Activity로 이동하도록 처리
        */
        btn_login.setOnClickListener {
            isValidateInputs()?.let { pair ->
                firebaseAuth.signInWithEmailAndPassword(pair.first, pair.second).addOnCompleteListener { task ->
                    /* 성공한 경우*/
                    task.addOnSuccessListener {
                        lockButton = false
                        progressBar.visibility = View.GONE
                        /*로그인 성공시 바로 MainActivity로 이동합니다.*/
                        moveToMainActivity()
                    }

                    /* 실패한 경우*/
                    task.addOnFailureListener {
                        lockButton = false
                        progressBar.visibility = View.GONE
                        Toast.makeText(this, it.message, Toast.LENGTH_SHORT).show()
                    }
                }

            }
        }
    }

    /* main으로 이동합니다.*/
    fun moveToMainActivity() {
        Intent(this, MainActivity::class.java).run {
            startActivity(this)
            finish()
        }
    }

    /* 이메일주소와 비밀번호를 체크한 후 값이 있으면 Pair,
       값이 없으면 null을 리턴합니다.*/
    fun isValidateInputs(): Pair<String, String>? {
        val userEmail = edit_email.text.toString()
        val userPassword = edit_password.text.toString()
        if (userEmail.isBlank() || userPassword.isBlank()) {
            Toast.makeText(this, "이메일과 비밀번호흘 입력해주세요", Toast.LENGTH_LONG).show()
            return null
        } else {
            return Pair(userEmail, userPassword)
        }
    }
}
