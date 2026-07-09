# Stack Problems

---

# 1. Celebrity Problem

## Problem Statement

Given a square matrix `mat[][]` of size `n × n`, where:

- `mat[i][j] == 1` means person `i` knows person `j`.
- `mat[i][j] == 0` means person `i` does **not** know person `j`.

Find the **celebrity** person, where:

A celebrity is someone who:

- Is known by everyone else.
- Does not know anyone (except themselves).

Return the **index** of the celebrity if one exists; otherwise return **-1**.

> **Note:** It is guaranteed that `mat[i][i] == 1` for all `i`.

---

# 2. Reverse a Stack

## Problem Statement

Given a stack `st[]`, reverse the stack so that:

- The top element becomes the bottom.
- The bottom element becomes the top.
- The order of the remaining elements is preserved accordingly.

> **Note:** The input array represents the stack from **bottom to top** (the last element is the top). The output is displayed by printing elements from **top to bottom** after reversal.

---

# 3. Largest Rectangular Area in a Histogram

## Problem Statement

Given an array `arr[]` representing a histogram, where:

- Each element denotes the height of a bar.
- Every bar has a uniform width of **1 unit**.

Find the **largest rectangular area** that can be formed within the histogram.

The rectangle must be formed using **contiguous bars**.
