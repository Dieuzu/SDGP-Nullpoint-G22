def readword(filename):
    import docx2txt
    print("------------------------------------- Docx To Text Extraction Start Here -------------------------------------\n")
    

    mytext = docx2txt.process(filename)
    print("[SYSTEM] Extracting data from docx to text\n")

    print("[SYSTEM] Writing data to a text file\n")

    f = open('input\\pdoc.txt', 'w')
    f.write(mytext)
    f.close()
