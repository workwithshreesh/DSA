class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None




def takeInput(input_list):

    if not input_list:
        return

    root=BinaryTreeNode(input_list[0])
    queue=[root]
    i=1

    while i<len(input_list):

        current_node=queue.pop(0)

        if input_list[i]!=-1:
            current_node.left=BinaryTreeNode(input_list[i])
            queue.append(current_node.left)

        i+=1

        if i<len(input_list) and input_list[i]!=-1:
            current_node.right=BinaryTreeNode(input_list[i])
            queue.append(current_node.right)

        i+=1
    return root




def printTreeDetailed(root,level=0,prefix="Root"):

    if root is not None:
        print(" "*(level*4)+prefix+str(root.data))
        if root.left is not None or root.right is not None:
            printTreeDetailed(root.left,level+1,"L--")
            printTreeDetailed(root.right,level+1,"R--")




def hight(root):
    if root is None:
        return 0

    return max(hight(root.left),hight(root.right))+1




def DiameterOfTree(root):
    if root is None:
        return 0
    else:
        leftHight=hight(root.left)
        rightHight=hight(root.right)
        leftDiameter=DiameterOfTree(root.left)
        rightDiameter=DiameterOfTree(root.right)

        return max(leftHight+rightHight+1,max(leftDiameter,rightDiameter))




input_list=list(map(int,input("Enter:").split()))
root=takeInput(input_list)
printTreeDetailed(root)
ans=DiameterOfTree(root)
print(ans)
