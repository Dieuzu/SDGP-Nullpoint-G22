#Custom stuff
from researchGap import Search

initiate = Search.SearchWeb # simplifies the method

initiate("NLPResultsExample")          # Uses Default Relevance of 75% and Default delete Cooldown of 30 secs
#initiate("NLPResultsExample", 65)      # Uses Custom Relevance of 65% and Default delete Cooldown of 30 secs
#initiate("NLPResultsExample", 65, 45)  # Uses Custom Relevance of 65% and Custom delete Cooldown of 30 secs