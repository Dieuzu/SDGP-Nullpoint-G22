import spacy

import time

def extractNLPKeys(RDIR, Name, Num): 
    # RDIR = the Root location of the file u wanna run through nlp
    # Name = name of the file u wanna run through NLP
    # Number = index of the file name

    start = time.perf_counter()

    nlp = spacy.load("en_core_web_sm")

    print("[SYSTEM] Extracting Keywords from : " + Name + str(Num)+ ".txt!")
    NDIR = "output\\NLP\\" #this is the NLP saving location

    Taskfile = RDIR + Name+ str(Num) +".txt"           #DIR\Task_Num.txt           | where DIR = output\Raw\
    Keyfile = NDIR + Name+ str(Num) +"_Keywords.txt"   #DIR\Task_Num_Keywords.txt  | where DIR = output\NLP\

    task =  r"" + Taskfile
    taskDoc = nlp(open(task).read())

    chunkKeywords = ""
    for chunk in taskDoc.noun_chunks:
        chunkKeywords = chunkKeywords + str(chunk) + " "

    keywordDoc = nlp(chunkKeywords)

    tokenKeyword = ""
    for token in keywordDoc:
        if not token.is_stop:
            tokenKeyword = tokenKeyword + str(token) + " "
    print("[SYSTEM] The Extracted Keywords for "+ Name + str(Num)+ ".txt are : " + tokenKeyword)  

    print("[SYSTEM] Saving the Keywords in : " + Keyfile + "\n")
    saveTaskNLPK = open(r""+Keyfile,'w')
    saveTaskNLPK.write(tokenKeyword)
    saveTaskNLPK.close()

    elapsed = time.perf_counter()
    timeTaken = elapsed - start
    print ("\n[SYSTEM] This Component took Exactly " + str(round(timeTaken,2)) + " seconds to Generate Results!\n")