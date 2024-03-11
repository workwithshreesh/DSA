def CalcFactorial(n):
    if (n==0):
        return 1
    return n * CalcFactorial(n-1)

print(CalcFactorial(1))

'''
factorial(5) 
   factorial(4) 
      factorial(3) 
         factorial(2) 
            factorial(1) 
               return 1 
            return 2*1 = 2 
         return 3*2 = 6 
      return 4*6 = 24 
   return 5*24 = 120
'''