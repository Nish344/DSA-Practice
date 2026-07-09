class Queue:
    """
    Queue class implementing the basic queue operations.
    """

    def __init__(self):
        """
        Constructor

        Creates an empty list that will store
        all queue elements.
        """
        self.queue = []

    def enqueue(self, item):
        """
        Insert an element at the rear of the queue.

        Time Complexity:
        O(1)
        """

        self.queue.append(item)

    def dequeue(self):
        """
        Remove and return the front element.

        Returns:
            Front element if queue is not empty.
            Message if queue is empty.

        Time Complexity:
        O(n)
        """

        if self.isEmpty():
            return "Queue is Empty"

        return self.queue.pop(0)

    def peek(self):
        """
        Return the front element without removing it.

        Returns:
            Front element if queue exists.
            None if queue is empty.

        Time Complexity:
        O(1)
        """

        if self.isEmpty():
            return None

        return self.queue[0]

    def isEmpty(self):
        """
        Check whether queue is empty.

        Returns:
            True  -> Queue is empty
            False -> Queue has elements
        """

        return len(self.queue) == 0

    def size(self):
        """
        Return number of elements in queue.
        """

        return len(self.queue)

    def display(self):
        """
        Display the queue.
        """

        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue :", self.queue)


# ==================================================
# Driver Code
# ==================================================

print("=" * 50)
print("QUEUE IMPLEMENTATION")
print("=" * 50)

# Create Queue
q = Queue()

print("\nInitially")
q.display()

print("\nEnqueue Operations")

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

q.enqueue(40)
q.display()

print("\nFront Element")
print(q.peek())

print("\nQueue Size")
print(q.size())

print("\nDequeue Operation")
removed = q.dequeue()
print("Removed :", removed)
q.display()

print("\nDequeue Again")
removed = q.dequeue()
print("Removed :", removed)
q.display()

print("\nCurrent Front")
print(q.peek())

print("\nCurrent Size")
print(q.size())

print("\nIs Queue Empty?")
print(q.isEmpty())

print("\nRemoving Remaining Elements")

print("Removed :", q.dequeue())
print("Removed :", q.dequeue())

q.display()

print("\nIs Queue Empty?")
print(q.isEmpty())

print("\nTrying to Dequeue from Empty Queue")
print(q.dequeue())

print("\nTrying to Peek Empty Queue")
print(q.peek())