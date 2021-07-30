def convertFive(n):
    strnum= str(n)
    newstr=""
    for i in range(len(strnum)):
        if strnum[i]=="0":
            newstr+="5"
        else:
            newstr+=strnum[i]
    
    return newstr
