class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, end='')
    if root.left != None:
        print("L",root.left.data,end='')
    if root.right != None:
        print("R",root.right.data,end='')

    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

root = takeInput()
printTreeDetailed(root)





