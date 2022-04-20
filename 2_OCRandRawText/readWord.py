def readword(filename):
    import docx2txt

    mytext = docx2txt.process(filename)

    f = open('input\\pdoc.txt', 'w')
    f.write(mytext)
    f.close()
