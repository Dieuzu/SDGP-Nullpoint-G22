# this will be a common class for every task created by the system
class subTask:
    taskID = 0                # for quick tracking 
    subTask = ""              #contains the Entire string of the task
    deadlineNumDays = 0       #contains the Remaining number of days till deadline
    
    fileName = ""             #contains the FileName of the Task wen stored in text file (Can be coded obsolete)
    
    masterKey = ""            #contains the Main Subject topic of the task
    
    #The below Variables contain the 4 Important keywords Extracted from NLP componanrt related to the subtask
    keyWord1 = ""             
    keyWord2 = ""
    keyWord3 = ""
    keyWord4 = ""
    
    searchMe = ""             #this will be the string that Will be passed through the Web Scraper
    
    #Constructor
    def __init__(self, ID, task, deadline, fName, MKey, k1, k2, k3, k4):
        self.taskID = ID
        self.subTask = task
        self.deadlineNumDays = deadline
        self.fileName = fName
        self.masterKey =  MKey
        self.keyWord1 = k1
        self.keyWord2 = k2
        self.keyWord3 = k3
        self.keyWord4 = k4
        self.searchMe = self.searchMe = self.masterKey + " " + self.keyWord1 + " " + self.keyWord2 + " " + self.keyWord3 + " " + self.keyWord4


    def PwintMe (self): # this is a test method
        print ("The Current task ID is : " + self.taskID) 
        print ("The Current task is : " + self.subTask) 
        print ("The Current task is due in : " + self.deadlineNumDays + " Days") 
        print ("The Current task is stored as : " + self.fileName + ".txt") 
        #print ("The Current task Search String is : " + self.searchMe) 
        
