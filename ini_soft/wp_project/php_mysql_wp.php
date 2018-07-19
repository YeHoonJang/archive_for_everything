<?php

$db_connection = new PDO("mysql:host=localhost;dbname=wordpress;charset=utf8","root","ini6223") or die("connect fail\n");
print "connect success\n";


$current_user = wp_get_current_user();
echo 'User ID: ' . $current_user->ID . '<br />';


$author_id = $current_user;
$stmt = $db_connection->prepare("SELECT * FROM uploaded_video WHERE author=:author_id");
$stmt->bindValue(':author_id', $author_id, PDO::PARAM_INT);
$stmt->execute();
while ($row = $stmt->fetch()) {
  echo "Author : " . $row['author'] . "\t Video ID : " . $row['video_id'] . "\n";

}

?>
