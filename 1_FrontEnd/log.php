<?php

if (isset($_POST['uname']) && isset($_POST['password'])) {
    function validate($data){
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    $uname = validate ($_post['uname']);
    $pass = validate($_post['password']);

    if (empty($uname)){
        header("Location: login.php?error=User Name is required");
        exit();

    }else if(empty($pass)){
        header("Location: login.php?error=Password is required");
        exit();
        
    }else{
        echo "Valid input";
    }
}else{
    header("Location: login.php");
    exit();
}
?>