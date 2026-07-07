class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def reverse_inplace(head):
    p = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = p
        p = cur
        cur = nxt

    return p


def find_max(head):
    if not head:
        return None

    m = head.data
    cur = head

    while cur:
        if cur.data > m:
            m = cur.data
        cur = cur.next

    return m


head = Node(5)
head.next = Node(1)
head.next.next = Node(9)
head.next.next.next = Node(2)

print(find_max(head))

head = reverse_inplace(head)

t = head
while t:
    print(t.data, end=" ")
    t = t.next