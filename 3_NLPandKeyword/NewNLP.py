import spacy
nlp = spacy.load("en_core_web_sm")

def spacyNLP(DIR, Name, Num):
    Taskfile = DIR + Name+ str(Num) +".txt"  #DIR\Task_Num.txt
    Keyfile = DIR + Name+ str(Num) +"_Keywords.txt" #DIR\Task_Num_Keywords.txt
    
    task =  r"" + Taskfile
    taskDoc = nlp(open(task).read())

    saveTaskNLPK = open(r""+Keyfile,'w')

    print("\nThe Extracted Keywords are : " + str(taskDoc.ents))

    #for chunk in taskDoc.noun_chunks:
    #    print(chunk)

    saveTaskNLPK.write(str(taskDoc.ents))
    saveTaskNLPK.close()

    

#==================================================================
directory = "3_NLPandKeyword\\Sample_Text\\"
taskcount = 0
taskName = "Task_"

taskNumber = 3
for i in range (taskNumber):
    taskcount += 1
    spacyNLP(directory, taskName, taskcount)

