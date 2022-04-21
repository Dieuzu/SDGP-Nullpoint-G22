from researchGap import NLPFindKeyword

print ("\n===================================== NLP Keyword Extraction =====================================\n")
directory = "3_NLPandKeyword\\Sample_Text\\" # this is simulation folder
taskcount = 0
taskName = "Task_"

taskNumber = 3
for i in range (taskNumber):
    taskcount += 1
    NLPFindKeyword.extractNLPKeys(directory, taskName, taskcount)