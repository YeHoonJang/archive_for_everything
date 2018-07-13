<?php /* Template Name: complete */ ?>
<?php
/*  $uploaddir = "http://192.168.10.37:/var/www/html/wp-content/uploads/"; */
 $uploaddir = "/var/www/html/wp-content/uploads/";
 $uploadfile = $uploaddir . basename($_FILES['file'] ['name']); 
 $allowedExts = array("jpg", "jpeg", "gif", "png", "mp3", "mp4", "wma");
 $extension = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
 if ((($_FILES["file"]["type"] == "video/mp4")
|| ($_FILES["file"]["type"] == "audio/mp3")
|| ($_FILES["file"]["type"] == "audio/wma")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/png")
|| ($_FILES["file"]["type"] == "image/jpeg"))

&& ($_FILES["file"]["size"] < 20000)
&& in_array($extension, $allowedExts))

  {
  if ($_FILES["file"]["error"] > 0)
    {
    echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
    }
  else
    {
    echo "Upload: " . $_FILES["file"]["name"] . "<br />";
    echo "Type: " . $_FILES["file"]["type"] . "<br />";
    echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
    echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br />";

    if (file_exists($uploadfile))
      {
      echo $_FILES["file"]["name"] . " already exists. ";
      }
    else
      {
      move_uploaded_file($_FILES["file"]["tmp_name"], $uploadfile);
      echo "Stored in: " . $uploadfile ;
      }
    }
  }
else
  {
  echo "Invalid file";
  }


/*   echo "confirm file information <br />";
 $uploaddir = "http://192.168.10.37/wp-content/uploads/";
 $uploadfile = $uploaddir . basename($_FILES['upload'] ['name']);
 if(move_uploaded_file($_FILES['upload']['tmp_name'],$uploadfile)){
  echo "파일이 업로드 되었습니다.<br />";
  echo "<img src ={$_FILES['upload']['name']}> <p>";
  echo "1. file name : {$_FILES['upload']['name']}<br />";
  echo "2. file type : {$_FILES['upload']['type']}<br />";
  echo "3. file size : {$_FILES['upload']['size']} byte <br />";
  echo "4. temporary file name : {$_FILES['upload']['size']}<br />";
 } else {
  echo "error :  {$_FILES}</ br>";
  echo "파일 업로드 실패 !! 다시 시도해주세요.<br />";
 } */
?>
