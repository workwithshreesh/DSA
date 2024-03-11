
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def takeInput(input_list):

    if not input_list:
        return None

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

    return root



def printDetailed(root,level=0,prefix="Root"):
    if root is not None:
        print(" "*(level*4)+prefix+str(root.data))
        if root.left is not None or root.right is not None:
            printDetailed(root.left,level+1,"R--")
            printDetailed(root.right,level+1,"L--")



def RplaceNode(root,level=0):
    if root==None:
        return None
    else:
        root.data=level
        RplaceNode(root.left,level+1)
        RplaceNode(root.right,level+1)

    return root


input_list=list(map(int,input("Enter").split()))
root=takeInput(input_list)
printDetailed(root)
print()
root1=RplaceNode(root)
printDetailed(root1)
