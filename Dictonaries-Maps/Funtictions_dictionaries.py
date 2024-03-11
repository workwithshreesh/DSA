a={1:2,3:4,"List":[1,24],"Dict":{1:4}}
print(a)

print(a["List"])
print(a["Dict"][1])
print(a[1])

print(a.get("List"))

# it will return value of key if key is present otherwise print second value
print(a.get("Li","Not Available"))

print(a.values())
print(a.keys())

print(a.items())

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

for i,j in a.items():
    print(i,j)

print("List" in a)
