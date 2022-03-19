import re

def RelevanceCheck(LinksArray, Relevence, matchpercent=75):
    array = [] 
    numRelevence = len(Relevence)
    for link in LinksArray:
        mCount = 0             # Match count
        for word in Relevence:
            if re.search(word.lower(), link.lower()):
                mCount += 1

        currentpercent = round((mCount/numRelevence) * 100)
        
        if (currentpercent > matchpercent):
            array.append( str(link) + "," + str(currentpercent) ) 
            
    return array