def searchtxt():
    import os
    import seperatetxt

    for root,dirs,files in os.walk('D:\campus\ex'):
        for file in files:
                if file.endswith('.txt'):
                    seperatetxt.Separatetxt(os.path.join(root,file))