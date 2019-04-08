package kr.ac.gachon.ugkang.intent06

import android.os.Parcel
import android.os.Parcelable
import android.util.Log

//Parcelable 인터페이스를 구현한 ParcelCless 클래스 선언
class ParcelCless: Parcelable {
    //멤버속성 선언
    var id: Int = 0
    var name: String? = null

    /* 인텐트에 객체를 저장할 때 호출되는 메서드
       - MainActivity에서 startActivityForResult(intent, REQUEST_CODE)를 통해 객체를 전달할 떄 호출됨
       - 안드로이드 OS에서 Parcel? 클래스 타입의 객체가 dest 매개변수를 통해 전달함
     */
    override fun writeToParcel(dest: Parcel?, flags: Int) {
        Log.d("INTENT6", "writeToParcel() 호출")
        //id, name 속성값 설정
        dest?.writeInt(id)
        dest?.writeString(name)
    }

    override fun describeContents(): Int {
        return 0
    }

    /* 객체를 복원할 때 사용할 메서드 설정
       - 안드로이드에서는 객체를 복원할 때 CREATE 멤버 변수를 사용하여 해당 메서드를 호출함
       - CREATE 멤버변수를 static으로 선언하기 위해 companion object로 선언함(코틀린은 static 키워드가 없음)
    */
    companion object {
        @JvmField //안드로이드에서 static 변수처럼 호출할 수 있도록 @JvmField 붙여줌(final static 선언)
        val CREATOR: Parcelable.Creator<ParcelCless> = object: Parcelable.Creator<ParcelCless> {

            /* 인텐트로부터 객체를 추출해 낼 때 호출하는 메서드
              - SecondActivity에서 getParcelableExtra<ParcelTestCless>()메서드로 객체를 복원할 떄 호출됨
               - 객체를 복원하는 createFromParcel 메서드 오버라이딩(객체 하나만 담아서 넘기는 경우 호출됨)
            */
            override fun createFromParcel(source: Parcel?): ParcelCless {
                Log.d("INTENT6", "createFromParcel() 호출")

                // ParcelTestCless 클래스의 S1 객체 생성
                val S1 = ParcelCless()

                /* Parcel? 클래스 타입의 매개변수 source에 전달된 객체에서 속성값을 읽어
                   S1객체의 id와 name 속성을 저장하여 s1 객체를 반환
                   - !! : nullable로 설정된 property를 강제로 not null로 바꿔주는 연산자
                     (!! 표시를 property나 변수에 붙이면 강제로 null이 아님을 선언)
                */
                S1.id= source?.readInt()!!
                S1.name= source?.readString()
                return S1
            }

            //객체를 복원하는 newArray 메서드 오버라이딩(배열을 담아서 넘기는 경우 호출됨)
            override fun newArray(size: Int): Array<ParcelCless?> {
                //ParcelTestCless 타입의 배열을 만들어 요소들을 null 값으로 채워 반환
                return arrayOfNulls<ParcelCless>(size)
            }
        }
    }
}