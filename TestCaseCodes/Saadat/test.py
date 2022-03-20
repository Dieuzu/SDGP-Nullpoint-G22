# this was base code for refining search results to specific domains

import re
links = ["https://stackoverflow.com/questions/5835311/what-is-the-advantage-of-interface-over-abstract-classes", "https://stackoverflow.com/questions/25214075/why-cant-an-abstract-class-extend-an-interface", "https://stackoverflow.com/questions/1814821/interface-or-an-abstract-class-which-one-to-use", "https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html", "https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-java/", "https://www.geeksforgeeks.org/implement-interface-using-abstract-class-in-java/"]
   
      
core = ["stackoverflow","geeksforgeeks", "oracle"]


for x in range(len(links)):
      for y in range(len(core)):
        if re.search(core[y], links[x]):
            print(links[x])
