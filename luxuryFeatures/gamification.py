from researchGap import Search

def questionOne(fileName):
    print("[SYSTEM] Was the Generated Results useful to you? (yes/y or no/n)")
    userResponse = input("[SYSTEM] Your Reply : ")
    
    if (userResponse.lower() == "y" or userResponse.lower() == "yes"):
        print("[SYSTEM] Thank You for Your Feedback!\n")
        return
    elif (userResponse.lower() == "n" or userResponse.lower() == "no"):
        questionTwo(fileName) # Jumps to next question asking if end user wants to Reduce tolerence and try 
    else:
        print("[SYSTEM] Enterd Input is Not Valid! please try again..\n")
        questionOne(fileName)


def questionTwo(fileName):
    print("[SYSTEM] Would you like to Widen your Search by Reducing your Relevance tolerence percent and trying again?")
    userResponse = input("[SYSTEM] Your Reply : ")
    
    if (userResponse.lower() == "y" or userResponse.lower() == "yes"):
        questionThree(fileName) # Jumps to Next question asking for new Tolerence % 
    elif (userResponse.lower() == "n" or userResponse.lower() == "no"):
        print("[SYSTEM] Thank You for Your Feedback!\n")
        return
    else:
        print("[SYSTEM] Enterd Input is Not Valid! please try again..\n")
        questionTwo(fileName)


def questionThree(fileName):
    try:
        newTolerence = int(input("[SYSTEM] Please Enter the New Relevance Tolerence: "))
        
        if newTolerence not in range(0, 101, 1):
            print("[SYSTEM] Enterd Input is out of range (0-100)! Please try again ...\n")
            questionThree(fileName)
        else:
            print("[SYSTEM] Re-Running the Search with New Relevance Tolerence of " + str(newTolerence) + "%")
            initiate = Search.SearchWeb # Reruns the entire search with lower Tolerence!
            initiate(fileName, newTolerence, 5)
    except ValueError:
        print("[SYSTEM] Enterd Input is Not an Integer! Please try again ...\n")
        questionThree(fileName)