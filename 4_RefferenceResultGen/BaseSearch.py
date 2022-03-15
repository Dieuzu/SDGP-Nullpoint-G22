#this is the first early prototype to searching the net 
from subTask import subTask
from shlex import join
import re
import RunMeh
import os # this for deleting files 
import time

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
SearchResults = [] #this stores all results in this array
RefinedResults = [] # this where only refined results are stored
core = ["geeksforgeeks", "oracle", ".edu/", ".pdf", "w3schools", "freecodecamp", "codecademy","javatpoint", "semanticscholar"] #Core domains to get results from
# to search
# this is a temp run code with manual input
idNumber = str(1)
Task = "this is a String for subtask" #input("Please enter the Task at hand : ")

Deadline = "4" #input("Please enter the deadline in number of days : ")
 
Filename = "ExampleFileName" #input("Please enter the Filename : ")

rnlp = open('4_RefferenceResultGen\\NLPResults.txt','r')

MasterKey = rnlp.readline() #input("Please enter the MasterKey : ")

Keyword1 = rnlp.readline()  #input("Please enter the 1st Keyword : ")
Keyword2 = rnlp.readline()  #input("Please enter the 2nd Keyword : ")
Keyword3 = rnlp.readline()  #input("Please enter the 3rd Keyword : ")
Keyword4 = rnlp.readline()  #input("Please enter the 4th Keyword : ") 

print("")

# this creates a new object from the subtask class
NewTask = subTask(idNumber, Task, Deadline, Filename, MasterKey, Keyword1, Keyword2, Keyword3, Keyword4)
#print(NewTask.searchMe) #keywords printed line by line ??????
NewTask.PwintMe()
print("")

#runs the Search from the details stored in class
query = NewTask.searchMe
pdfQuery = query + " filetype:pdf"
SSchQuery = query + " semanticscholar"

print("Generating Refined Results Needed for Subtask " + NewTask.taskID +"....")

def BaseSearch(String, ResultNum):
    for j in search(String, tld="co.uk", num=ResultNum, stop=ResultNum, pause=2):
        #print(j + " \n")
        SearchResults.append(str(j))
        #f = open("4_RefferenceResultGen\TestFolder\\"+  NewTask.fileName +".txt", "a")
        f = open("4_RefferenceResultGen\TestFolder\Test.txt", "a") # comment me and uncomment above line in final
        f.write(j+"\n")
        f.close()
   
BaseSearch(pdfQuery,2)        
BaseSearch(query, 20)
BaseSearch(SSchQuery,2)

SearchResults = list(dict.fromkeys(SearchResults)) #this ensures no duplicates in lines 
        
for x in range(len(SearchResults)):
      for y in range(len(core)):
        if re.search(core[y], SearchResults[x]):
            #print(SearchResults[x])
            RefinedResults.append(SearchResults[x])
            #f = open("4_RefferenceResultGen\TestFolder\\Refined_"+  NewTask.fileName +".txt", "a")
            f = open("4_RefferenceResultGen\TestFolder\Refined_Test.txt", "a") # comment me and uncomment above line in final
            f.write(SearchResults[x]+"\n")
            f.close()
            break

RunMeh.main()

time.sleep(5)   # Delays for 5 seconds. You can also use a float value.      
# this is to delete the unwanted search results text file this wont exist after i import them to classes           
if os.path.exists("4_RefferenceResultGen\TestFolder\Test.txt") and os.path.exists("4_RefferenceResultGen\TestFolder\Refined_Test.txt"):
      os.remove("4_RefferenceResultGen\TestFolder\Test.txt")
      os.remove("4_RefferenceResultGen\TestFolder\Refined_Test.txt")
      print("\nDeleted the files Test.txt and Refined_Test.txt")
else:
  print("The files does not exist Continuing")