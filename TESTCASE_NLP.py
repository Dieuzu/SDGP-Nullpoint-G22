from researchGap import NLPFindKeyword

print ("\n===================================== NLP Keyword Extraction =====================================\n")
directory = "TestCaseCodes\\Rishi\\" # this is simulation folder
taskcount = 0
taskName = "Task_"

taskNumber = 3
for i in range (taskNumber):
    taskcount += 1
    NLPFindKeyword.extractNLPKeys(directory, taskName, taskcount)