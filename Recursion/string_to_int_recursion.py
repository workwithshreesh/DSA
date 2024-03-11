def strToNum(mystr):
    l=len(mystr)-1
    if l<1:
        if l==0:
            return int(mystr)
        return 0

    b=int(mystr[0])
    a=int(mystr[1:])

    strToNum(mystr[1:])
    return b*(10**l)+a
mystr='347809'
strToNum(mystr)







def solveint(mystr):
    l=len(mystr)
    if l==0:
        return 0

    smallAnswer=solveint(mystr[0:l-1])
    nextDigit=ord(mystr[l-1])-ord('0')
    finalAnswer=(smallAnswer*10)+nextDigit

    return finalAnswer

mystr='211043'
a=solveint(mystr)
print(a)