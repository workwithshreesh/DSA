# First Method sum of n natural number using recursion

def sum_of_n(n,base_condition, sum_n):
    if (n==base_condition):
        sum_n+=n
        print(sum_n)
        return 0
    sum_n+=n
    sum_of_n(n+1,base_condition,sum_n)

sum_of_n(1,5,0)



# Second Method sum of n natural number using recursion

def sum_of_n(n):
    if (n==0):
        return 0
    smalloutput=sum_of_n(n-1)
    output=smalloutput+n
    return output

print(sum_of_n(5))




# Third Method sum of n natural number

def sum_of_n(n,base_con,sum_n):
    if(n>base_con):
        return 0
    sum_n+=n
    print(sum_n)
    sum_of_n(n+1,base_con,sum_n)

sum_of_n(1,5,0)





# Fourth Method sum of n natural number

def sum_of_n(n):
    if(n==0):
        return 0
    return n+sum_of_n(n-1)

print(sum_of_n(5))

'''
sum_of_n(5) 
   sum_of_n(4) 
      sum_of_n(3) 
         sum_of_n(2) 
            sum_of_n(1) 
               sum_of_n(0) base case true
               return 0+1 = 1
            return 1+2 = 3 
         return 3+3 =  6
      return 4+6 = 10 
   return 5+10 = 15
'''