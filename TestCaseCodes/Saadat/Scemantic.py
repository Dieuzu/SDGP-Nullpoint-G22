from semanticscholar import SemanticScholar

sch = SemanticScholar(timeout=2)
paper = sch.paper('10.1145/967900.968165') # Need this 

#paper.keys()
#dict_keys(['abstract', 'arxivId', 'authors', 'citationVelocity', 'citations', 'doi','influentialCitationCount', 'paperId', 'references', 'title', 'topics', 'url', 'venue', 'year'])

Authors ="\nPaper Authors :"

print("\n===========================================================================================================================================================================================================================")
print("\nPaper Title : " + paper['title'])

for author in paper['authors']:
    Authors = Authors + " " + author['name']

print(Authors)

print("\nPaper Abstract : " + paper['abstract'])

print("\n===========================================================================================================================================================================================================================")


#print("\nPapaer Title : " + (author['authorId'])
