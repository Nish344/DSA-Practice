class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def insert_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.n += 1
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        self.n += 1

    def insert_middle(self, target, value):
        new_node = Node(value)
        temp = self.head

        while temp is not None and temp.next is not None:
            if temp.data == target:
                new_node.next = temp.next
                temp.next = new_node
                self.n += 1
                return
            temp = temp.next

    def delete_head(self):
        if self.head is None:
            print("Linked List is Empty, Deletion cannot be performed")
            return

        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        if self.head is None:
            print("Linked List is Empty, Deletion cannot be performed")
            return

        if self.head.next is None:
            self.delete_head()
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        self.n -= 1

    def delete_value(self, value):
        if self.head is None:
            print("Linked List is Empty, Deletion cannot be performed")
            return

        if self.head.data == value:
            self.delete_head()
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                self.n -= 1
                return
            temp = temp.next

    def __str__(self):
        temp = self.head
        res = ""

        while temp is not None:
            res = res + "->" + str(temp.data)
            temp = temp.next

        return res[2:] if res else ""

    def search(self, target):
        if self.head is None:
            print("Linked List is Empty, search cannot be performed")
            return None

        temp = self.head
        counter = 0

        while temp is not None:
            if temp.data == target:
                return counter
            temp = temp.next
            counter += 1

        print("Element not found in the linked list")
        return None

    def rev(self):
        """Reverse using a duplicate list (class exercise — not in-place)."""
        if self.head is None:
            print("Linked List is Empty, reversal cannot be performed")
            return

        rev = LinkedList()
        temp = self.head

        while temp is not None:
            rev.insert_head(temp.data)
            temp = temp.next

        return rev

    # --- HW #1: implement these ---

    def reverse_inplace(self):
        """Reverse the list in O(n) time, O(1) space. See linkedLists.md."""
        raise NotImplementedError

    def find_max(self):
        """Return the maximum value, or None if the list is empty."""
        raise NotImplementedError


def main():
    L = LinkedList()

    L.insert_tail(1)
    L.insert_tail(2)
    L.insert_tail(3)
    L.insert_tail(4)
    L.insert_tail(33)
    L.insert_tail(5)

    print(L)

    L.delete_value(33)
    print("Node deleted")
    print(L)

    L.delete_value(5)
    print(L)

    print(L.search(3))

    rev = L.rev()
    print(rev)

    # HW #1 — uncomment after implementing
    # L.reverse_inplace()
    # print(L)
    # print(L.find_max())


if __name__ == "__main__":
    main()
