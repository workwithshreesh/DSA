def reverseStack(n,stack1,stack2):

    if not stack1:
        return 0

    stack2.append(stack1[n])
    stack1.pop()
    reverseStack(n-1,stack1,stack2)
    stack1.append(stack2[n])
    if len(stack1)-1==len(stack2)-1:
        while stack2:
            stack2.pop()

stack1=[1,2,3,4,5]
stack2=[]
n=len(stack1)-1
reverseStack(n,stack1,stack2)
print(stack1)



#second mathod
def reverseStack(stack1,stack2):
    if len(stack1)<=1:
        return

    while (len(stack1)!=1):
        ele=stack1.pop()
        stack2.append(ele)

    lastElement=stack1.pop()

    while (len(stack2)!=0):
        ele=stack2.pop()
        stack1.append(ele)

    reverseStack(stack1,stack2)
    stack1.append(lastElement)

stack1=[1,2,3,4,5]
stack2=[]
reverseStack(stack1,stack2)
print(stack1)


