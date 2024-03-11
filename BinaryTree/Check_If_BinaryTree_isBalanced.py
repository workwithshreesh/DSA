class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():

    rootData = int(input("Enter:"))
    if rootData==-1:
        return

    root=BinaryTreeNode(rootData)

    leftTree=takeInput()
    rightTree=takeInput()

    root.left=leftTree
    root.right=rightTree

    return root


def printTreeDetailed(root,level=0,prefix="Root"):
    if root is not None:
        print(" "*(level*4)+prefix+str(root.data))
        if root.left is not None or root.right is not None:
            printTreeDetailed(root.left,level+1,"L=")
            printTreeDetailed(root.right,level+1,"R=")

    return


def Hight(root):
    if root==None:
        return 0

    return 1+max(Hight(root.left),Hight(root.right))


def isBalanced(root):
    if root==None:
        return True

    h1=Hight(root.left)
    h2=Hight(root.right)

    if h1-h2>1 or h2-h1>1:
        return False

    isLeftBalanced=isBalanced(root.left)
    isRightBalanced=isBalanced(root.right)

    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False



root=takeInput()
printTreeDetailed(root)
ans=isBalanced(root)
print(ans)

