keypad=['.','abc','def','ghi','jkl','mno','pqrs','tu','vwx','yz']
def keypad_combination(mystr,indx,combination):
    global keypad
    if(indx==len(mystr)):
        print(combination)
        return 0

    currChar=mystr[indx]
    mapping=keypad[ord(currChar)-ord('0')]

    for i in range(len(mapping)):
        keypad_combination(mystr,indx+1,combination+mapping[i])

mystr='2'
keypad_combination(mystr,0,'')