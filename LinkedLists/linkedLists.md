# Linked Lists — Reference

A linked list is a **linear data structure** where elements (nodes) are **not stored in contiguous memory**. Each node holds a value and a reference (pointer) to the next node, forming a chain connected through logic rather than physical adjacency.

```
head
 ↓
[ 10 | • ] → [ 20 | • ] → [ 30 | null ]
 data  next    data  next    data  next
```

---

## Core concepts

### Node

The basic building block. At minimum:

| Field | Purpose |
|-------|---------|
| `data` | The value stored |
| `next` | Reference to the next node (or `null` / `None` at the tail) |

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
```

### Head pointer

- `head` points to the **first node**
- An empty list has `head = None`
- Most operations start from `head` and follow `next` pointers

### Size tracking (optional)

Maintaining a `size` / `n` counter lets `len()` run in O(1) instead of traversing every time.

---

## Types of linked lists

| Type | Description |
|------|-------------|
| **Singly linked** | Each node points only to the next node |
| **Doubly linked** | Each node has `next` and `prev` — bidirectional traversal |
| **Circular** | Last node points back to head (or another node) |

This repo focuses on **singly linked lists** unless stated otherwise.

---

## Advantages

| Advantage | Why |
|-----------|-----|
| **O(1) insert/delete at head** | Just rewire a few pointers |
| **Dynamic size** | No fixed capacity; grow as needed |
| **Flexible data types** | Nodes can hold any type per node |
| **Foundation for other structures** | Stacks, queues, adjacency lists, hash map chaining |

---

## Disadvantages

| Disadvantage | Why |
|--------------|-----|
| **O(n) random access** | Must traverse from head; no index-based lookup |
| **Pointer overhead** | Extra memory per node for the `next` pointer |
| **Cache unfriendly** | Nodes may be scattered in memory (poor locality vs arrays) |
| **Manual memory management** | In languages like C/C++, you allocate/free nodes explicitly |

---

## Time complexity summary

| Operation | Singly linked list | Notes |
|-----------|-------------------|-------|
| Access by index | O(n) | Must traverse |
| Search | O(n) | Worst case: element at tail or missing |
| Insert at head | O(1) | Update `head` and one pointer |
| Insert at tail | O(n) | Must traverse to last node* |
| Insert after known node | O(1) | If you already have a pointer to that node |
| Insert at arbitrary position | O(n) | Need to traverse to find position |
| Delete head | O(1) | Move `head` forward |
| Delete tail | O(n) | Need node before tail* |
| Delete by value | O(n) | Search + rewire |
| Traverse / print | O(n) | Visit every node |
| Reverse (in-place) | O(n) | Single pass with 3 pointers |
| Find maximum | O(n) | Single pass |

\* O(1) tail insert/delete if you maintain a `tail` pointer (doubly linked helps for tail delete too).

---

## Operations — detailed

### Insertion at head — O(1)

```
new_node.next = head
head = new_node
```

```
Before:  head → [A] → [B]
After:   head → [X] → [A] → [B]
```

### Insertion at tail — O(n)

Traverse until `current.next is None`, then attach the new node.

```
Before:  head → [A] → [B] → null
After:   head → [A] → [B] → [X] → null
```

### Insertion in the middle — O(n)

Find the node **before** the insertion point, then:

```
new_node.next = target.next
target.next = new_node
```

### Deletion at head — O(1)

```
head = head.next
```

Watch out: always check if the list is empty first.

### Deletion at tail — O(n)

Need the **second-to-last** node:

```
while current.next.next is not None:
    current = current.next
current.next = None
```

### Deletion by value — O(n)

Two cases:
1. **Head matches** — treat as delete head
2. **Else** — walk while checking `current.next.data`; when found, skip that node:

```
current.next = current.next.next
```

### Search — O(n)

Walk from head, compare `data` at each node, return index or signal not found.

### Print / traverse — O(n)

```python
current = head
while current is not None:
    print(current.data)
    current = current.next
```

---

## Reversal

### Method 1 — Using a duplicate list (NOT in-place)

Traverse the original list and `insert_head` each value into a new list.  
**Time:** O(n) · **Space:** O(n) for the new list.

This is useful for learning but **not** the HW requirement.

### Method 2 — In-place reversal (HW #1)

Flip `next` pointers without allocating a new list.

**Time:** O(n) · **Space:** O(1)

```
Step 0:  null ← [1] → [2] → [3] → null
         prev  curr

Step 1:  null ← [1]   [2] → [3] → null
               prev    curr

Step 2:  null ← [1] ← [2]   [3] → null
                      prev    curr

Step 3:  null ← [1] ← [2] ← [3]   null
                             prev   curr (done)
head = prev
```

**Pseudocode:**

```
reverse_inplace():
    prev = None
    curr = head
    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    head = prev
```

**Edge cases:**
- Empty list → nothing to do
- Single node → `head.next` is already `None`, loop runs once, `head` stays correct

---

## Finding the maximum element (HW #1)

Single traversal tracking the largest value seen so far.

**Time:** O(n) · **Space:** O(1)

```
find_max():
    if head is None:
        return None
    max_val = head.data
    curr = head.next
    while curr is not None:
        if curr.data > max_val:
            max_val = curr.data
        curr = curr.next
    return max_val
```

**Edge cases:**
- Empty list → return `None` / `null`
- All equal values → return that value
- Negative numbers → works the same way

---

## Linked list vs array

| | Array | Linked list |
|---|-------|-------------|
| Memory | Contiguous | Scattered nodes |
| Access by index | O(1) | O(n) |
| Insert at head | O(n) shift | O(1) |
| Insert at tail | O(1) amortized* | O(n) without tail ptr |
| Delete at head | O(n) shift | O(1) |
| Cache performance | Better | Worse |
| Memory overhead | Low | Extra pointer per node |

\* Dynamic arrays (e.g. Python `list`) amortize tail append.

---

## Common pitfalls

1. **Losing the head** — use a temp pointer; never reassign `head` unless intentional
2. **Empty list operations** — always guard `if head is None` before accessing `head.next` or `head.data`
3. **Off-by-one in tail delete** — you need `current.next.next`, not just `current.next`
4. **Not updating head after in-place reverse** — the old head becomes the tail; `head` must point to the old tail (new first node)
5. **Creating a new list for "in-place" reverse** — violates the space constraint
6. **Forgetting to decrement size** on delete (if tracking `n`)

---

## When to use linked lists

**Good fit:**
- Frequent insertions/deletions at the **front**
- Unknown or highly variable size
- Implementing stacks, queues, or graph adjacency lists

**Poor fit:**
- Frequent random access by index
- Binary search or sorting that needs fast indexing
- Memory-constrained scenarios where pointer overhead matters

---

## Further reading / practice ideas

- Add a `tail` pointer for O(1) tail insert
- Implement a doubly linked list
- Detect a cycle (Floyd's tortoise & hare)
- Find the middle node in one pass (slow/fast pointers)
- Merge two sorted linked lists
