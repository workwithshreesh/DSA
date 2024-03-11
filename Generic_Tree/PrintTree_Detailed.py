class GenericTree:
    def __init__(self,data):
        self.data=data
        self.childeren=list()


def printTreeDetailed(root):

    if root==None:
        return

    print(root.data,":",end="")
    for chiled in root.childeren:
        print(chiled.data,end=" ")

    print()

    return root

root=GenericTree(1)
n1=GenericTree(2)
n3=GenericTree(3)
n4=GenericTree(4)
n5=GenericTree(5)

root.childeren.append(n1)
root.childeren.append(n3)
n1.childeren.append(n4)
n1.childeren.append(n5)

root=printTreeDetailed(root)
print(root)
