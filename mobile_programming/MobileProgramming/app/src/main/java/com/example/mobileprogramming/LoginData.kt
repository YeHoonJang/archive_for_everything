package com.example.mobileprogramming

import android.os.Parcel
import android.os.Parcelable
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class LoginData(
    @PrimaryKey
    val userName: String,
    val userPass: String
) : Parcelable {

    /* 객체를 복원할 때 사용할 메서드 선언 */
    companion object CREATOR : Parcelable.Creator<LoginData> {

        /* 인텐트로부터 LoginData 객체 데이터를 추출할 때 호출되는 메서드
          - Parcel로 부터 LoginData 객체 데이터 클래스의 인스턴스를 반환
          - 노드에서 JSON.parse에 해당합니다.
        */
        override fun createFromParcel(parcel: Parcel): LoginData {
            return LoginData(parcel)
        }

        /* 객체를 복원하는 메서드(배열을 담아서 넘길 때 호출)
         - Parcel을 어레이로 만들때 새로운 어레이를 선언하기위해 사용합니다.
         - 정말 특별한 경우가 아니라면 아래와 같은 형식을 고정하여 사용합니다
        */
        override fun newArray(size: Int): Array<LoginData?> = arrayOfNulls(size)
    }

    /* Parent인 Parcelable에 값을 전달합니다.*/
    private constructor(parcel: Parcel) : this(parcel.readString() ?: "", parcel.readString() ?: "")

    /* 인텐트에 객체를 저장할 때 호출되는 메서드(객체 저장)
       - MainActivity에서 startActivity(myIntent)를 통해 인텐트를 전달할 때 호출됨
       - dest 객체에 userName, userPass 속성 저장(Parcel 객체 타입으로 변환)
       - 이때 인자가 늘어나면 인자에 맞게 값을 처리합니다.
       - 노드에서 JSON.Stringify에 해당합니다
    */
    override fun writeToParcel(dest: Parcel, flags: Int) {
        dest.writeString(userName)
        dest.writeString(userPass)
    }

    /* 전달하는 값의 형식을 리턴하여 크게 0과 CONTENTS_FILE_DESCRIPTOR라는 BIG Mask값이 있습니다.*/
    /* 일반적으로는 0을쓰고 파일과 같은 바이트 형태의 데이터를 넘길때 선언할 수 있습니다.*/
    override fun describeContents(): Int = 0
}
