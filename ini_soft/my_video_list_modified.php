[insert_php]

$current_user = wp_get_current_user();
$current_id = $current_user->ID;

global $wpdb;
$result = $wpdb->get_results ( "SELECT * FROM wp_uploaded_video  WHERE author =" . $current_id );

echo '<table>';
  echo '<tr>';
    echo '<th> video_id </th>';
    echo '<th> title </th>';
    echo '<th> path </th>';
    echo '<th> size </th>';
    echo '<th> author </th>';
    echo '<th> uploaded_time </th>';
    echo '<th> type </th>';
    echo '<th> delete </th>';
    echo '</tr>';
    foreach ( $result as $print )   {
      echo '<tr>';
      echo '<td>' . $print->video_id.'</td>';
      $video_id = $print->video_id;
      echo '<td>' . $print->title.'</td>';
      echo '<td>' . $print->path.'</td>';
      echo '<td>' . $print->size.'</td>';
      echo '<td>' . $print->author.'</td>';
      $author = $print->author
      echo '<td>' . $print->uploaded_time.'</td>';
      echo '<td>' . $print->type.'</td>';
      echo '<td><button type="button" id="delete_video" onclick="delete_video(".$author.",".$video_id.")" name="delete_video">delete</button></td>';
      echo '</tr>';

    }
echo '</table>';
[/insert_php]

<script>
function selete_video(author, video_id){
  $.ajax({
    type:"POST",
    url:"http://localhost/delete_video.php",
    data:"author="+author+"&video_id="+video_id,
    cache:false,
    success: function(result) {
      alert(result);
    }
  });
}
</script>
