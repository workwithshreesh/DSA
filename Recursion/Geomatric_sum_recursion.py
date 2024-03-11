def geomatric_sum(k,a=1):
    # if a==None:
    #     a=1
    if k==0:
        print(a)
        return 0
    a+=1/(2**k)
    geomatric_sum(k-1,a)

geomatric_sum(3)
