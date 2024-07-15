def NaiveSearch(v,l):
    for x in l:
        if v==x:
            return(True)
    return(False)





def BinarySearch(v,l):
    if l==[]:
        return(False)
    m = len(l)//2
    if v==m:
        return(True)
    if v<l[m]:
        return(BinarySearch(v,l[:m]))
    else:
        return(BinarySearch(v,l[m+1:]))



l=list(range(0,51,2))
for i in range (0,51):
    print(NaiveSearch(i,l),end=",")
print()
for i in range (0,51):
    print(BinarySearch(i,l),end=",")
print()
