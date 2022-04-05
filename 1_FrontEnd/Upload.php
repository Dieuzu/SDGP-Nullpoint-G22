
<?php

$filename = $_FILES['file']['name'];
$location = "upload/".$filename;

if(move_uploaded_file($_FILES['file']['tmp_name'], $location)){
    echo '<p>File uploaded successfully </p>';   
}else{
    echo '<b>Error uploading file.<b>';
}

?>
