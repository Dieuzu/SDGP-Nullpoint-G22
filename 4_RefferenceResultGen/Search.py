#this is the first early prototype to searching the net 

import re
import RecomendWeb
import os # this for deleting files 
import time
import Relevency

RelevancyPercent = 20

def main():
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
        print("Terminating Search....")
        quit()

    SearchResults = []   # this stores all results in this array
    RelevantResults = [] # this Stores all the results and the % of relevancy
    RefinedResults = []  # this where only refined results are stored
    
    coreDomains = ["geeksforgeeks", "oracle", ".edu/", ".pdf", "w3schools", "freecodecamp", "codecademy", "javatpoint", "semanticscholar"] #Core domains to get results from
    
    rnlp = open('4_RefferenceResultGen\\NLPResults.txt','r')

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

    def BaseSearch(String, ResultNum):
        for j in search(String, tld="co.uk", num=ResultNum, stop=ResultNum, pause=2):
            SearchResults.append(str(j))
            #All below extra
            f = open("4_RefferenceResultGen\TestFolder\RawSearch.txt", "a") 
            f.write(j+"\n")
            f.close()
    
    print ("[SYSTEM] Running a base Search on Google with NLP Result...")
    BaseSearch(pdfQuery,20)        
    print ("[SYSTEM] Running a PDF file Search on Google with NLP Result...")
    BaseSearch(query, 20)
    print ("[SYSTEM] Running a Scemantic schoalar Search with NLP Result...")
    BaseSearch(SSchQuery,20)
    #==================================================================================================================================
    print ("[SYSTEM] Deleting any Duplicate links from all Search Results")
    SearchResults = list(dict.fromkeys(SearchResults)) #this ensures no duplicates in lines 
    
    print ("[SYSTEM] Checking Match Relevancy of links to the NLP Results (Current match % = " + str(75)+ "% or Greater)")
    RelevantResults = Relevency.RelevanceCheck(SearchResults, SplitNLP, RelevancyPercent)

    print ("[SYSTEM] Checking all Relevant links against Notable and acedemic Core Domains!")   

    for links in RelevantResults:
        for domains in coreDomains:
            if re.search(domains, links):
                #this is for the array:
                RefinedResults.append(links)
                #this is for the Text file:
                f = open("4_RefferenceResultGen\TestFolder\Refined_Links.txt", "a")
                f.write(links+"\n")
                f.close()
                break
    
    print ("[SYSTEM] RefinedResults.txt Created")

    print ("[SYSTEM] Running the RecomendWeb Module...")
    RecomendWeb.main()

    time.sleep(5)   # Delays for 5 seconds. can also use a float value.   

    # this is to delete the unwanted search results text file this wont exist after i import them to classes           
    if os.path.exists("4_RefferenceResultGen\TestFolder\RawSearch.txt") and os.path.exists("4_RefferenceResultGen\TestFolder\Refined_Links.txt"):
        os.remove("4_RefferenceResultGen\TestFolder\RawSearch.txt")
        os.remove("4_RefferenceResultGen\TestFolder\Refined_Links.txt")
        print("\n[SYSTEM] Deleted the files RawSearch.txt and Refined_Links.txt")
    else:
        print("[SYSTEM] The files does not exist Continuing")

#============================================================for later
if __name__ == "__main__":
    main()    