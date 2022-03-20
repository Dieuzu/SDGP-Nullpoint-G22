# Load the NLP model (Spacy)

import spacy
nlp = spacy.load("en_core_web_sm")

# Extract the keywords for the FIRST TASK and write it on a text file for the next segment to be used. 
  
task1 = r'3_NLPandKeyword\\Sample_Text\\Task1_Text.txt'
t1 = open(task1).read()
t1doc = nlp(t1)

#for token in t1doc:
   # print (token)
#print(t1doc.ents)

ourt1k = open(r'3_NLPandKeyword\\Sample_Text\\Task1Keywords.txt','w')
t1k = (t1doc.ents)

print(' ')
print('The Extracted Keywords are : ')
print(' ')
for chunk in t1doc.noun_chunks:
      print(chunk)

ourt1k.write(str(t1k))
ourt1k.close()












# Extract the keywords for the SECOND TASK and write it on a text file for the next segment to be used. 
task2 = r'3_NLPandKeyword\\Sample_Text\\Task2_Text.txt'
t2 = open(task2).read()
t2doc = nlp(t2)

#for token in t2doc:
 #   print (token)
#print(t2doc.ents)

ourt2k = open(r'3_NLPandKeyword\\Sample_Text\\Task2Keywords.txt','w')
t2k = (t2doc.ents)

print(' ')
print('The Extracted Keywords are : ')
print(' ')
for chunk in t2doc.noun_chunks:
      print(chunk)

ourt2k.write(str(t2k))

ourt2k.close()
print(' ')


# Extract the keywords for the THIRD TASK and write it on a text file for the next segment to be used. 
task3 = r'3_NLPandKeyword\\Sample_Text\\Task3_Text.txt'
t3 = open(task3).read()
t3doc = nlp(t3)

#for token in t3doc:
 #   print (token)
#print(t3doc.ents)

print(' ')
print('The Extracted Keywords are : ')
print(' ')
for chunk in t3doc.noun_chunks:
   print(chunk)

ourt3k = open(r'3_NLPandKeyword\\Sample_Text\\Task3Keywords.txt','w')
t3k = (t3doc.ents)

ourt3k.write(str(t3k))

ourt3k.close()
print(' ')

