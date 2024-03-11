list1=[False for i in range(26)]
def removeDuplicates(Mystr,indx,newStr):
    global list1
    if(indx==len(Mystr)):
        print(newStr)
        return 0

    currChar=Mystr[indx]
    if(list1[ord(currChar)-ord('a')]==True):
        removeDuplicates(Mystr,indx+1,newStr)
    else:
        newStr+=currChar
        list1[ord(currChar)-ord('a')]=True
        removeDuplicates(Mystr,indx+1,newStr)

Mystr='abbcdcd'
removeDuplicates(Mystr,0,'')