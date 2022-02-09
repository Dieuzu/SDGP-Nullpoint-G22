#this is the first early prototype to searching the net 
from shlex import join


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
Filename = input("Please enter the Filename : ")

MasterKey = input("Please enter the MasterKey : ")

Keyword1 = input("Please enter the 1st Keyword : ")
Keyword2 = input("Please enter the 2nd Keyword : ")
Keyword3 = input("Please enter the 3rd Keyword : ")
Keyword4 = input("Please enter the 4th Keyword : ")



query = MasterKey + " " + Keyword1 + " " + Keyword2 + " " + Keyword3 + " " + Keyword4
print("Generating Results : \n")

for j in search(query, tld="co.uk", num=10, stop=10, pause=2):
    print(j + " \n")
    f = open("4_RefferenceResultGen\TestFolder\\"+  Filename +".txt", "a")
    f.write(j+"\n")
    f.close()