<?php /* Template Name: upload */ ?>

<?php
 echo "file upload program<br />";
 echo "select the file<br />";
?>
<form method="post" action="http://localhost/upload/complete" enctype="multipart/form-data">
<input type="file" name="file"><hr>
<input type="submit" name="submit" value="send">
</form>

