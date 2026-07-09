# Queues

## Session Summary

In today's session, we learned the fundamentals of the **Queue** data structure.

### Topics Covered

- What is a Queue?
- FIFO (First In, First Out)
- Queue Operations
  - enqueue()
  - dequeue()
  - peek()
  - isEmpty()
  - size()
- Queue Implementation using Python List
- Time Complexity
- Real-world Applications
- Placement Interview Questions

---

# Homework

Complete the following LeetCode problems.

## Problem 1

### Implement Queue using Stacks

**LeetCode 232**

Difficulty: Easy

Expected Learning

- Understand Queue implementation
- Understand Stack operations
- Learn how one data structure can be implemented using another

---

## Problem 2

### Number of Recent Calls

**LeetCode 933**

Difficulty: Easy

Expected Learning

- Learn practical Queue usage
- Understand FIFO in real-world scenarios
- Practice Queue operations

---

# Requirements

While solving the problems:

- Write clean code.
- Use meaningful variable names.
- Add comments wherever necessary.
- Test your solution before pushing.
- Try to explain your solution in your own words.

---

# Manual Test Cases

## Queue Implementation

### Test Case 1

Operation

```
enqueue(10)
enqueue(20)
enqueue(30)
```

Expected Queue

```
[10, 20, 30]
```

---

### Test Case 2

Operation

```
dequeue()
```

Expected Output

```
10
```

Expected Queue

```
[20, 30]
```

---

### Test Case 3

Operation

```
peek()
```

Expected Output

```
20
```

Queue should remain

```
[20, 30]
```

---

### Test Case 4

Operation

```
size()
```

Expected Output

```
2
```

---

### Test Case 5

Operation

```
isEmpty()
```

Expected Output

```
False
```

---

### Test Case 6

Operation

```
dequeue()
dequeue()
```

Expected Queue

```
[]
```

---

### Test Case 7

Operation

```
isEmpty()
```

Expected Output

```
True
```

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| enqueue() | O(1) |
| dequeue() | O(n) (Python List Implementation) |
| peek() | O(1) |
| isEmpty() | O(1) |
| size() | O(1) |

---

# Interview Questions

Try answering these questions before the next session.

1. What is FIFO?
2. What is the difference between Stack and Queue?
3. Why is dequeue O(n) when using a Python List?
4. Why is `collections.deque` preferred over a Python List?
5. Name three real-world applications of Queue.

---

# Submission Instructions

1. Pull the latest changes from the repository.

2. Create your folder if it does not already exist.

Example

```
Queues/<your-name>/
```

3. Solve both homework problems.

4. Test your implementation using the manual test cases.

5. Commit and push your code.

Example

```
git add Queues/<your-name>/
git commit -m "Queues: complete homework"
git push origin main
```

6. Comment on the GitHub Homework Issue using the format

```
Done — Queues/<your-name>/ — Python — self-checked ✓
```

If you could not complete everything

```
Partial — Queues/<your-name>/ — Python — Completed Problem 1, working on Problem 2
```

---

# Reference

Theory Notes

```
Queues/queues.md
```

Homework

```
Queues/README.md
```

Good luck!

Remember:

> Understanding the idea is more important than memorizing the code.
