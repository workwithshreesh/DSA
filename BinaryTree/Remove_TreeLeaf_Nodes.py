class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput(input_list):

    if input_list==None:
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


def printTreeDetailed(root):
    if root is None:
        return None

    print("Root",root.data,":",end="")
    if root.left!=None:
        print("L",root.left.data,end="")

    if root.right!=None:
        print("R",root.right.data,end="")

    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def removeLeaf(root):
    if root == None:
        return None

    if root.left is None and root.right is None:
        return None

    root.left=removeLeaf(root.left)
    root.right=removeLeaf(root.right)

    return root



input_list=list(map(int,input("Enter:").split()))
root=takeInput(input_list)
printTreeDetailed(root)
ans=removeLeaf(root)
printTreeDetailed(ans)

