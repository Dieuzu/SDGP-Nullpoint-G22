def pdfFile(filename):
    import PyPDF2
    x = 0

    pdfFileObj = open(filename, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    x = pdfReader.numPages

    for y in range(0,x):
        pageObj = pdfReader.getPage(y)
        print("Page no :" + str (1 + pdfReader.getPageNumber(pageObj)))
        content = pageObj.extractText()

        f = open('D:\campus\ex\p.txt', 'w')
        f.write(content)
        f.close()       

    pdfFileObj.close()