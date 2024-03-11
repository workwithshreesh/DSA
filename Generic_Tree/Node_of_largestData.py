import queue

class GenericTree:
    def __init__(self,data):
        self.data=data
        self.chiledren=[]


def takeInput():
    q=queue.Queue()
    rootData=int(input("Enter a root"))
    if rootData==-1:
        return None

    root=GenericTree(rootData)
    q.put(root)

    while (not q.empty()):
        currentNode=q.get()
        print("Enter number of chiled for",currentNode.data)
        numChiledren=int(input(":"))
        for i in range(numChiledren):
            print("Enter chiled for",currentNode.data)
            chiledData=int(input(":"))
            chiled=GenericTree(chiledData)
            root.chiledren.append(chiled)
            q.put(chiled)

    return root



def printTree(root):

    if root==None:
        return None

    print(root.data,":",end="")
    for chiled in root.chiledren:
        print(chiled.data,end=" ")

    print()



def largest_Node_data(root):

    largest=0
    if root==None:
        return None

    for chiled in root.chiledren:
        for chiled2 in root.chiledren:
            if chiled.data>chiled2.data:
                largest=chiled.data

    return largest

root=takeInput()
printTree(root)
print(largest_Node_data(root))
