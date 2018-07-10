[insert_php]
$current_user = wp_get_current_user();
$current_id = $current_user->ID;

global $wpdb;
$result = $wpdb->get_results ( "SELECT * FROM wp_uploaded_video  WHERE author =" . $current_id );
echo '<form method="post" action="http://192.168.10.37/script.php">';
echo '<table>';
  echo '<tr>';
    echo '<td> video_id </td>';
    echo '<td> title </td>';
    echo '<td> path </td>';
    echo '<td> size </td>';
    echo '<td> author </td>';
    echo '<td> uploaded_time </td>';
    echo '<td> type </td>';
    echo '<td> delete </td>';
    echo '</tr>';
    foreach ( $result as $print )   {
$video_id = $print->video_id;
      echo '<tr>';
      echo '<td><input type="hidden" name="video_id" value="'  .$video_id . '">' .$video_id . '</td>';
      echo '<td>' . $print->title.'</td>';
      echo '<td>' . $print->path.'</td>';
      echo '<td>' . $print->size.'</td>';
      echo '<td>' . $print->author.'</td>';
      echo '<td>' . $print->uploaded_time.'</td>';
      echo '<td>' . $print->type.'</td>';
      echo '<td><input type="submit" name="delete_btn" value="delete"></td>';
      echo '</tr>';
    }
echo '</table>';
echo '</form>';
[/insert_php]
