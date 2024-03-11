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

        i=i+1

        if i<len(input_list) and input_list[i]!=-1:
            current_node.right=BinaryTreeNode(input_list[i])
            queue.append(current_node.right)
        i=i+1

    return root


def printDetail(root):
    if root is None:
        return

    print("Root",root.data,":",end="")
    if root.left!=None:
        print("L",root.left.data,end="")

    if root.right!=None:
        print("R",root.right.data,end="")

    print()
    printDetail(root.left)
    printDetail(root.right)

def NumberOfLeaf(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    Left=NumberOfLeaf(root.left)
    Right=NumberOfLeaf(root.right)

    return Left + Right

input_list=list(map(int,input("Enter:").split()))
root=takeInput(input_list)
printDetail(root)
print()
ans=NumberOfLeaf(root)
print(ans)
