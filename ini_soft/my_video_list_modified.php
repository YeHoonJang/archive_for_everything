[insert_php]
$db = new PDO('mysql:host=localhost;dbname=wordpress;charset=utf8', 'root', 'ini6223');
foreach($_COOKIE as $key => $value)
{
  if(preg_match('/^wordpress_logged_/', $key))
  {
   global $loggin_cookie;
   $loggin_cookie =  $value;
  }
}
$cookie_info = explode("|", $loggin_cookie);
$username =  $cookie_info[0];
$stmt = $db->prepare("SELECT ID FROM wp_users WHERE user_login=:user_name") ;
$stmt->execute(array(':user_name' =>  $username));
$user = $stmt->fetch();
$user_id = ($user["ID"]);
$stmt = $db->prepare("SELECT * FROM wp_uploaded_video WHERE author =:user_id AND NOT status ='delete'");
$stmt->execute(array(':user_id' =>  $user_id));
$result = $stmt->fetchAll();
$row_count = $stmt->rowCount();
echo $row_count.' rows selected';

echo '<table>';
 echo '<tr>';
   echo '<td> title </td>';
   echo '<td> size </td>';
   echo '<td> uploaded_time </td>';
   echo '<td> type </td>';
   echo '<td> delete </td>';
   echo '</tr>';
foreach ($result as $key => $val )   {
     $video_id = $val[0];
     $title = $val[1];
     echo '<tr>';
     echo '<td>' . $val[1].'</td>';
     echo '<td>' . $val[3].'</td>';
     echo '<td>' . $val[5].'</td>';
     echo '<td>' . $val[6].'</td>';
     echo '<td><a name="'.$video_id.'" id=btn_modal  href="http://192.168.10.37/update_video_status.php?video_id='.$video_id.'">delete</a></td>';
     echo '</tr>';
   }
echo '</table>';
[/insert_php]
