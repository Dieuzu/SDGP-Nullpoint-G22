<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Login</title>

    <!--external css sheets-->
    <link rel="stylesheet" href="style.css" />
    <link rel="stylesheet" href="login.css" />

</head>

<body>
    <header>
        <a href="./index.html">
            <img class="logo" src="Images/logo.png" />
        </a>

        <div class="btn-right">
            <button class="primary-btn"><a href="./signup.html">Register</a></button>
        </div>
    </header>
    <section class="login">
        <div class="frame">
            <img class="image" src="./Images/login-img.png" alt="">
        </div>
        <div class="form">
            <br><br>
            <b class="greetings">welcome back</b>
            <h2 class="greetings">Login to your account</h2>
            

                <form action="log.php" method="post">
                      
                    <label ><b>Username</b></label><br>
                    <input type="text" placeholder="Enter Username" name="uname" ><br><br>

                    <label ><b>Password</b></label><br>
                    <input type="password" placeholder="Enter Password" name="pass" ><br><br><br>

                    <button type="submit">Login</button><br>
                
                </form>
            
        </div>
    </section>
</body>

</html>