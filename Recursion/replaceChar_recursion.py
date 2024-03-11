def replaceChar(strings,char1,char2):
    if len(strings)==0:
        return strings

    smalloutput=replaceChar(strings[1:],char1,char2)

    if strings[0]==char1:
        return char2+smalloutput
    else:
        return strings[0]+smalloutput

print(replaceChar('dsxxcdds','d','a'))





# Replace the 2 charecter of String

def replaceStr(Str,x,xn):
    if(len(Str)==0 or len(Str)==1):
        return Str

    smallOutput=replaceStr(Str[1:],x,xn)
    if(Str[:2]==xn):
        return x+smallOutput[1:]
    else:
        return Str[0]+smallOutput

Str='abcdpibbpi'
x='3.14'
xn='pi'
print(replaceStr(Str,x,xn))




def replaceStr(Str):
    if((len(Str)==0) or (len(Str)==0)):
        return Str

    if(Str[0]=='p' and Str[1]=='i'):
        smallOutput=replaceStr(Str[2:])
        return '3.14'+smallOutput
    else:
        smallOutput=replaceStr(Str[1:])
        return Str[0]+smallOutput

print(replaceStr('absdpibdsj'))
