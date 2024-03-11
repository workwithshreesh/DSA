def sum_of_digits(n,sum=0):
    mystr=str(n)
    if len(mystr)==0:
        print(sum)
        return 0
    sum+=int(mystr[-1])

    sum_of_digits(mystr[:-1],sum)

sum_of_digits(12345)