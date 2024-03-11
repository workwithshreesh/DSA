while True:
    try:
        n = input('Enter numerator')
        num = int(n)
        n = input('Enter denominator')
        denom = int(n)
        if denom==0:  # Custom error raise
            raise ZeroDivisionError
        value = num / denom
        print(value)
        break
    except (ValueError):
        print('Numerater and denominator should be integer')