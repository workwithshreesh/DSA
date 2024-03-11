def pairStar(mystr,newstr):
    currChar = mystr[0]
    if len(mystr)-1>=1:
        nextChar = mystr[1]
        if currChar == nextChar:
            pairStar(mystr[1:], newstr + currChar + '*')
        else:
            pairStar(mystr[1:], newstr + currChar)

    if len(mystr)-1==0:
        print(newstr+currChar)
        return 0


pairStar('helloo','')



def pairStar(mystr,newstr):
    global nextChar
    currChar = mystr[0]
    if len(mystr)-1>=1:
        nextChar = mystr[1]

    if len(mystr)-1==0:
        print(newstr+currChar)
        return 0

    if currChar == nextChar:
        pairStar(mystr[1:], newstr + currChar + '*')
    else:
        pairStar(mystr[1:], newstr + currChar)

pairStar('hell','')




def pairStar(mystr,indx,newstr):
    currChar = mystr[indx - 1]

    if indx==len(mystr):
        print(newstr+currChar)
        return 0

    nextChar=mystr[indx]

    if currChar==nextChar:
        pairStar(mystr,indx+1,newstr+currChar+'*')
    else:
        pairStar(mystr,indx+1,newstr+currChar)

pairStar('shreesh',1,'')

