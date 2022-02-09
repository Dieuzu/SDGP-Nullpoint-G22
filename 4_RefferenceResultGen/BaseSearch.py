#this is the first early prototype to searching the net 
from subTask import subTask
from shlex import join

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
# this is a temp run code with manual input
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
NewTask = subTask(Task, Deadline, Filename, MasterKey, Keyword1, Keyword2, Keyword3, Keyword4)
NewTask.PwintMe()
print("")

#runs the Search from the details stored in class
query = NewTask.searchMe
print("Generating Results : \n")

for j in search(query, tld="co.uk", num=10, stop=10, pause=2):
    print(j + " \n")
    f = open("4_RefferenceResultGen\TestFolder\\"+  NewTask.fileName +".txt", "a")
    f.write(j+"\n")
    f.close()