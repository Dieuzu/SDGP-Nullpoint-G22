import re

NLPResult = "Java Difference Abstract Interface class OOP Java Difference Abstract Interface"

Links = [   
            "http://ocw.ump.edu.my/mod/resource/view.php?id=2840",
            "https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/recitations/MIT1_00S12_REC_6.pdf",
            "https://www.guru99.com/interface-vs-abstract-class-java.html",
            "https://www.javatpoint.com/difference-between-abstract-class-and-interface",
            "https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-java/",
            "https://www.baeldung.com/java-interface-vs-abstract-class",
            "https://www.delftstack.com/howto/java/abstract-class-vs-interface-java/",
            "https://stackoverflow.com/questions/761194/interface-vs-abstract-class-general-oo",
            "https://stackoverflow.com/questions/1913098/what-is-the-difference-between-an-interface-and-abstract-class",
            "https://stackoverflow.com/questions/18777989/how-should-i-have-explained-the-difference-between-an-interface-and-an-abstract",
            "https://stackoverflow.com/questions/10040069/abstract-class-vs-interface-in-java",
            "https://stackoverflow.com/questions/479142/when-to-use-an-interface-instead-of-an-abstract-class-and-vice-versa",
            "https://www.edureka.co/blog/difference-between-abstract-class-and-interface",
            "https://www.tutorialspoint.com/differences-between-abstract-class-and-interface-in-java",
            "https://beginnersbook.com/2013/05/abstract-class-vs-interface-in-java/",
            "https://www.simplilearn.com/abstract-class-vs-interface-java-article",
            "https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html",
            "https://java.tutorials24x7.com/blog/interface-vs-abstract-class-in-java",
            "https://pediaa.com/what-is-the-difference-between-abstract-class-and-interface-in-java/",
            "https://www.linkedin.com/pulse/what-difference-between-interface-abstract-class-david-ramazani",
            "https://www.quora.com/What-is-the-difference-between-an-abstract-class-and-an-interface-in-OOP",
            "https://javapapers.com/core-java/abstract-and-interface-core-java-2/difference-between-a-java-interface-and-a-java-abstract-class/",
            "https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-java/",
            "https://www.semanticscholar.org/paper/Interfaces-with-default-implementations-in-Java-Mohnen/23ba73a7a71239cabc1b66ec12cf9db075cb11f1",
        ]

def RelevanceCheck(html, Relevence):
    count = 0
    for x in range(len(html)):
        for y in range(len(Relevence)):
            if re.search(Relevence[y].lower(), html[x].lower()):
                count += 1
    nRelevence = len(Relevence)
    y = (count/nRelevence) * 100
    return y

SplitCore = NLPResult.split(" ")

SplitCore = list(dict.fromkeys(SplitCore))

Goodcount = 0
Badcount = 0
matchPercent = 75

print("======================================================================================================================================")
for x in range (len (Links)):
    Single = [Links[x]]
    SingleMatch = round (RelevanceCheck(Single, SplitCore), 2)
    if (SingleMatch > matchPercent):
        Goodcount+=1
        print ("The link " + str(Goodcount) + " : \n" + str(Single) + "\n has a " + str(SingleMatch) + "% Relevance with NLP results\n")
    else:
        Badcount+=1
print("======================================================================================================================================")
print ("Sucessfully found " + str(Goodcount) + " number of Results with over "+ str(matchPercent) +"% accuracy and " + str(Badcount) + " number of uslesss links")
print("======================================================================================================================================")