# Reverse string method 1
def reverse_str(rev,str,n):
    len_calc = len(str)

    if (len(rev)==len_calc):
        print(rev)
        return 0

    reverse_str(rev+str[len_calc-n],str,n+1)

reverse_str("","rececar",1)



# Reverse string method 2
def reverse_str(rev,str,n):
    len_calc = len(str)

    if (len(rev)==len_calc):
        print(rev)
        return 0

    reverse_str(rev+str[-n],str,n+1)

reverse_str("","string",1)



# Thired method of reverse string
def reverse_str(mystr,indx):
    if (indx==0):
        print(mystr[indx])
        return 0
    print(mystr[indx],end="")
    reverse_str(mystr,indx-1)
