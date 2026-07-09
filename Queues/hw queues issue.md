# [HW] Queues — Implement Queue & Practice FIFO

## Topic

Queues

---

## Tutor

Rohan Poddar

---

## Tasks

* [ ] Solve **LeetCode 232 – Implement Queue using Stacks**
* [ ] Solve **LeetCode 933 – Number of Recent Calls**
* [ ] Test your solutions with your own test cases.
* [ ] Push your code to your folder in the repository.

---

## Session Summary

In today's session, we learned:

* Queue Data Structure
* FIFO (First In, First Out)
* Queue Operations

  * enqueue()
  * dequeue()
  * peek()
  * isEmpty()
  * size()
* Queue Implementation using Python
* Time Complexity
* Real-world Applications

---

## Expected Complexity

### Queue (Python List Implementation)

| Operation | Expected Complexity |
| --------- | ------------------- |
| enqueue() | O(1)                |
| dequeue() | O(n)                |
| peek()    | O(1)                |
| isEmpty() | O(1)                |
| size()    | O(1)                |

---

## Manual Test Cases

### Test Case 1

Operations

```text
enqueue(10)
enqueue(20)
enqueue(30)
```

Expected Queue

```text
[10, 20, 30]
```

---

### Test Case 2

Operation

```text
dequeue()
```

Expected Output

```text
10
```

Expected Queue

```text
[20, 30]
```

---

### Test Case 3

Operation

```text
peek()
```

Expected Output

```text
20
```

Queue should remain

```text
[20, 30]
```

---

### Test Case 4

Operation

```text
size()
```

Expected Output

```text
2
```

---

### Test Case 5

Operation

```text
isEmpty()
```

Expected Output

```text
False
```

---

### Test Case 6

Operations

```text
dequeue()
dequeue()
```

Expected Queue

```text
[]
```

---

### Test Case 7

Operation

```text
isEmpty()
```

Expected Output

```text
True
```

---

## Submission Instructions

1. Pull the latest version of the repository.
2. Solve both homework problems.
3. Place your solution inside your own folder.

Example:

```text
Queues/<your-name>/
```

4. Test your solution.
5. Commit and push your code.

Example:

```bash
git add Queues/<your-name>/
git commit -m "Queues: complete homework"
git push origin main
```

---

## When Done

Comment below using this format:

```text
Done — Queues/<your-name>/ — Python — self-checked ✓
```

If you couldn't finish everything:

```text
Partial — Queues/<your-name>/ — Python — Completed Problem 1, working on Problem 2
```

---

**Do not close this issue.** The tutor will close it.

Happy Coding! 🚀
