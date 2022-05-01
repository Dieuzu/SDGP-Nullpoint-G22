def searchtxt():
    import os
    import seperatetxt
    import sp
    import time
    import Json

    print("------------------------------------- Getting The Txt File And Seperate Task -------------------------------------\n")


    for root,dirs,files in os.walk('input\\'):
        for file in files:
                if file.endswith('.txt'):
                    if(os.path.join(root,file) == 'input\pimg.txt'):
                        print("[SYSTEM] Found name called "+ os.path.join(root,file)+"\n")
                        seperatetxt.Separatetxt(os.path.join(root,file))
                        
                    elif(os.path.join(root,file) == 'input\pdoc.txt'):
                        print("[SYSTEM] Found name called "+ os.path.join(root,file)+"\n")
                        sp.Separatetxt(os.path.join(root,file))
    
                        
                
