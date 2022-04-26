def Json(filename):
    import json

    strin = filename
    s = ""

    for p in strin:
        if (p == "1"):
            s = p  
        elif (p == "2"):
            s = p
        elif (p == "3"):
            s = p

    dict1 = {}
    fields =['Task']
    with open(filename) as fh:
        l = 1
        for line in fh:
            description = list(line.split(None, 0))
            sno ='assignment'+str(l)
            i = 0
            dict2 = {}
            while i<len(fields):
                    dict2[fields[i]]= description[i]
                    i = i + 1
                    
            dict1[sno]= dict2
            l = l + 1

    out_file = open ('output\\JSONRAW\\Json'+s+'.json', "w")
    json.dump(dict1, out_file, indent = 1)
    out_file.close()