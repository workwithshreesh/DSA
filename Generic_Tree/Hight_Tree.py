import queue
class GenericTree:
    def __init__(self,data):
        self.data=data
        self.chiledren=list()


def takeInput():
    q=queue.Queue()

    rootData=int(input("Enter root data:"))

    if rootData==-1:
        return None

    root=GenericTree(rootData)
    q.put(root)
    while (not q.empty()):
        currentNode=q.get()
        print("Enter number of chiled for",currentNode.data)
        numChiledren=int(input(":"))
        for i in range(numChiledren):
            print("Enter chiled of",currentNode.data)
            chiledData=int(input(":"))
            chiled=GenericTree(chiledData)
            root.chiledren.append(chiled)
            q.put(chiled)

    return root

def printTreeDetailed(root):
    if root==None:
        return None
    print(root.data,":",end="")
    for chiled in root.chiledren:
        print(chiled.data,end=" ")

    print()


def printHightTree(root):
    if root==None:
        return 0

    max_hight=0
    for i in root.chiledren:
        max_hight=max(max_hight,printHightTree(i))

    return 1+max_hight

root=takeInput()
printTreeDetailed(root)
hight=printHightTree(root)
print("Hight :",hight)
