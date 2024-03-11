class GenericNode:
    def __init__(self,data):
        self.data=data
        self.chilederen=[]


def takeInput():

    rootData=int(input("Enter root data"))
    if rootData==-1:
        return

    root=GenericNode(rootData)

    print("Enter number of chilederen for",rootData)
    chiledrenData = int(input())

    for i in range(chiledrenData):
        chiled = takeInput()
        root.chilederen.append(chiled)

    return root


def printDetailed(root):

    if root==None:
        return None

    print(root.data,":",end="")
    for chiled in root.chilederen:
        print(chiled.data,end=" ")
    print()



root=takeInput()
printDetailed(root)




