def checkAB(mystr):
    s=len(mystr)
    if s==1 or s==2:
        if mystr=='a' or mystr=='bb':
            return True
        return 0
    if s>=3:
        if mystr[0]=='a':
            if mystr[1:3]=='bb':
                return True
            else:
                return False

        if mystr[:2]=='bb':
            if mystr[2]=='a':
                return True
            else:
                return False

print(checkAB('bba'))