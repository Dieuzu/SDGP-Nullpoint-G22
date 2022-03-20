import docx

def readword(filename):

    doc = docx.Document(filename)

    completeText = []

    for para in doc.paragraphs:
        completeText.append(para.text)

    a = ('\n' .join(completeText))

    f = open('D:\campus\p.txt', 'w')
    f.write(a)
    f.close()
