def pdfFile(filename):
    import PyPDF2
    import time
    print("------------------------------------- PDF To Text Extraction Start Here -------------------------------------\n")

    start_time = time.time()
    x = 0

    pdfFileObj = open(filename, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    x = pdfReader.numPages
    print("[SYSTEM] Extracting data from docx to text\n")

    for y in range(0,x):
        pageObj = pdfReader.getPage(y)
        print("Page no :" + str (1 + pdfReader.getPageNumber(pageObj)))
        content = pageObj.extractText()

        f = open('input\\ppdf.txt', 'w')
        f.write(content)
        f.close()   
    print("[SYSTEM] Writing data to a text file\n")
        
    pdfFileObj.close()
    sttime = time.time() - start_time
    format_float = "{:.2f}".format(sttime)
    print("[SYSTEM] "+format_float+" Seconds Extracting Data From PDF To Txt\n")