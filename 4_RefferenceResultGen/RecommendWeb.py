# write-html.py
import webbrowser

def CreateRecomendPage():
        
    f = open('web\\html\\TaskResults.html','a')
    r = open('output\\SearchResults\\Refined_Links.txt','r')
    

    P1 = """<!DOCTYPE html>
    <html lang="en">

        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <title>Recommdation </title>
            <!--external css sheets-->
            <link rel="stylesheet" href="../styles/style.css" />
            <link rel="stylesheet" href="../styles/recommdation.css" />
        </head>

        <body>
            <header>
                <a href="../index.html">
                    <img class="logo" src="../Images/logo.png" />
                </a>
            </header>

            <section class="main">
                <div class="context">
                    <h1> We Recommend the Following links : </h1>
                    <h4> [For better results Check them based on Relevancy]</h4>
                </div>

                """

    P2_1 = """<div class="link-box">
                    <h5><a href=\""""


    P2_3 = """</a></h5>
                </div>
                <br><br>

                """

    P3 = """<footer>
                    <img class="footer-logo" src="">
                    <div class="footer-title">
                        <h2>Join Assignment Manager</h2>
                        <p>Subscribe to get alerted on new updates and offers</p>
                    </div>

                    <div class="footerForm">
                        <input type="email" placeholder="Enter Your Email" class="widget-input footerEmail">
                        <button class="primary-btn subscribe" onclick="">Subscribe</button>
                    </div>

                    <div class="hr"></div>
                    <div class="footer-bottom">
                        <div class="footer-btm-cnt">
                            <p>Privacy policy</p>
                        </div>
                        <div class="footer-btm-cnt">
                            <p>Terms and Conditions</p>
                        </div>
                        <div class="footer-btm-cnt">
                            <p>Covid Guidelines</p>
                        </div>
                    </div>
                    <div class="cpryt">
                        <p>@Assignment Manager 2022</p>
                    </div>
                </footer>
            </section>
        </body>
    </html>"""
    
    print ("[SYSTEM] Creating the TaskResults.html")
    f.write(P1)
    Linkindex = 1
    
    for x in r:
        spliter = x.split(",")
        
        P2_2 = "\" target=\"_blank\">Check out Link Number: " +  str(Linkindex)  + " (" + str(spliter[1]) +"% Relevancy)"

        FullHtml =  P2_1 + spliter[0] + P2_2 + P2_3
        Linkindex += 1 
        f.write(FullHtml)

    f.write(P3)
    f.close()
    
    print("[SYSTEM] Deploying the TaskResults.html")

    url = 'web\\html\\TaskResults.html'
    webbrowser.open(url, new=2)  # open in new tab
