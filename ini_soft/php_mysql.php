<?php
function show_list_of_video($db_connection, $author_id) {
  $select = $db_connection->prepare("SELECT * FROM uploaded_video WHERE author=:author_id");
  $select->bindValue(':author_id', $author_id, PDO::PARAM_INT);
  $select->execute();
  while ($row = $select->fetch()) {
    echo "Author : " . $row['author'] . "\t Video ID : " . $row['video_id'] . "\n";

  }

  print "======== selection is done!! ======== \n\n";
}



function delete_video($db_connection, $author_id, $video_id, $file_route) {
 $affected_rows = $db_connection->prepare("DELETE FROM uploaded_video WHERE author=:author_id and video_id=:video_id");
 $affected_rows->bindValue(':author_id', $author_id, PDO::PARAM_INT);
 $affected_rows->bindValue(':video_id', $video_id, PDO::PARAM_INT);
 $affected_rows->execute();

 chmod($file_route, 777);
 unlink($file_route);
}

$db_connection = new PDO("mysql:host=localhost;dbname=wordpress;charset=utf8","root","ini6223") or die("connect fail\n");
print "connect success\n";

$author_id = 1;
$video_id = 17;

show_list_of_video($db_connection, $author_id);
delete_video($db_connection, $author_id, $video_id);
// show_list_of_video($db_connection, $author_id);
?>
