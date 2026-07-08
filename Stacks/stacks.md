# Stack

## What is a Stack?

A **Stack** is a **linear data structure** that stores elements in a
specific order and follows the **LIFO (Last In, First Out)** principle.
It is one of the most fundamental data structures used in computer
science.

---

## LIFO (Last In, First Out)

LIFO means:

- The **last element inserted** into the stack is the **first element
  removed**.

Example:

```text
Push 10
Push 20
Push 30

Top
30
20
10
```

When we perform **Pop()**, the output is:

```text
30
```

because **30 was inserted last**, so it comes out first.

---

## FILO (First In, Last Out)

A stack is also called **FILO (First In, Last Out)** because:

- The **first element inserted** remains at the bottom.
- It becomes the **last element to be removed**.

Both **LIFO** and **FILO** describe the same behavior.

---

# Basic Stack Operations

---

Operation Description Time Complexity

---

**Push()** Insert an element at **O(1)**
the top

**Pop()** Remove the top element **O(1)**

**Peek()/Top()** View the top element **O(1)**

**isEmpty()** Check whether the **O(1)**
stack is empty

**isFull()** Check whether the **O(1)**
stack is full  
 (fixed-size arrays  
 only)

---

---

# `append()` vs `insert()` in Python

append() insert()

---

Adds an element at the end Inserts at a specific index
**O(1)** **O(n)**
No shifting Existing elements shift
Faster Slower

Example:

```python
arr.append(10)      # O(1)
arr.insert(0, 10)   # O(n)
```

**Why append()?**

Since the stack top is maintained at the end of the list,
adding/removing elements from the end takes constant time.

---

# Stack Using Array

## Characteristics

- Contiguous memory
- Push/Pop: **O(1)** (except resizing)
- Better memory usage
- Excellent cache performance

## Advantages

- Fast operations
- Lower memory overhead
- Better cache locality
- Simple implementation

## Disadvantages

- Fixed-size arrays can cause **Stack Overflow**
- Resizing may take **O(n)**

---

# Stack Using Linked List

## Characteristics

- Memory is scattered
- Push/Pop always **O(1)**
- Each node stores data + pointer
- Poorer cache performance

## Advantages

- Dynamic size
- No fixed capacity limitation
- Push/Pop remain **O(1)**

## Disadvantages

- Extra memory for pointers
- Poor cache locality
- No random access

---

# Array vs Linked List

Feature Array Linked List

---

Memory Contiguous Scattered
Push() O(1)\* O(1)
Pop() O(1) O(1)
Memory Usage Lower Higher
Cache Performance Excellent Poor
Size Fixed/Resizable Dynamic
Random Access Yes No

> \*Resizing may occasionally take **O(n)**.

---

# Advantages of Stack

- Fast insertion and deletion
- Simple implementation
- Constant-time push and pop
- Used by the **Call Stack**
- Efficient for reverse-order processing

---

# Disadvantages of Stack

- No random access
- Array implementation may overflow
- Linked list has pointer overhead
- Searching requires traversal

---

# Applications of Stack

- Function Call Management (Call Stack)
- Browser History
- Undo/Redo
- Backtracking (Maze, Sudoku, DFS)
- Expression Evaluation
- Parentheses Matching
- Syntax Parsing

---

# Quick Revision

- Stack follows **LIFO**
- Also called **FILO**
- Push, Pop, Peek, isEmpty, isFull → **O(1)**
- Use **append()** instead of **insert()**
- Arrays are cache-friendly
- Linked lists are dynamically sized
