class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def buildTreefromPreIn(pre,inorder):
    if len(pre)==0:
        return None

    rootData = pre[0]
    root=BinaryTreeNode(rootData)
    rootIndexInInorder=-1

    for i in range(0,len(inorder)):
        if inorder[i]==rootData:
            rootIndexInInorder=i
            break

    if rootIndexInInorder==-1:
        return None

    leftInorder=inorder[0:rootIndexInInorder]
    rightInorder=inorder[rootIndexInInorder+1:]

    lenLeftSubtree=len(leftInorder)

    leftPreorder=pre[1:lenLeftSubtree+1]
    rightPreorder=pre[lenLeftSubtree+1:]

    leftChiled = buildTreefromPreIn(leftPreorder,leftInorder)
    rightChiled= buildTreefromPreIn(rightPreorder, rightInorder)

    root.left = leftChiled
    root.right = rightChiled

    return root


def printDetailed(root):

    if root==None:
        return None

    print("Root: ",root.data,end="")

    if root.left!=None:
        print("L",root.left.data,end="")

    if root.right!=None:
        print("R",root.right.data,end="")

    print()

    printDetailed(root.left)
    printDetailed(root.right)


pre=[1,2,4,5,3,7]
Inorder=[4,2,5,1,6,3,7]
root=buildTreefromPreIn(pre,Inorder)
printDetailed(root)
