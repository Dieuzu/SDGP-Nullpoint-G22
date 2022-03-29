import chunk
import spacy
#nlp = spacy.load("en_core_web_md")
nlp = spacy.load("en_core_web_sm")

def spacyNLP(DIR, Name, Num):
    Taskfile = DIR + Name+ str(Num) +".txt"  #DIR\Task_Num.txt
    Keyfile = DIR + Name+ str(Num) +"_Keywords.txt" #DIR\Task_Num_Keywords.txt
    
    task =  r"" + Taskfile
    taskDoc = nlp(open(task).read())

    #for token in taskDoc:
     #   if not token.is_stop:
      #      print(token)

    chunkKeywords = ""

    for chunk in taskDoc.noun_chunks:
    #    print(chunk)
        chunkKeywords = chunkKeywords + " " + str(chunk)
    print("The Extracted Keywords are : " + chunkKeywords)    
    #print(str(taskDoc.ents))

    saveTaskNLPK = open(r""+Keyfile,'w')
    saveTaskNLPK.write(chunkKeywords)
    saveTaskNLPK.close()


#==================================================================
directory = "3_NLPandKeyword\\Sample_Text\\"
taskcount = 0
taskName = "Task_"

taskNumber = 3
for i in range (taskNumber):
    taskcount += 1
    spacyNLP(directory, taskName, taskcount)




#with open('output.txt', 'w') as f:
 #   while loop:
       #f.write(stuff)