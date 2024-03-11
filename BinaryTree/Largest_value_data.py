class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():
    rootData = int(input("Enter:"))

    if rootData==-1:
        return

    root = BinaryTreeNode(rootData)

    leftTree = takeInput()
    rightTree = takeInput()

    root.left = leftTree
    root.right = rightTree

    return root



def printDetailed(root):
    if root==None:
        return None

    print(root.data,":",end='')
    if (root.left!=None):
        print("L",root.left.data,end="")

    if (root.right!=None):
        print("R",root.right.data,end='')
    print()
    printDetailed(root.left)
    printDetailed(root.right)



def LargestNode(root):
    if root==None:
        return -1

    leftValue = LargestNode(root.left)
    rightValue = LargestNode(root.right)

    largest = max(leftValue,rightValue,root.data)

    return largest



root = takeInput()
printDetailed(root)
ans = LargestNode(root)
print(ans)

