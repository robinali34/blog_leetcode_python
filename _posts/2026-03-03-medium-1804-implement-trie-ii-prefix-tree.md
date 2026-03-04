---
layout: post
title: "1804. Implement Trie II (Prefix Tree)"
date: 2026-03-03 00:00:00 -0700
categories: [leetcode, medium, trie, data-structure]
tags: [leetcode, medium, trie, prefix-tree, design]
permalink: /2026/03/03/medium-1804-implement-trie-ii-prefix-tree/
---

# 1804. Implement Trie II (Prefix Tree)

## Problem Statement

Design a trie (prefix tree) that supports the following operations:

- `insert(word)`: Insert a string `word` into the data structure.
- `countWordsEqualTo(word)`: Return how many times `word` was inserted.
- `countWordsStartingWith(prefix)`: Return how many words in the trie start with `prefix`.
- `erase(word)`: Remove one occurrence of `word` from the trie. It is guaranteed that `word` exists at least once when `erase` is called.

You may assume:
- All words consist only of lowercase English letters `'a'` to `'z'`.

## Examples

**Example 1:**

```python
Input:
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith",
 "erase", "countWordsEqualTo", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"]]

Output:
[null, null, null, 2, 2, null, 1, 1]
```

Explanation:
- There are two `"apple"` after two inserts.
- Two words start with `"app"` (`"apple"`, `"apple"`).
- After one `erase("apple")`, we have one `"apple"` and still one word starting with `"app"`.

## Constraints

- Number of operations ≤ \(10^5\)
- Sum of lengths of all inserted words ≤ \(10^5\)
- Words consist only of lowercase English letters `'a'`–`'z'`
- `erase(word)` is called only if `word` has been inserted at least once

## Clarification Questions

1. **Duplicates**: Can the same word be inserted multiple times and should we count all occurrences?  
   **Assumption**: Yes — each insert increments the count; `countWordsEqualTo` returns that count.
2. **Erase precondition**: Is it guaranteed that `erase(word)` is only called when `word` exists?  
   **Assumption**: Yes — so we don’t need to handle invalid erases.
3. **Character set**: Only `'a'`–`'z'` (26 lowercase letters)?  
   **Assumption**: Yes — we can index children by array of size 26.
4. **Performance target**: Do we need near `O(L)` per operation, where `L` is word length?  
   **Assumption**: Yes — standard for trie operations.
5. **Memory trade-off**: Is it okay to keep extra counters in each node to speed up prefix queries?  
   **Assumption**: Yes — typical approach for this problem.  

## Interview Deduction Process (20 minutes)

**Step 1: Basic trie (5 min)**  
Standard trie only supports:
- `insert(word)`
- `search(word)`
- `startsWith(prefix)`

Each node holds a flag `is_end` to mark whether a full word ends there.

**Step 2: Need counts, not just existence (7 min)**  
The operations here require counting:
- Exact word count.
- Number of words starting with a prefix.

We can store two extra integers in each node:
- `words_ending_here`: how many words end at this node.
- `words_starting_here`: how many words pass through this node (including those ending here).

This lets us:
- Increment `words_starting_here` on the path when inserting.
- Increment `words_ending_here` at the final node.
- For `countWordsEqualTo`, follow the word and return `words_ending_here` at the end node.
- For `countWordsStartingWith`, follow the prefix and return `words_starting_here` at that node.

**Step 3: Erase logic (8 min)**  
To erase one occurrence of `word`:
- Traverse the same path as insert.
- On each node along the path (except root), decrement `words_starting_here`.
- At the final node, decrement `words_ending_here`.

We don’t strictly need to delete nodes from memory; leaving them is fine as long as counts stay correct. This keeps implementation simple and remains within constraints.

## Solution Approach

We implement:

- A `TrieNode` class with:
  - `links`: fixed-size array `[None] * 26` for child pointers.
  - `words_ending_here`: integer counter.
  - `words_starting_here`: integer counter.
- A `Trie` class with:
  - `root`: the root `TrieNode`.
  - `insert`, `countWordsEqualTo`, `countWordsStartingWith`, and `erase` as described.

Each operation walks down at most `L` nodes where `L` is the word or prefix length.

### Key Insights

1. **Per-node counters**  
   - `words_ending_here` supports exact word counts.  
   - `words_starting_here` supports fast prefix counts without scanning entire subtrees.

2. **Erase is symmetric to insert**  
   - Insert increments counters along the path.  
   - Erase decrements counters along the same path.

3. **No need for structural node deletion**  
   - Since constraints are moderate and we only require correct counts, we can skip pruning unused nodes.

4. **Array-based children**  
   - Using a fixed array of length 26 avoids dictionary overhead and is safe because alphabet is small and known.

## Python Implementation

```python
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.words_ending_here = 0
        self.words_starting_here = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.links[idx] is None:
                node.links[idx] = TrieNode()
            node = node.links[idx]
            node.words_starting_here += 1
        node.words_ending_here += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.links[idx] is None:
                return 0
            node = node.links[idx]
        return node.words_ending_here

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if node.links[idx] is None:
                return 0
            node = node.links[idx]
        return node.words_starting_here

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            node = node.links[idx]
            node.words_starting_here -= 1
        node.words_ending_here -= 1
```

## Algorithm Explanation

- **Insert**:
  - Walk down the trie, creating nodes as needed.
  - For each node on the path after moving to the child, increment `words_starting_here`.
  - At the last node, increment `words_ending_here`.

- **countWordsEqualTo**:
  - Walk the word; if at any step the link is missing, return `0`.
  - Otherwise, return `words_ending_here` at the terminal node.

- **countWordsStartingWith**:
  - Walk the prefix; if any link is missing, return `0`.
  - Otherwise, return `words_starting_here` at the last node of the prefix.

- **erase**:
  - Walk the word again, assuming it exists.
  - On each node along the path after moving to child, decrement `words_starting_here`.
  - At the end node, decrement `words_ending_here`.

Because we always update counts consistently, queries remain correct even after multiple inserts and erases.

## Complexity Analysis

Let \(L\) be the length of the word or prefix:

- **Time Complexity**:
  - `insert`: \(O(L)\)
  - `countWordsEqualTo`: \(O(L)\)
  - `countWordsStartingWith`: \(O(L)\)
  - `erase`: \(O(L)\)

- **Space Complexity**:
  - Worst case \(O(N \cdot \Sigma)\), where \(N\) is total number of characters stored and \(\Sigma = 26\) for lowercase letters. For typical usage this is acceptable.

## Edge Cases

- Inserting the same word many times — counts increase correctly and all operations remain \(O(L)\).
- Erasing a word multiple times — as long as it was inserted at least that many times, counters stay non-negative.
- Querying a word or prefix that does not exist — returns `0` without errors.

## Common Mistakes

- Forgetting to maintain `words_starting_here` for each node on the path, which breaks prefix counts.
- Not decrementing `words_starting_here` during `erase`, leading to overcounted `countWordsStartingWith`.
- Mishandling the assumption that `erase(word)` is always valid (e.g., going negative on counters without checks).

## Related Problems

- [LC 208: Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) — Basic trie with insert/search/startsWith.
- [LC 211: Add and Search Word - Data structure design](https://leetcode.com/problems/design-add-and-search-words-data-structure/) — Trie with wildcard search.
- [LC 212: Word Search II](https://leetcode.com/problems/word-search-ii/) — Backtracking on a board using a trie of words.

