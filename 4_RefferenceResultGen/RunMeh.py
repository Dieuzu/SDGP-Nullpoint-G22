# write-html.py
import webbrowser

def main():
    f = open('4_RefferenceResultGen\TestFolder\SubTaskResults.html','a')
    r = open('4_RefferenceResultGen\TestFolder\Refined_Test.txt','r')
    
    P1 = """<!DOCTYPE html>
    <html style="font-size: 16px;">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta charset="utf-8">
        <meta name="keywords" content="Learn marketing strategy, Our Courses, Drive Your Career Forward">
        <meta name="description" content="">
        <meta name="page_type" content="np-template-header-footer-from-plugin">
        <title>NullPoint</title>
        <link rel="stylesheet" href="nicepage.css" media="screen">
    <link rel="stylesheet" href="Page-2.css" media="screen">
        <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
        <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
        <meta name="generator" content="Nicepage 4.4.3, nicepage.com">
        <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
        <link id="u-page-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i">

        <script type="application/ld+json">{
        "@context": "http://schema.org",
        "@type": "Organization",
        "name": "",
        "logo": "images/default-logo.png"
    }</script>
        <meta name="theme-color" content="#478ac9">
        <meta property="og:title" content="Page 2">
        <meta property="og:type" content="website">
      </head>
      <body class="u-body u-xl-mode"><header class="u-clearfix u-header u-header" id="sec-00c3"><div class="u-clearfix u-sheet u-sheet-1">
            <a href="https://nicepage.com" class="u-image u-logo u-image-1">
              <img src="images/default-logo.png" class="u-logo-image u-logo-image-1">
            </a>
          </div></header>
        <section class="u-align-center u-clearfix u-image u-shading u-section-1" src="" id="carousel_0791" data-image-width="150" data-image-height="97">
          <div class="u-clearfix u-sheet u-sheet-1">
            <h2 class="u-text u-text-1">NULLPOINT<br>Assignment Manager
            </h2>
          </div>
        </section>
        <section class="u-align-left u-clearfix u-grey-10 u-section-2" id="carousel_77f5">
          <div class="u-clearfix u-sheet u-valign-middle-md u-valign-middle-sm u-valign-middle-xs u-sheet-1">
            <h2 class="u-align-center u-custom-font u-font-montserrat u-text u-text-default u-text-1"> Maybe the Following Links Might help you.....</h2>
            <div class="u-border-16 u-border-palette-3-base u-line u-line-horizontal u-line-1"></div>
            <div class="u-expanded-width u-list u-list-1">
              <div class="u-repeater u-repeater-1"> """
              
    P2_1 = """    <div class="u-align-left u-container-style u-list-item u-repeater-item u-white u-list-item-1">
                  <div class="u-container-layout u-similar-container u-valign-middle u-container-layout-1">
                    <h5 class="u-text u-text-default u-text-2"> <a href=\""""
                                    
                
                    
    P2_3 = """</a></h5> 
              <div class="u-expanded-height-lg u-expanded-height-sm u-expanded-height-xl u-expanded-height-xs u-palette-3-base u-shape u-shape-rectangle u-shape-1"></div>
                  </div>
                </div> """


    P3 = """
              </div>
            </div>
          </div>
        </section>
        <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-67f3"><div class="u-clearfix u-sheet u-sheet-1">
            <p class="u-small-text u-text u-text-variant u-text-1">Nullpoint Assignment manager</p>
          </div></footer>
      </body>
    </html>"""



    f.write(P1)
    Linkindex = 1
    for x in r:
          P2_2 = "\" target=\"_blank\">Check out Link Number: " +  str(Linkindex)   
          FullHtml =  P2_1 + x + P2_2 + P2_3
          Linkindex += 1 
          f.write(FullHtml)

    f.write(P3)
    f.close()
    print("\nWebsite Created and deployed!")

    url = '4_RefferenceResultGen\TestFolder\SubTaskResults.html'
    webbrowser.open(url, new=2)  # open in new tab
       
if __name__ == "__main__":
   main()    