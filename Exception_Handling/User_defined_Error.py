class ZeroDenomError(Exception):
    pass

while True:
    try:
        n=input('Enter numerator')
        num=int(n)
        n=input('Enter denominetor')
        denom=int(n)
        if denom==0:
            raise ZeroDenomError('Zero denominetor error')
        value=num/denom
        print(value)
    except(ValueError):
        print('Numerator Denominator should be zero')




class ZeroDenomError(Exception):
    pass

while True:
    try:
        n=input('Enter numerator')
        num=int(n)
        n=input('Enter denominetor')
        denom=int(n)
        if denom==0:
            raise ZeroDenomError('Zero denominetor error')
        value=num/denom
        print(value)
    except(ValueError):
        print('Numerator Denominator should be zero')
    except(ZeroDenomError):
        print('Zero is not allowed in denominator')
