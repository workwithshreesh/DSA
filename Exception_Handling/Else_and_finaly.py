# Else with try
class ZeroDenominatorError(ZeroDivisionError): # ZeroDivisionError is parent class of user defined error
    pass
while 1:
    try:
        n=input('Enter numerator')
        num=int(n)
        n=input('Enter denominator')
        denom=int(n)
        if denom==0:
            raise ZeroDenominatorError('Denominator should not be zero')
    except(ZeroDivisionError):
        print('Denominator is always greater then zeero')
    else:
        value = (num / denom)
        print(value)
        break







class ZeroDenominatorError(ZeroDivisionError):
    pass
while True:
    try:
        n=input('Enter numerator')
        num=int(n)
        n=input('Enter denominator')
        denom=int(n)

        if denom==0:
            raise ZeroDenominatorError('Denominator should not be zero')

    except(ZeroDivisionError):
        print('Denominator is always greater then zeero')

    else:
        value = (num / denom)
        print(value)
        break
    finally:
        print('Exception raised may or may not be')