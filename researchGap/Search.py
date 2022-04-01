# Built in stuff
import re

#Custom stuff i made
from researchGap import RecommendWeb
from researchGap import Relevancy
from researchGap import Delete

#this is needed to Do a google Search we throw it into a try except to kill entire thing in event it cannot be imported!
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    print("Terminating Search....")
    quit()

#this is a function to webscrape (it requires Search String, number of results to look up and an array to store them into)
def BaseSearch(String, ResultNum, SearchArray):
    for j in search(String, tld="co.uk", num=ResultNum, stop=ResultNum, pause=2):
        SearchArray.append(str(j))
        #All below extra nuke later
        f = open("output\\SearchResults\\RawSearch.txt", "a") 
        f.write(j+"\n")
        f.close()
    return SearchArray

def SearchWeb (FileName, Relevence = 75, Cooldown = 30): #Cooldown = time to delete created files default set to 30 secs
    
    RelevancyPercent = Relevence # this is the tolerence for relevancy

    SearchResults = []   # this stores all results in this array
    RelevantResults = [] # this Stores all the results and the % of relevancy
    RefinedResults = []  # this where only refined results are stored

    coreDomains = ["geeksforgeeks", "oracle", ".edu/", ".pdf", "w3schools", "freecodecamp", "codecademy", "javatpoint", "semanticscholar"] #Core domains to get results from

    rnlp = open("output\\NLP\\" + str(FileName) +".txt","r")

    print ("\n=============================================== Saadat's Component ===============================================")
    print ("[SYSTEM] Getting NLP Results from directory... ")
    NLPString = rnlp.readline() 

    SplitNLP = NLPString.split(" ")
    SplitNLP = list(dict.fromkeys(SplitNLP))

    print("[SYSTEM] NLP Result = " + str(SplitNLP)) #<=================== COMMENT THIS LINE OUT AT THE END!!!!!!!!! 

    #==================================================================================================================================
    #runs the Search from the details stored in class
    query = NLPString
    pdfQuery = query + " filetype:pdf"
    SSchQuery = query + " semanticscholar"

    #print("Generating Refined Results Needed for Subtask " + idNumber +"....")

    print ("[SYSTEM] Running a base Search on Google with NLP Result...")
    SearchResults = BaseSearch(pdfQuery,20, SearchResults)        
    print ("[SYSTEM] Running a PDF file Search on Google with NLP Result...")
    SearchResults = BaseSearch(query, 20, SearchResults)
    print ("[SYSTEM] Running a Scemantic schoalar Search with NLP Result...")
    SearchResults = BaseSearch(SSchQuery,20, SearchResults)
    
    print ("[SYSTEM] Deleting any Duplicate links from all Search Results")
    SearchResults = list(dict.fromkeys(SearchResults)) #this ensures no duplicates in lines 
    
    # this checks each link and its relevancy to the NLP Keywords it also identifies the relevency based on the tolerance set!
    print ("[SYSTEM] Checking Match Relevancy of links to the NLP Results (Current match tolerance = " + str(RelevancyPercent)+ "% or Greater)")
    RelevantResults = Relevancy.RelevanceCheck(SearchResults, SplitNLP, RelevancyPercent)

    print ("[SYSTEM] Checking all Relevant links against Notable and Academic Domains!")   

    for links in RelevantResults:
        for domains in coreDomains:
            if re.search(domains, links):
                #this is for the array:
                RefinedResults.append(links)
                #this is for the Text file:
                f = open("output\\SearchResults\\Refined_Links.txt", "a")
                f.write(links+"\n")
                f.close()
                break

    print ("[SYSTEM] RefinedResults.txt Created")

    print ("[SYSTEM] Running the RecomendWeb Module...")
    RecommendWeb.CreateRecomendPage()

    Delete.residualDel(Cooldown)
