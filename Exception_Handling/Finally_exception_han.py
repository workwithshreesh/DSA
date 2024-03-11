# Finally will raise every time whenever exception are there or not
try:
    n=input('Enter numerator')
    num=int(n)
    n=input('Enter denominator')
    denom=int(n)
    value=num/denom
    print(value)
except(ZeroDivisionError):
    print('Exception:> Denominator should not be zero')
finally:
    print('Finally:> Exception may be raised or not')