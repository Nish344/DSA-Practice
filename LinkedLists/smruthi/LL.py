class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

def find_max(head):
        if not head:
            return None
        mv=head.data
        cur=head.next
        
        while cur:
            if cur.data > mv:
                mv=cur.data
            cur=cur.next
        return mv

def reverse_inplace(head):
    if not head :
        return None
    prev =None
    cur = head
    while cur:
        temp=cur.next
        cur.next=prev
        prev=cur
        cur=temp
    return prev
     

head=Node(10)
head.next=Node(50)
head.next.next=Node(15)
head.next.next.next=Node(25)
head.next.next.next.next=Node(1000)

temp=head
while temp :
    print(temp.data)
    temp=temp.next

print("Max of all the numbers in the LinkedList is ",find_max(head))
head = reverse_inplace(head)
print("The reverse of the Linked List :")
temp=head
while temp:
    print(temp.data)
    temp=temp.next
 
