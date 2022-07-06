import re

def RelevanceCheck(LinksArray, Relevence, matchpercent=75):
    """
    This function takes in an array of links and an array of relevence words. It then checks each link
    for the relevence words and returns a sorted array of links with the relevence percentage
    
    :param LinksArray: This is the array of links that you want to check for relevance
    :param Relevence: This is the list of words that you want to match against
    :param matchpercent: This is the minimum percentage of words that must match in order to be
    considered relevant, defaults to 75 (optional)
    :return: a list of links that are relevant to the search query.
    """
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

    """
    It takes two arrays, one with the links and one with the tolerance values, and sorts them in
    descending order
    
    :param linkArray: a list of links.
    :param tolArray: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    :return: the linkArray....
    """
def BubbleSort(linkArray, tolArray):
    n = len(tolArray)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if tolArray[j] < tolArray[j + 1] :
                tolArray[j], tolArray[j + 1] = tolArray[j + 1], tolArray[j]
                linkArray[j], linkArray[j + 1] = linkArray[j + 1], linkArray[j]
    
    return linkArray