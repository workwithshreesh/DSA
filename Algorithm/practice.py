
def quick(a,low,high):
    pivot=a[high]
    i = low - 1
    for j in range(low,high):
        if a[j]<pivot:
            i += 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    i+=1
    temp=a[i]
    a[i]=pivot
    a[high]=temp
    return i

def partition(a,low,high):
    if low<high:
        pidx=quick(a,low,high)

        low=partition(a,low,pidx-1)
        high=partition(a,pidx+1,high)


a=[4,5,2,6,1]
low=0
high=len(a)-1
partition(a,low,high)
print(a)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(2)
node2=Node(1)
node2.next=node1
print(node2.next.data)



def keypadComb(indx,mystr,newstr):
    lists=['.','abc','def','ghi','jkl','mno','pqr','stu','vwx','yz']
    if indx==len(mystr):
        print(newstr)
        return 0

    currData=mystr[indx]
    Mapping=lists[ord(currData)-ord('0')]
    for i in range(len(Mapping)):
        keypadComb(indx+1,mystr,newstr+Mapping[i])

keypadComb(0,'2','')


comp=[False for i in range(26)]
def duplicate(indx,mystr,newstr,comp):
    if indx==len(mystr)-1:
        print(newstr)
        return 0

    currData=mystr[indx]
    if comp[ord('a')-ord(currData)]==False:
        comp[ord('a')-ord(currData)]=True
        duplicate(indx+1,mystr,newstr+currData,comp)
    else:
        duplicate(indx+1,mystr,newstr,comp)

mystr='aabbccdd'
indx=0
newstr=''
duplicate(indx,mystr,newstr,comp)




def merge_sort(a,a1,a2):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=a2[j]
            j+=1
            k+=1

    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1

    while j<len(a2):
        a[k]=a2[j]
        j+=1
        k+=1


def parttion(a):
    if len(a)==0 or len(a)==1:
        return 0

    dev=len(a)//2
    a1=a[0:dev]
    a2=a[dev:]
    parttion(a1)
    parttion(a2)

    merge_sort(a,a1,a2)

a=[1,9,4,3]
parttion(a)
print(a)


def pivot(a,high,low):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<pivot:
            i+=1
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

    i+=1
    temp=a[i]
    a[i]=pivot
    a[high]=temp
    return i

def quick_sort(a,high,low):
    if low<high:
        pidx=pivot(a,high,low)

        quick_sort(a,pidx-1,low)
        quick_sort(a,high,pidx+1)

a=[2,1,4,3,8,5]
low=0
high=len(a)-1
quick_sort(a,high,low)
print(a)



from collections import deque
a=deque()
for i in range(10):a.append(i),print(a)

for j in range(10):a.popleft(),print(a)

b={'A':['b','c']}
print(b['A'])

def mergeSort(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=a2[j]
            j+=1
            k+=1

    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1

    while j<len(a2):
        a[k]=a2[j]
        j+=1
        k+=1

    return a


def midPoint(a):
    if len(a)==0 or len(a)==1:
        return

    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]

    midPoint(a1)
    midPoint(a2)

    mergeSort(a1,a2,a)


a=[1,3,2,5,4,8]
midPoint(a)
print(a)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sort(head):
    if not head or not head.next:
        return head
    mid_node = find_mid(head)
    h2 = mid_node.next
    mid_node.next = None
    part1 = merge_sort(head)
    part2 = merge_sort(h2)
    merged_list = merge_two_lists(part1, part2)
    return merged_list

def find_mid(head):
    if not head:
        return head
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_two_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    t1, t2, tail, head = head1, head2, None, None

    if t1.val <= t2.val:
        head = t1
        tail = t1
        t1 = t1.next
    else:
        head = t2
        tail = t2
        t2 = t2.next

    while t1 and t2:
        if t1.val <= t2.val:
            tail.next = t1
            tail = t1
            t1 = t1.next
        else:
            tail.next = t2
            tail = tail.next
            t2 = t2.next

    if not t1:
        tail.next = t2
    if not t2:
        tail.next = t1

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Initialize the linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

# Call the merge_sort function
sorted_list = merge_sort(head)

# Print the sorted linked list
print("Sorted linked list:")
print_linked_list(sorted_list)



a=10
b=None
if a is None:
    print(a)
else:
    print(b)

