import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeLevelWiseInput():

    q=queue.Queue()
    print("Enter root")
    rootData=int(input("Enter:"))

    if (rootData==-1):
        return None

    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left chiled data ",current_node.data)
        leftChiledData=int(input("Enter"))
        if leftChiledData!=-1:
            current_node.left=BinaryTreeNode(leftChiledData)
            q.put(current_node.left)

        print("Enter right chiled data ",current_node.data)
        rightChiledData=int(input("Enter"))
        if rightChiledData!=-1:
            current_node.right=BinaryTreeNode(rightChiledData)
            q.put(current_node.right)


    return root


def printDetailed(root,prefix="Root: ",level=0):
    if root is not None:
        print(" "*(level*4)+prefix,str(root.data))

        if root.left is not None or root.right is not None:
            printDetailed(root.left,"L--",level+1)
            printDetailed(root.right,"R--",level+1)



root=takeLevelWiseInput()
printDetailed(root)

