<?php
$db = new PDO('mysql:host=localhost;dbname=wordpress;charset=utf8', 'root', 'ini6223');
$stmt = $db->prepare("SELECT file_path FROM wp_uploaded_video WHERE status='delete'");
$stmt->execute();
$status = $stmt->fetchAll();
print_r($status);

foreach ($status as $key => $val) {
  $file_path = $val[0];
  $stmt = $db->prepare("DELETE FROM wp_uploaded_video WHERE file_path=:file_path");
  $stmt->bindValue(':file_path', $file_path);
  $stmt->execute();

  unlink($file_path);
}
?>
