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

        f = open('input\\ppdf.txt', 'w')
        f.write(content)
        f.close()       

    pdfFileObj.close()