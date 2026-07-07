class Node:
    def __init__(self, value=-1):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        res = ""
        curr = self.head.next
        while curr != self.tail:
            res += str(curr.data) + "->"
            curr = curr.next
        return res.strip("->")

    def insert_before_tail(self, val):
        new_node = Node(value=val)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        new_node.prev.next = new_node
        self.tail.prev = new_node
        return new_node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


def main():
    def test_insert_before_tail():
        vals = [1, 2, 3, 4]  # h -> 1 -> 2-> 2-> 4 -> t
        dll = LinkedList()
        for ele in vals:
            dll.insert_before_tail(ele)
            print(dll)

    def test_remove_node():
        vals = [1, 2, 3, 4]  # h -> 1 -> 2 -> 3-> 4 -> t
        # remove(2) => # h -> 1 -> 3-> 4 -> t. Removed in O(1)
        nodes = []
        dll = LinkedList()
        for ele in vals:
            nodes.append(dll.insert_before_tail(ele))
            print(dll)
        # print(nodes)
        dll.remove_node(nodes[1])
        print(dll)

    test_insert_before_tail()
    test_remove_node()


if __name__ == "__main__":
    main()
