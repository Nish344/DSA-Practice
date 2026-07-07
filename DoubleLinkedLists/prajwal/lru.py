class LRUNode:
    def __init__(self, key, val, freq=1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUDLL:
    def __init__(self):
        self.head = LRUNode(-1, -1)
        self.tail = LRUNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hmap = {}  # Store pointers to node. Key -> node pointer

    def add_node(self, node):
        """
        Appending the given node to the front of DLL and add the key to hmap.
        Front node is always be most recently used node.
        So eviction of node (the least recently used) is at tail.
        """
        first_node = self.head.next

        self.head.next = node
        node.prev = self.head

        first_node.prev = node
        node.next = first_node

        self.hmap[node.key] = node

    def remove_node(self, node):
        """Standard DLL node remove of given node and delete key from hmap"""

        node.prev.next = node.next
        node.next.prev = node.prev
        self.hmap.pop(node.key)
        # optional
        # return node

    def get(self, key):
        """Handle the get() operation of LRUCache"""
        node = self.hmap.get(key)
        # print("hmap", node, key, self.hmap)

        # making the node with given key as most recently used by appending it at head.
        if node:
            self.remove_node(node)
            self.add_node(node)

        return node

    def remove_last_node(self):
        """
        It is assumed that DLL is never empty and dummy head and tail or preserved and
        node at tail is lru always.
        """
        node = self.tail.prev
        self.remove_node(node)


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = LRUDLL()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print("get", self.cache.hmap.keys())
        res = self.cache.get(key)
        return res.val if res else -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.hmap.get(key)

        if not node:  # new node since key was not in hashmap
            self.capacity -= 1
            if self.capacity == -1:
                self.capacity += 1
                self.cache.remove_last_node()
            node = LRUNode(key, value)
            self.cache.add_node(node)
        else:
            node.val = value
            self.get(key)  # .get maintains the lru ordering.


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

