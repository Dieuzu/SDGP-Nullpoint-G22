print("[SYSTEM] Importing SPACY library")
print("\n[SYSTEM] Extracting Keywords from Coursework Specification....\n")

import spacy
#nlp = spacy.load("en_core_web_md")
nlp = spacy.load("en_core_web_sm")

#=======================================================================================

def spacyNLP(RDIR, Name, Num):
    NDIR = "output\\NLP\\" #this is the NLP saving location
    
    Taskfile = RDIR + Name+ str(Num) +".txt"  #DIR\Task_Num.txt
    Keyfile = NDIR + Name+ str(Num) +"_Keywords.txt" #DIR\Task_Num_Keywords.txt
    
    task =  r"" + Taskfile
    taskDoc = nlp(open(task).read())
  
    chunkKeywords = ""

    for chunk in taskDoc.noun_chunks:
    #    print(chunk)
        chunkKeywords = chunkKeywords + " " + str(chunk)

    keywordDoc = nlp(chunkKeywords)

    tokenKeyword = ""

    for token in keywordDoc:
        if not token.is_stop:
            tokenKeyword = tokenKeyword + " " + str(token)

    print("The Extracted Keywords for TASK " + str(Num) + " are : " + tokenKeyword)    
    print(" ")
    
    saveTaskNLPK = open(r""+Keyfile,'w')
    saveTaskNLPK.write(tokenKeyword)
    saveTaskNLPK.close()

#==================================================================
#directory = "3_NLPandKeyword\\Sample_Text\\"
#taskcount = 0
#taskName = "Task_"

#taskNumber = 3
#for i in range (taskNumber):
 #   taskcount += 1
  #  spacyNLP(directory, taskName, taskcount)


print("\n[SYSTEM] Successfully identified KEYWORDS !!!")