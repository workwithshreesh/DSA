first=-1
last=-1
def findOccurance(strs,element,indx):
    global first, last
    # Base case
    if(len(strs)==indx):
        print(first)
        print(last)
        return 0

    current_char=strs[indx]
    if(current_char==element):
        if (first==-1):
            first=indx
        else:
            last=indx

    findOccurance(strs,element,indx+1)


findOccurance("aabshabaas","a",0)