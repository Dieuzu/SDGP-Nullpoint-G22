def searchtxt():
    import os
    import seperatetxt
    import sp

    for root,dirs,files in os.walk('D:\campus\ex'):
        for file in files:
                if file.endswith('.txt'):
                    if(os.path.join(root,file) == 'D:\campus\ex\pimg.txt'):
                        seperatetxt.Separatetxt(os.path.join(root,file))
                        print(os.path.join(root,file))
                    elif(os.path.join(root,file) == 'D:\campus\ex\pdoc.txt'):
                        sp.Separatetxt(os.path.join(root,file))
                        print(os.path.join(root,file))
