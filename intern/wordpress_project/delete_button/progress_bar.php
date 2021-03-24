[insert_php]
$db = new PDO('mysql:host=localhost;dbname=wordpress;charset=utf8', 'root', 'ini6223');

echo "file upload program<br />";
echo "select the file<br />";

foreach($_COOKIE as $key => $value)
{
  if(preg_match('/^wordpress_logged_/', $key))
  {
  global $loggin_cookie;
   $loggin_cookie =  $value;

       // You can access $value or create a new array based off these values
  }
}
$cookie_info = explode("|", $loggin_cookie);
$username =  $cookie_info[0];
$stmt = $db->prepare("SELECT ID FROM wp_users WHERE user_login=:user_name");
$stmt->execute(array(':user_name' =>  $username));
$user = $stmt->fetch();
$user_id = ($user["ID"]);


[/insert_php]

<script>
function _(el){
return document.getElementById(el);
}
function uploadFile(){
var file = _("file1").files[0];
var formdata = new FormData();
formdata.append("file1", file);
var ajax = new XMLHttpRequest();
ajax.upload.addEventListener("progress", progressHandler, false);
ajax.addEventListener("load", completeHandler, false);
ajax.addEventListener("error", errorHandler, false);
ajax.addEventListener("abort", abortHandler, false);
ajax.open("POST", " http://192.168.10.37/file_upload_parser_final.php"); // 개발서버에선 localhost를 192.168.10.190로 수정
ajax.send(formdata);
}
function progressHandler(event){
_("loaded_n_total").innerHTML = "Uploaded "+event.loaded+" bytes of "+event.total;
var percent = (event.loaded / event.total) * 100;
_("progressBar").value = Math.round(percent);
_("status").innerHTML = Math.round(percent)+"% uploaded... please wait";
}
function completeHandler(event){
_("status").innerHTML = event.target.responseText;
_("progressBar").value = 0;
}
function errorHandler(event){
_("status").innerHTML = "Upload Failed";
}
function abortHandler(event){
_("status").innerHTML = "Upload Aborted";
}
</script>
<form method="post"  enctype="multipart/form-data">
 <input type="file" name="file1" id="file1"><br>
 <input type="button" value="Upload File" onclick="uploadFile()">
<progress id="progressBar" value="0" max="100" style="width:300px;"></progress>
<h3 id="status"></h3>
<p id="loaded_n_total"></p>
</form>
