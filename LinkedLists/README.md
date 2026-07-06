# Linked Lists

> **Theory & algorithms:** [linkedLists.md](./linkedLists.md) — read this for concepts, complexity, pseudocode, and pitfalls.  
> **Repo workflow:** [../README.md](../README.md) — how homework, git, and the rotating tutor system work.

---

## Table of contents

1. [How this topic fits the repo](#how-this-topic-fits-the-repo)
2. [Your folder](#your-folder)
3. [Session 1 — what we covered in class](#session-1--what-we-covered-in-class)
4. [HW #1 — what you need to implement](#hw-1--what-you-need-to-implement)
5. [Manual test cases](#manual-test-cases)
6. [How to submit](#how-to-submit)
7. [Tutor notes (Linked Lists)](#tutor-notes-linked-lists)

---

## How this topic fits the repo

This folder follows the same pattern every topic will use:

```
LinkedLists/
├── linkedLists.md     ← theory (detailed reference, everyone reads)
├── README.md          ← you are here (session summary + active homework)
└── <your-name>/       ← your code only
    └── linkedlist.*
```

| Phase | What happens |
|-------|----------------|
| **In class** | Tutor teaches basics; everyone follows along |
| **After class** | Tutor updates this README + opens a GitHub Issue |
| **At home** | You implement HW in your folder, self-test, comment on the issue |

**No auto-grading.** You are responsible for running the test tables below and reporting honestly on the issue.

---

## Your folder

Create a folder with your **first name (lowercase)**. If two people share a name, use first name + last initial.

```bash
# from repo root, after git pull
mkdir -p LinkedLists/<your-name>
```

Examples:

```
LinkedLists/
├── nishanth/
│   └── linkedlist.py
├── priya/
│   └── LinkedList.java
└── arjun/
    └── linkedlist.cpp
```

**Rules:**
- Only create/edit files inside **your** folder
- One main solution file is enough; name it `linkedlist` + your language extension
- Any language is fine — match the **behavior** in the spec, not necessarily the exact method spelling

---

## Session 1 — what we covered in class

**Tutor:** Nishanth  
**Status:** Basic operations done in class; two topics left for homework.

These operations should already be in your implementation before you start HW #1:

| Operation | Method (suggested) | Time | Space | Notes |
|-----------|-------------------|------|-------|-------|
| Insert at head | `insert_head` | O(1) | O(1) | New node points to old head |
| Insert at tail | `insert_tail` | O(n) | O(1) | Traverse to last node |
| Insert after value | `insert_middle` | O(n) | O(1) | Find target, splice in |
| Delete head | `delete_head` | O(1) | O(1) | Advance head pointer |
| Delete tail | `delete_tail` | O(n) | O(1) | Need second-to-last node |
| Delete by value | `delete_value` | O(n) | O(1) | Search then rewire |
| Traverse / print | `__str__` / `print` | O(n) | O(1) | Walk from head |
| Search by value | `search` | O(n) | O(1) | Return index or not found |
| Reverse (extra list) | `rev` | O(n) | O(n) | **Class demo only** — uses a second list |

### What we did NOT cover (→ HW #1)

| Operation | Why it's homework |
|-----------|-------------------|
| **In-place reversal** | Core pointer technique; must not allocate a second list |
| **Find maximum** | Simple traversal practice; edge case when list is empty |

See [linkedLists.md — Reversal](./linkedLists.md#reversal) and [Finding the maximum](./linkedLists.md#finding-the-maximum-element-hw-1) for full algorithm walkthroughs.

---

## HW #1 — what you need to implement

**GitHub Issue:** *(tutor creates this after class — check the [Issues](https://github.com/) tab for `[HW] Linked Lists`)*

Implement **two methods** on your linked list class.

### 1. `reverse_inplace()`

Reverse the list **in place**.

| Requirement | Detail |
|-------------|--------|
| Time | O(n) — single pass |
| Space | O(1) — no second linked list, no value array |
| Mutation | Must update `head` and flip `next` pointers on existing nodes |
| Edge cases | Empty list, single-node list |

**Must NOT:**
- Create a new `LinkedList` and copy values (that's what `rev()` does — different exercise)
- Use a stack/array to store all values first (that is O(n) extra space)

**Algorithm (3-pointer technique):**

```
prev = None
curr = head
while curr is not None:
    next_node = curr.next   # save rest of list
    curr.next = prev        # flip pointer
    prev = curr             # advance prev
    curr = next_node        # advance curr
head = prev
```

**Walkthrough for `1 → 2 → 3`:**

```
Start:  null ← ?    [1]→[2]→[3]→null
Step 1: null ← [1]  [2]→[3]→null
Step 2: null ← [1]←[2]  [3]→null
Step 3: null ← [1]←[2]←[3]
head = node 3
```

### 2. `find_max()`

Return the largest value in the list.

| Requirement | Detail |
|-------------|--------|
| Time | O(n) — single traversal |
| Space | O(1) |
| Empty list | Return `None` / `null` (state this in a comment if your language has no nullable return) |
| Assumption | Values are comparable numbers |

**Pseudocode:**

```
if head is None: return None
max_val = head.data
curr = head.next
while curr is not None:
    if curr.data > max_val:
        max_val = curr.data
    curr = curr.next
return max_val
```

---

## Manual test cases

Run **every** row below before commenting on the issue. Be honest in your self-check.

### `reverse_inplace()`

Build the list, call `reverse_inplace()`, then print/traverse and compare.

| # | Before (head → tail) | After (expected) | Edge case? |
|---|----------------------|------------------|------------|
| 1 | `1 → 2 → 3` | `3 → 2 → 1` | normal |
| 2 | `1` | `1` | single node |
| 3 | *(empty)* | *(empty, no crash)* | empty |
| 4 | `5 → 1 → 9 → 2` | `2 → 9 → 1 → 5` | unsorted |
| 5 | `2 → 2 → 2` | `2 → 2 → 2` | duplicates |

**Self-check questions:**
- After reversing twice, do you get the original order back?
- Did `head` actually change, or did you only print a reversed copy?

### `find_max()`

| # | Input (head → tail) | Expected return |
|---|---------------------|-----------------|
| 1 | `1 → 2 → 3` | `3` |
| 2 | `5 → 1 → 9 → 2` | `9` |
| 3 | `7` | `7` |
| 4 | *(empty)* | `None` / `null` |
| 5 | `-3 → -1 → -7` | `-1` |
| 6 | `4 → 4 → 1` | `4` |

### Suggested local test flow (Python example)

```python
L = LinkedList()
for v in [1, 2, 3]:
    L.insert_tail(v)
L.reverse_inplace()
assert str(L) == "3->2->1"

L2 = LinkedList()
assert L2.find_max() is None
```

Adapt the same logic in your language.

---

## How to submit

### 1. Push your code

```bash
git pull origin main
# edit only LinkedLists/<your-name>/
git add LinkedLists/<your-name>/
git commit -m "LinkedLists HW1: reverse_inplace and find_max"
git push origin main
```

### 2. Comment on the GitHub Issue

Find the issue titled something like:

`[HW] Linked Lists — In-place reversal & max element`

Leave a comment:

```
Done — LinkedLists/<your-name>/ — <language> — self-checked ✓
```

**Examples:**

```
Done — LinkedLists/priya/ — Java — self-checked ✓
```

```
Partial — LinkedLists/arjun/ — C++ — find_max done, reverse_inplace stuck
```

### 3. Do not close the issue

The tutor closes it after the deadline. You only comment.

---

## Tutor notes (Linked Lists)

*For whoever teaches the next linked-list session or creates the issue.*

### Creating the HW #1 issue

1. **Issues → New issue → Homework template**
2. **Title:** `[HW] Linked Lists — In-place reversal & max element`
3. **Body — copy/paste:**

```markdown
## Topic
Linked Lists

## Tasks
- [ ] `reverse_inplace()` — O(n) time, O(1) extra space, no second list
- [ ] `find_max()` — O(n) single traversal, handle empty list

## Spec
Full details and test tables: [LinkedLists/README.md](https://github.com/<org>/DSA-Practice/blob/main/LinkedLists/README.md)

Theory reference: [linkedLists.md](https://github.com/<org>/DSA-Practice/blob/main/LinkedLists/linkedLists.md)

## When done
Comment below:
`Done — LinkedLists/<your-name>/ — <language> — self-checked ✓`
```

4. **Labels:** `homework`, `linked-lists`
5. **Assignees:** all classmates (optional)
6. **Deadline:** set in a comment or issue body, e.g. `Due: July 13`

### After deadline

- [ ] Read all comments — note who finished / partial / silent
- [ ] Close the issue
- [ ] (Optional) Next session: 5-min recap of in-place reverse pointer trick

### Future HW ideas (Linked Lists)

| HW # | Topic |
|------|-------|
| HW #2 | Detect cycle (Floyd's algorithm) |
| HW #3 | Find middle node (slow/fast pointers) |
| HW #4 | Merge two sorted linked lists |

When adding HW #2, update this README and open a new issue — don't edit a closed one.
