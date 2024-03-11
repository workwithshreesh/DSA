import queue

import Queues

class GenericTree:
    def __init__(self,data):
        self.data=data
        self.chileren=[]


def takeInput():
    q=queue.Queue()
    rootData=int(input("Enter a root:"))
    if rootData==-1:
        return None

    root = GenericTree(rootData)
    q.put(root)
    while (not q.empty()):
        currentNode=q.get()
        print("Enter num of children for",currentNode.data)
        numChildren=int(input(":"))
        for i in range(numChildren):
            print("Enter next chiled for",currentNode.data)
            chiledData=int(input(":"))
            child=GenericTree(chiledData)
            currentNode.chileren.append(child)
            q.put(child)

    return root



def printTree(root):

    if root==None:
        return None

    print(root.data,":",end="")
    for chiled in root.chileren:
        print(chiled.data,",",end="")

    print()

    for chiled in root.chileren:
        print(chiled.data)

root=takeInput()
printTree(root)
