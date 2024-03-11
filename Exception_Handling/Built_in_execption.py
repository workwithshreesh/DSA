while True:
    try:
        n = input('Enter the numerator')
        num = int(n)
        n = input('Enter the denominator')
        denom = int(n)
        value = num / denom
        print(value)
        break
    except(ValueError,ZeroDivisionError):
        print('Numerator and denominator should be integer and denominator should not be zero')







while True:
    try:
        n = input('Enter the numerator')
        num = int(n)
        n = input('Enter the denominator')
        denom = int(n)
        value = num / denom
        print(value)
        break
    except(ValueError):
        print('Numerator and denominator should be integer')
    except(ZeroDivisionError):
        print('Denominator should not be zero')
