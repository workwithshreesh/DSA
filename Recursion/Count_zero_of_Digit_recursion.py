def countZero(n,sum=0):
    if n==0:
        print(sum)
        return 0
    lastDigit=n%10
    allDigit=n//2
    if lastDigit==0:
        countZero(allDigit,sum+1)
    else:
        countZero(allDigit,sum)

countZero(29809800)
