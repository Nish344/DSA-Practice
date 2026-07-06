# Linked Lists — Homework

> Theory & detailed reference: [linkedLists.md](./linkedLists.md)

## Folder layout

Create your own folder and add your solution:

```
LinkedLists/
├── nishanth/
│   └── linkedlist.py
├── priya/
│   └── LinkedList.java
└── arjun/
    └── linkedlist.cpp
```

---

## Session 1 — Basic operations (completed in class)

These should already be implemented before starting HW #1:

| Operation | Expected complexity |
|-----------|---------------------|
| Insert at head | O(1) |
| Insert at tail | O(n) |
| Insert after a value | O(n) |
| Delete head | O(1) |
| Delete tail | O(n) |
| Delete by value | O(n) |
| Traverse / print | O(n) |
| Search by value | O(n) |

---

## HW #1 — In-place reversal & maximum element

Implement the following two methods on your linked list class.

### 1. `reverse_inplace()`

Reverse the list **in place** using O(1) extra space.

**Rules:**
- Must mutate the existing list (update `head` / pointers)
- Must **not** create a second linked list or copy values into a new structure
- Empty list and single-node list should be handled safely

**Algorithm hint (3-pointer technique):**

```
prev = None
curr = head
while curr is not None:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
head = prev
```

### 2. `find_max()`

Return the **maximum value** stored in the list.

**Rules:**
- Single traversal — O(n) time
- If the list is empty, return `None` / `null` (or document your choice in a comment)
- Assume comparable values (numbers)

---

## Manual test cases

Run these yourself before marking the issue done.

### `reverse_inplace()`

| Input (head → tail) | After reverse |
|---------------------|---------------|
| `1 → 2 → 3`         | `3 → 2 → 1`   |
| `1`                 | `1`           |
| *(empty)*           | *(empty)*     |
| `5 → 1 → 9 → 2`     | `2 → 9 → 1 → 5` |

### `find_max()`

| Input           | Expected |
|-----------------|----------|
| `1 → 2 → 3`     | `3`      |
| `5 → 1 → 9 → 2` | `9`      |
| `7`             | `7`      |
| *(empty)*       | `None` / `null` |

---

## When you're done

Comment on the GitHub Issue with:

```
Done — LinkedLists/<your-name>/ — <language> — self-checked ✓
```
