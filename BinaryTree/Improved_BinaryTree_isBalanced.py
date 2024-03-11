class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput():

    rootData = int(input("Enter:"))

    if rootData==-1:
        return None

    root=BinaryTreeNode(rootData)

    leftInput=takeInput()
    rightInput=takeInput()

    root.left=leftInput
    root.right=rightInput

    return root


def printDetail(root):

    if root==None:
        return

    print("Root:",root.data)

    if root.left!=None:
        print("L",root.left.data,end="")

    if root.right!=None:
        print("R",root.right.data,end="")

    print()

    printDetail(root.left)
    printDetail(root.right)


def GetHightCheckisBalanced(root):

    if root==None:
        return 0,True

    lh, isLeftBalanced=GetHightCheckisBalanced(root.left)
    rh, isRightBalanced=GetHightCheckisBalanced(root.right)

    h=1+max(lh,rh)

    if lh-rh>1 or rh-lh>1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h,False


def isBalanced2(root):
    h, isBalanced=GetHightCheckisBalanced(root)
    return isBalanced


root=takeInput()
printDetail(root)
ans=GetHightCheckisBalanced(root)
print(ans)
ans=isBalanced2(root)
print(ans)
