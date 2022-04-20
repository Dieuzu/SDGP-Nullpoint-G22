def readword(filename):
    import docx

    doc = docx.Document(filename)

    completeText = []

    for para in doc.paragraphs:
        completeText.append(para.text)

    a = ('\n' .join(completeText))

    f = open('D:\campus\ex\p.txt', 'w')
    f.write(a)
    f.close()