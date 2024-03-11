class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def takeInput(input_list):

    if input_list==None:
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

        if i<len(input_list) and current_node!=-1:
            current_node.right=BinaryTreeNode(input_list[i])
            queue.append(current_node.right)

        i+=1

    return root

def printDetail(root):
    if root is None:
        return None

    print("Root",root.data,":",end="")
    if root.left!=None:
        print("R",root.left.data,end="")

    if root.right!=None:
        print("L",root.right.data,end="")

    print()
    printDetail(root.left)
    printDetail(root.right)


def printKdepth(root,k):
    if root == None:
        return

    if k==0:
        print("Leaf Node",":",root.data)
        return

    printKdepth(root.left,k-1)
    printKdepth(root.right,k-1)

input_list=list(map(int,input("Enter:").split()))
root=takeInput(input_list)
printDetail(root)
printKdepth(root,2)
