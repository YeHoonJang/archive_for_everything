package kr.ac.gachon.ugkang.listview03

import android.content.Context
import android.graphics.drawable.AnimationDrawable
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.ImageView
import android.widget.TextView

class WorkoutAdapter(val context: Context): BaseAdapter() {
    /* 리스트뷰에서 보여줄 아이템(항목) 화면의 인플레이션을 위해 LayoutInflater 참조 */
    private val mInflater: LayoutInflater = LayoutInflater.from(context)

    /* getCount() 메서드 : WorkoutDta 클래스의 모든 항목의 갯수를 리스트뷰에게 반환
       - 어댑터에서 관리하고 있는 데이터의 갯수를 리스트뷰에 반환
       - values()메서드를 이용하여 WorkoutDta 클래스의 모든 항목의 갯수를 반환
    */
    override fun getCount() = WorkoutData.values().size

    /* 어댑터에서 관리하는 데이터에서 position에 해당하는 데이터를 객체 형태로 리스트뷰에게 반환 */
    override fun getItem(position: Int) = WorkoutData.values()[position]

    /* 어댑터 데이터 아이디
       - 어댑터에서 관리하는 데이터에서 Position에 해당하는 데이터(아이템)의 id 값을 리스트뷰에게 반환
    */
    override fun getItemId(position: Int) = position.toLong()

    /* 리스트뷰에 출력할 아이템 뷰를 만들어 반환하는 메서드
       - 화면에 보일 아이템을 위한 뷰를 만들어 반환하는 메서드
       - 리스트뷰는 화면에 새로운 아이템을 표시할 떄마다 getView() 메서드를 호출
       - getCount()에서 반환된 갯수 많큼 호출

       - params
         1) position: 리스트뷰에 표시할 아이템의 position(0,1,2...)
         2) convertView: 리스트뷰에 아이템(항목) 1개를 표시할 때마다 getView()메서드가 호출됨
                         따라서 리스트뷰에 100개의 아이템을 표시하기 위해서는 getView()가
                         100번 호출되므로 비효울적임
                         이런 문제를 해결하기 위해 convertView를 사용
                         convertView는 생성된 뷰를 보관하는 View로서,
                         안드로이드에서는 getView() 메서드를 통해 리턴받은 뷰를 View를 따로
                         convertView에 보관하여 재사용하도록 지원함
            * 따라서 convertView == null 일때만 뷰를 생성하고, null이 아닌경우는
              convertView에 보관된 뷰를 재사용함
              convertView가 갖는 값은
                 (1) inflate가 한번도 되지 않았을 떄 : null
                 (2) inflate가 수행된 이후 : inflate에 의해 생성된 View

         3) parent: 부모 객체(ListView)
    */
    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View? {

        /* 이미 사용중인 뷰가 있으면 재사용, 없으면 뷰를 생성
            - 안드로이드에서는 리스트뷰에 화면상 보여지는 아이템의 갯수에 더하여 약간 여분의 ConverView를 생성하며,
              getView() 메서드에서는 각 ConverView에 해당 아이템 레이아웃을 설정하여 반환 함

            - convertView가 null이 아니면 convertView에서 반환된 뷰를 view에 저장
            - convertView가 null이면 새로운 뷰를 만들어 view에 저장(아이템의 화면을 구성한 XML 레이아웃(list_item_workout) 인플레이트
            - inflate() params
              1) R.layout.list_item_workout : 인플레이트할 리소스(항목의 레이아웃 파일)
              2) parent: 부모뷰
              3) attachToRoot : view를 부모뷰(root)에 attach할 것인지 지정
        */

        if(convertView != null){
            Log.i("CONVERT-VIEW","convertView is not null, position: ${position.toString()}")
        }else{
            Log.i("CONVERT-VIEW","convertView is null, position: ${position.toString()}")
        }

        val view = convertView ?: mInflater.inflate(R.layout.list_item_workout, parent, false)

        view.findViewById<TextView>(R.id.txt_workout_name).text = getItem(position).workName

        /* 2개의 이미지가 돌아가는 형식을 생성.*/
        val animation = AnimationDrawable().apply {
            addFrame(context.resources.getDrawable(getItem(position).firstImage), 1000)
            addFrame(context.resources.getDrawable(getItem(position).secondImage), 1000)
        }
        /* 반복해서 움직이게 해준다. */
        animation.isOneShot = false
        view.findViewById<ImageView>(R.id.img_detail_workout).setImageDrawable(animation)
        animation.start()
        return view
    }
}