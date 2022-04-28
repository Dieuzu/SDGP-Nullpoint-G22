def readword(filename):
    import docx2txt
    import time
    print("------------------------------------- Docx To Text Extraction Start Here -------------------------------------\n")

    start_time = time.time()
    mytext = docx2txt.process(filename)
    print("[SYSTEM] Extracting data from docx to text\n")

    print("[SYSTEM] Writing data to a text file\n")

    f = open('input\\pdoc.txt', 'w')
    f.write(mytext)
    f.close()
    sttime = time.time() - start_time
    format_float = "{:.2f}".format(sttime)
    print("[SYSTEM] "+format_float+" Seconds Extracting Data From word document To Txt\n")
