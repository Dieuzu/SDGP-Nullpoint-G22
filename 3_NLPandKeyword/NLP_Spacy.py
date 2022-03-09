# Load the NLP model (Spacy)

import spacy
nlp = spacy.load("en_core_web_sm")

# Extract the keywords for the FIRST TASK and write it on a text file for the next segment to be used. 
   
task1 = r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\Sample Text\Task1.txt'
t1 = open(task1).read()
t1doc = nlp(t1)
for token in t1doc:
    print (token)
print(t1doc.ents)
ourt1k = open(r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\TaskKeywords\Task1Keywords.txt','w')
t1k = (t1doc.ents)


# Extract the keywords for the SECOND TASK and write it on a text file for the next segment to be used. 
task2 = r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\Sample Text\Task2.txt'
t2 = open(task1).read()
t2doc = nlp(t2)
for token in t2doc:
    print (token)
print(t2doc.ents)
ourt2k = open(r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\TaskKeywords\Task2Keywords.txt','w')
t2k = (t2doc.ents)

ourt2k.write(str(t2k))

ourt2k.close()



# Extract the keywords for the THIRD TASK and write it on a text file for the next segment to be used. 
task3 = r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\Sample Text\Task3.txt'
t3 = open(task3).read()
t3doc = nlp(t3)
for token in t3doc:
    print (token)
print(t3doc.ents)
ourt3k = open(r'C:\Users\ASUS TUF\Desktop\2nd Year\2nd SEM\SDGP\TaskKeywords\Task3Keywords.txt','w')
t3k = (t3doc.ents)