
# First Method of Move all x to end of string
new_string=''
count=''

def move_all_x(mystr,element,indx):
    global new_string,count
    # base case
    if(indx==len(mystr)):
        new_string+=count
        return new_string

    if(mystr[indx]==element):
        count+=element
    else:
        new_string+=mystr[indx]

    return move_all_x(mystr,element,indx+1)

mystr="axbxxxcxd"
print(move_all_x(mystr,"x",0))



# second Method of Move all x to end of string
new_string=''
count=''
def move_all_x(mystr,element,indx):
    global new_string,count

    if (mystr[indx] == element):
        count += element
    else:
        new_string += mystr[indx]

    # base case
    if(indx==len(mystr)-1):
        new_string+=count
        print(new_string)
        return 0

    move_all_x(mystr,element,indx+1)

mystr="axbxxxcxd"
move_all_x(mystr,"x",0)



# Thired method of move all x to end of string

def moveAll(mystr,indx,count,newStr):

    if(indx==len(mystr)):
        for num_of_x in range(count): #use while loop its exception
            newStr+='x'
        print(newStr)
        return 0

    currenChar=mystr[indx]
    if(currenChar=='x'):
        count+=1
        moveAll(mystr,indx+1,count,newStr)
    else:
        newStr+=currenChar
        moveAll(mystr,indx+1,count,newStr)

mystr="axbcxxxd"
moveAll(mystr,0,0,'')
