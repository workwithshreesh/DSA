a={"the":1,"a":5,10000:"abc"}
print(type(a))

b=a.copy()
print(b)

c=dict([("the",3),("a",32),("abs",34)])
print(c)

d=dict.fromkeys(["abc",32,4])
print(d)
