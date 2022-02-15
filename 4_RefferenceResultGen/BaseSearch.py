#this is the first early prototype to searching the net 
from subTask import subTask
from shlex import join
import re
import os # this for deleting files 

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
SearchResults = []
RefinedResults = []
core = ["geeksforgeeks", "oracle"] #Core domains to get results from
# to search
# this is a temp run code with manual input
idNumber = str(1)
Task = input("Please enter the Task at hand : ")

Deadline = input("Please enter the deadline in number of days : ")
 
Filename = input("Please enter the Filename : ")

MasterKey = input("Please enter the MasterKey : ")

Keyword1 = input("Please enter the 1st Keyword : ")
Keyword2 = input("Please enter the 2nd Keyword : ")
Keyword3 = input("Please enter the 3rd Keyword : ")
Keyword4 = input("Please enter the 4th Keyword : ") 
print("")

# this creates a new object from the subtask class
NewTask = subTask(idNumber, Task, Deadline, Filename, MasterKey, Keyword1, Keyword2, Keyword3, Keyword4)
NewTask.PwintMe()
print("")

#runs the Search from the details stored in class
query = NewTask.searchMe
print("Generating Refined Results Needed for Subtask " + NewTask.taskID +": \n")

for j in search(query, tld="co.uk", num=20, stop=20, pause=2):
    #print(j + " \n")
    SearchResults.append(str(j))
    #f = open("4_RefferenceResultGen\TestFolder\\"+  NewTask.fileName +".txt", "a")
    f = open("4_RefferenceResultGen\TestFolder\Test.txt", "a") # comment me and uncomment above line in final
    f.write(j+"\n")
    f.close()
    
for x in range(len(SearchResults)):
      for y in range(len(core)):
        if re.search(core[y], SearchResults[x]):
            print(SearchResults[x])
            RefinedResults.append(SearchResults[x])
            #f = open("4_RefferenceResultGen\TestFolder\\Refined_"+  NewTask.fileName +".txt", "a")
            f = open("4_RefferenceResultGen\TestFolder\Refined_Test.txt", "a") # comment me and uncomment above line in final
            f.write(SearchResults[x]+"\n")
            f.close()
            
# this is to delete the unwanted search results text file this wont exist after i import them to classes           
if os.path.exists("4_RefferenceResultGen\TestFolder\Test.txt") and os.path.exists("4_RefferenceResultGen\TestFolder\Refined_Test.txt"):
      os.remove("4_RefferenceResultGen\TestFolder\Test.txt")
      #os.remove("4_RefferenceResultGen\TestFolder\Refined_Test.txt")
      print("\nDeleted the files Test.txt and Refined_Test.txt")
else:
  print("The files does not exist Continuing")

  