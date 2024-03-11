class GenericTree:
    def __init__(self,data):
        self.data=data
        self.chiledren=list()


def treeInput():
    rootData=int(input("Root Data"))

    if rootData==-1:
        return None

    root=GenericTree(rootData)

    print("Enter the number of chiledren for root data:",root.data)
    chiledNode=int(input())
    for i in range(chiledNode):
        chiled=treeInput()
        root.chiledren.append(chiled)

    return root


def printtree(root):
    if root==None:
        return

    print(root.data,":",end="")
    for chiled in root.chiledren:
        print(chiled.data,end=" ")

    print()


def sumOfTree(root):
    sum=0

    if root==None:
        return

    for chiled in root.chiledren:
        sum+=chiled.data

    return sum

root=treeInput()
printtree(root)
print(sumOfTree(root))
