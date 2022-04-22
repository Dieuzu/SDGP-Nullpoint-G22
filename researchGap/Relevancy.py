import re

def RelevanceCheck(LinksArray, Relevence, matchpercent=75):
    array = []     # this holds links and the relevance %
    Tolerance = [] # this holds the relevance % in the same order as array
    
    numRelevence = len(Relevence)
    
    for link in LinksArray:
        mCount = 0             # Match count (this is number of NLP words that match with the numRelevence)
        for word in Relevence:
            if re.search(word.lower(), link.lower()):
                mCount += 1

        currentpercent = round((mCount/numRelevence) * 100, 2)
        
        if (currentpercent > matchpercent):
            array.append( str(link) + "," + str(currentpercent) + "," ) 
            Tolerance.append(str(currentpercent)) 
    
    sortedArray = BubbleSort(array, Tolerance)
    return sortedArray

def BubbleSort(linkArray, tolArray):
    n = len(tolArray)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if tolArray[j] < tolArray[j + 1] :
                tolArray[j], tolArray[j + 1] = tolArray[j + 1], tolArray[j]
                linkArray[j], linkArray[j + 1] = linkArray[j + 1], linkArray[j]
    
    return linkArray