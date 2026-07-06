# DSA Practice

A shared repo for our class to practice **Data Structures & Algorithms** together. Everyone implements problems in their own folder, in whatever language they prefer. Homework is tracked through **GitHub Issues** — no auto-grading, everyone self-evaluates.

---

## Table of contents

1. [Big picture](#big-picture)
2. [Rotating tutor role](#rotating-tutor-role)
3. [Repo structure](#repo-structure)
4. [First-time setup](#first-time-setup)
5. [Daily workflow (everyone)](#daily-workflow-everyone)
6. [Homework tracking (GitHub Issues)](#homework-tracking-github-issues)
7. [Languages & file naming](#languages--file-naming)
8. [Git rules](#git-rules)
9. [Tutor checklist](#tutor-checklist-when-its-your-turn)
10. [Student checklist](#student-checklist)
11. [FAQ](#faq)

---

## Big picture

```
┌─────────────────────────────────────────────────────────────┐
│  TUTOR (rotates each session/topic)                         │
│  · Teaches in class                                         │
│  · Updates theory docs + HW spec in the repo                │
│  · Creates a GitHub Issue for the homework                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  EVERYONE                                                   │
│  · Clones repo                                              │
│  · Works in their own folder:  Topic/<your-name>/           │
│  · Implements in any language                               │
│  · Self-tests using manual test cases in topic README       │
│  · Comments on the Issue when done                          │
└─────────────────────────────────────────────────────────────┘
```

**There is no answer checking.** You run the test cases yourself, honestly mark whether you passed, and comment on the issue. The goal is practice and learning, not grades.

---

## Rotating tutor role

Each session or topic, a **different person is the tutor**. The tutor is not a "teacher who knows everything" — they lead that topic, set up the repo for it, and assign the homework.

### What the tutor does

| When | Responsibility |
|------|----------------|
| **Before class** | Skim / prepare the topic; make sure theory notes exist or will be written |
| **During class** | Walk through concepts and live-code basic operations together |
| **After class** | Update docs in the repo (see [Tutor checklist](#tutor-checklist-when-its-your-turn)) |
| **After class** | Open a GitHub Issue for the homework |
| **Before next session** | Glance at issue comments to see who submitted (no grading required) |

### What the tutor does NOT do

- Review every solution line-by-line (unless you voluntarily pair up)
- Enforce one programming language
- Fail people — this is self-paced practice

### Tracking who's tutor when

Keep a simple list — in a pinned GitHub Issue, a `TUTORS.md` file, or your class group chat:

```
| # | Topic        | Tutor    | Date       |
|---|--------------|----------|------------|
| 1 | Linked Lists | Nishanth | 2026-07-06 |
| 2 | Arrays       | Priya    | TBD        |
| 3 | Stacks       | Arjun    | TBD        |
```

Whoever is **next** should have **write access** to the repo (ask the repo owner to add them as a collaborator before their session).

---

## Repo structure

```
DSA-Practice/
├── README.md                    ← you are here (how everything works)
│
├── LinkedLists/
│   ├── linkedLists.md           ← theory & reference (read-only for students)
│   ├── README.md                ← homework spec + test cases for this topic
│   ├── nishanth/
│   │   └── linkedlist.py
│   ├── priya/
│   │   └── LinkedList.java
│   └── arjun/
│       └── linkedlist.cpp
│
├── Arrays/                      ← added when that topic's tutor runs a session
│   ├── arrays.md
│   ├── README.md
│   └── <name>/
│
└── .github/
    └── ISSUE_TEMPLATE/
        └── homework.md          ← template when creating HW issues
```

### What each file type is for

| File | Who edits it | Purpose |
|------|--------------|---------|
| `README.md` (root) | Anyone (via PR or tutor) | How the repo works — this doc |
| `<Topic>/<topic>.md` | **Tutor** for that topic | Detailed theory, complexity, algorithms |
| `<Topic>/README.md` | **Tutor** for that topic | What was covered in class + current HW + test cases |
| `<Topic>/<your-name>/*` | **Only you** | Your implementation |

---

## First-time setup

### 1. Get access

Ask the repo owner to add you as a **collaborator** on GitHub  
(Settings → Collaborators → Add people).

### 2. Clone the repo

```bash
git clone https://github.com/<org-or-user>/DSA-Practice.git
cd DSA-Practice
```

### 3. Create your folder

Use your **first name, lowercase** (keeps things consistent):

```bash
mkdir -p LinkedLists/<your-name>
```

Example:

```bash
mkdir -p LinkedLists/priya
```

### 4. Configure git (one time, on your machine)

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

---

## Daily workflow (everyone)

### When a new topic session happens

1. **Pull** latest changes (tutor may have added docs after last session):
   ```bash
   git pull origin main
   ```
2. **Create your folder** if this is a new topic:
   ```bash
   mkdir -p Arrays/<your-name>
   ```
3. **Read** the topic theory (`<Topic>/<topic>.md`) and homework (`<Topic>/README.md`).
4. **Implement** in your folder only.

### When working on homework

```bash
# 1. Make sure you're up to date
git pull origin main

# 2. Write / edit your code
#    only touch: LinkedLists/<your-name>/linkedlist.py  (or .java, .cpp, etc.)

# 3. Test locally using the manual test cases in the topic README

# 4. Commit and push
git add LinkedLists/<your-name>/
git commit -m "LinkedLists: add reverse_inplace and find_max"
git push origin main
```

### When homework is done

Go to the **GitHub Issue** for that homework (linked from the topic README or Issues tab) and leave a comment:

```
Done — LinkedLists/priya/ — Java — self-checked ✓
```

That comment is your submission. No PR required unless the tutor asks for one.

---

## Homework tracking (GitHub Issues)

**One GitHub Issue = one homework assignment** for the whole class (not one issue per person).

### How it works

```
Issue #1: [HW] Linked Lists — reverse_inplace + find_max
│
├── Created by: tutor after class
├── Assigned to: everyone (optional)
│
├── Comment by Priya:  "Done — LinkedLists/priya/ — Java — self-checked ✓"
├── Comment by Arjun:  "Done — LinkedLists/arjun/ — C++ — self-checked ✓"
└── Comment by you:    "Done — LinkedLists/nishanth/ — Python — self-checked ✓"
```

### For students

1. Find the issue under the repo **Issues** tab (filter by label `homework`).
2. Implement the tasks listed in the issue body.
3. Self-test using the tables in `<Topic>/README.md`.
4. **Comment on the issue** when done (format above).
5. Do **not** close the issue yourself — the tutor closes it after the deadline.

### For the tutor

1. After class, go to **Issues → New issue**.
2. Choose the **Homework** template.
3. Fill in tasks, link to the topic README, assign classmates.
4. Add labels: `homework`, topic name (e.g. `linked-lists`).
5. Share the issue link in the class group.
6. Before the next session, read comments to see who finished.
7. **Close the issue** when the deadline passes.

### Optional: Project board

For a visual overview, create a **Project** (Kanban board):

```
┌──────────┬──────────────┬──────────┐
│   Todo   │ In Progress  │   Done   │
├──────────┼──────────────┼──────────┤
│  HW #2   │    HW #1     │ Session 0│
└──────────┴──────────────┴──────────┘
```

Not required — issue comments alone are enough for a small group.

---

## Languages & file naming

Everyone picks their own language. The repo does not run automated tests across languages.

| Language | Example path |
|----------|----------------|
| Python | `LinkedLists/nishanth/linkedlist.py` |
| Java | `LinkedLists/priya/LinkedList.java` |
| C++ | `LinkedLists/arjun/linkedlist.cpp` |
| JavaScript | `LinkedLists/sam/linkedlist.js` |
| C | `LinkedLists/alex/linkedlist.c` |

**Convention:** one main file named `linkedlist` (or `LinkedList` for Java) inside your folder. Add more files in your folder if you need helpers — that's fine.

### Method naming

Match the **behavior** described in the homework, not necessarily the exact spelling. If the spec says `reverse_inplace()`, Java might use `reverseInPlace()` — just mention your names in your issue comment if they differ.

---

## Git rules

### Do

- Only edit files inside **your own folder** (`<Topic>/<your-name>/`)
- Pull before you push (`git pull` then `git push`)
- Write clear commit messages: `LinkedLists: implement find_max`
- Ask in the group chat if you're unsure before editing shared docs

### Don't

- Edit or delete someone else's folder
- Delete or rewrite theory docs (`linkedLists.md`, etc.) unless you're the tutor for that topic
- Force-push to `main` (`git push --force`) — ever
- Commit build artifacts (`.class`, `__pycache__/`, binaries) — `.gitignore` handles most of this

### Merge conflicts

If `git pull` fails because someone else changed a file you also changed:

- **If the conflict is in your folder only** — unlikely unless two people share a name folder (don't).
- **If the conflict is in a shared doc** — talk to the tutor; they resolve it.
- **General fix:**
  ```bash
  git pull origin main
  # fix conflicts in your editor
  git add .
  git commit -m "Resolve merge conflict"
  git push origin main
  ```

---

## Tutor checklist (when it's your turn)

Use this when you are leading a topic session.

### Before class

- [ ] Confirm you have **write access** to the repo
- [ ] Read / skim the topic you'll teach
- [ ] Pull latest: `git pull origin main`

### During class

- [ ] Explain the data structure / algorithm
- [ ] Live-code **basic operations** together (insert, delete, traverse, etc.)
- [ ] Note what you **didn't** cover — that becomes homework

### After class (in the repo)

- [ ] Create topic folder if new: `Arrays/`, `Stacks/`, etc.
- [ ] Write or update **theory doc**: `<Topic>/<topic>.md` (detailed reference for everyone)
- [ ] Write or update **homework README**: `<Topic>/README.md`
  - What was covered in class (session notes)
  - What's assigned as HW
  - Manual test case tables
  - Link to the theory doc
- [ ] Commit and push:
  ```bash
  git add Arrays/
  git commit -m "Arrays: add theory notes and HW #1 spec"
  git push origin main
  ```

### After class (on GitHub)

- [ ] Create a **Homework issue** (Issues → New issue → Homework template)
- [ ] Title format: `[HW] <Topic> — <short description>`
- [ ] Copy tasks and test cases from `<Topic>/README.md` into the issue
- [ ] Assign everyone (or leave open for self-assign)
- [ ] Add labels: `homework`, `<topic-name>`
- [ ] Post the issue link in the class chat
- [ ] Update the tutor rotation table (who's next)

### Before the next session

- [ ] Check issue comments — who marked done?
- [ ] Close the issue after the deadline
- [ ] (Optional) Briefly mention common mistakes in class — no need to name names

---

## Student checklist

### Every session

- [ ] `git pull origin main`
- [ ] Read the new theory doc and topic README
- [ ] Create your folder if you don't have one yet

### Every homework

- [ ] Read the GitHub Issue for the assignment
- [ ] Implement only in `<Topic>/<your-name>/`
- [ ] Run **all** manual test cases from the topic README
- [ ] Commit and push your code
- [ ] Comment on the issue:
  ```
  Done — <Topic>/<your-name>/ — <language> — self-checked ✓
  ```
- [ ] If you couldn't finish, comment anyway:
  ```
  Partial — LinkedLists/priya/ — Java — stuck on reverse_inplace, find_max done
  ```

### Self-evaluation (be honest)

Ask yourself for each test case:

1. Does my code produce the expected output?
2. Does it handle empty input?
3. Does it meet the complexity requirement (e.g. O(1) space for in-place reverse)?

If no — keep working or ask for help in the group chat. Still comment `Partial` so the tutor knows where you are.

---

## FAQ

**Do I need to open a Pull Request?**  
No. Push to `main` and comment on the issue. PRs are optional if you want someone to look at your code.

**Can I look at someone else's solution?**  
After you've tried yourself, yes — that's a good way to learn. Don't copy without understanding.

**What if I use a different method name?**  
Fine. Match the behavior in the spec and mention your naming in the issue comment.

**What if the tutor hasn't created the issue yet?**  
Ping them in the group chat. You can still start coding from `<Topic>/README.md`.

**Who owns the repo?**  
Whoever created it on GitHub. They add collaborators and can transfer ownership later if needed.

**How do we add a new topic?**  
The tutor for that topic creates the folder, docs, and HW issue following the [Tutor checklist](#tutor-checklist-when-its-your-turn).

**What if two people have the same first name?**  
Use first name + last initial: `LinkedLists/nishanth-k/`.

---

## Current topics

| Topic | Theory | Homework | Tutor |
|-------|--------|----------|-------|
| [Linked Lists](./LinkedLists/) | [linkedLists.md](./LinkedLists/linkedLists.md) | [README](./LinkedLists/README.md) | Nishanth |

*(Tutors: add new rows when you onboard a topic.)*
