#Custom stuff
from dependancies import installPackage #this will check if all dependancies are installed if not it will start chain to install all of them!
from researchGap import Search

initiate = Search.SearchWeb # simplifies the method

initiate("NLPResultsExample", 80, 120) # this is TEST CODE relevancy tollerance set to 25% and CD set to 5 secs!

# there are  3 Ways to the Initiate Method for Recomended reseults (see below comments) 

#initiate("NLPResultsExample")          # Uses Default Relevance of 75% and Default delete Cooldown of 30 secs
#initiate("NLPResultsExample", 55)      # Uses Custom Relevance of 55% and Default delete Cooldown of 30 secs
#initiate("NLPResultsExample", 65, 45)  # Uses Custom Relevance of 65% and Custom delete Cooldown of 45 secs