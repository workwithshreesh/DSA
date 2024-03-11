def unique_subsequences(mystr,indx,newStr,sett):
    if(indx==len(mystr)):

        if (sett.__contains__(newStr)):
            return 0
        else:
            print(newStr)
            sett.add(newStr)

        return 0

    currChar=mystr[indx]
    unique_subsequences(mystr,indx+1,newStr+currChar,sett)

    unique_subsequences(mystr,indx+1,newStr,sett)

sett=set({})
mystr='aaa'
unique_subsequences(mystr,0,'',sett)