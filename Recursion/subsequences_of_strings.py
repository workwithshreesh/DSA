def subsequences(mystr,indx,newStr):
    if(indx==len(mystr)):
        print(newStr)
        return 0

    currChar=mystr[indx]
    subsequences(mystr,indx+1,newStr+currChar)

    subsequences(mystr,indx+1,newStr)

mystr='abc'
subsequences(mystr,0,'')