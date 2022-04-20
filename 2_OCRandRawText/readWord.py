def readword(filename):
    import docx2txt

    mytext = docx2txt.process(filename)

    f = open('D:\campus\ex\pdoc.txt', 'w')
    f.write(mytext)
    f.close()
