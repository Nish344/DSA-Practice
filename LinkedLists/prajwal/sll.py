class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        return


class LinkedList:
    def __str__(self):
        res = ""
        curr = self.head.next
        while curr:
            res += str(curr.val) + "->"
            curr = curr.next
        return res.strip("->")

    def __init__(self, head=Node(), val_list=[]):
        self.head = head
        if val_list:
            for ele in val_list:
                self.insert_front(ele)
        return

    def insert_front(self, val):
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        return

    def reverse_inplace(self):
        head = self.head.next
        dummy = Node(-1, head)
        first = head
        curr = head.next if head else head
        while curr and first:
            first.next = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = first.next
        self.head.next = dummy.next
        return

    def get_max(self):
        curr = self.head.next
        max_val = float("-inf")
        while curr:
            max_val = max(max_val, curr.val)
            curr = curr.next
        return max_val


def main():
    def test_listclass():
        tc = [[4, 3, 2, 1]]
        ans = ["1->2->3->4"]
        for t, a in zip(tc, ans):
            ll = LinkedList(val_list=t, head=Node())
            assert str(ll) == a, [str(ll), a]
        return

    def test_max():
        tc = [[3, 2, 1], [2, 9, 1, 5], [7], [], [-7, -1, -3], [1, 4, 4]]
        ans = [3, 9, 7, float("-inf"), -1, 4]
        for t, a in zip(tc, ans):
            ll = LinkedList(head=Node(), val_list=t)
            assert ll.get_max() == a, [t, ll.get_max(), a, str(ll)]
        return

    def test_reverse():
        tc = [[3, 2, 1], [1], [], [5, 1, 9, 2], [2, 2, 2]]  # inserted in reverse order
        ans = ["3->2->1", "1", "", "5->1->9->2", "2->2->2"]
        for t, a in zip(tc, ans):
            ll = LinkedList(head=Node(), val_list=t)
            ll.reverse_inplace()
            assert str(ll) == a, [t, ll.reverse_inplace(), a, str(ll)]
        return

    test_listclass()
    test_max()
    test_reverse()


if __name__ == "__main__":
    main()
