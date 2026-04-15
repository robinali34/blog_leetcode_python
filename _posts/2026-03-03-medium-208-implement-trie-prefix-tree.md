---
layout: post
title: "[Medium] 208. Implement Trie (Prefix Tree)"
date: 2026-03-03 00:00:00 -0700
categories: [leetcode, medium, trie, data-structure]
tags: [leetcode, medium, trie, prefix-tree, design]
permalink: /2026/03/03/medium-208-implement-trie-prefix-tree/
---

# [Medium] 208. Implement Trie (Prefix Tree)

## Problem Statement

Design a trie (prefix tree) with the following operations:

- `insert(word)`: Inserts the string `word` into the trie.
- `search(word)`: Returns `True` if the string `word` is in the trie.
- `startsWith(prefix)`: Returns `True` if there is any string in the trie that starts with the string `prefix`.

All words consist of lowercase English letters `'a'` to `'z'`.

## Examples

**Example:**

```python
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, True, False, True, null, True]
```

Explanation:
- Insert `"apple"`.
- `search("apple")` → `True`
- `search("app")` → `False`
- `startsWith("app")` → `True`
- Insert `"app"`.
- `search("app")` → `True`

## Constraints

- Number of operations ≤ \(10^4\)
- Sum of lengths of all strings ≤ \(10^5\)
- Each string consists only of lowercase English letters `'a'`–`'z'`

## Clarification Questions

1. **Duplicates**: If we insert the same word multiple times, does it change `search` / `startsWith`?  
   **Assumption**: `search` and `startsWith` are boolean existence checks, so duplicates do not change the result.
2. **Character set**: Only `'a'`–`'z'`?  
   **Assumption**: Yes — we can use a fixed array of 26 child pointers.
3. **Empty string**: Do we need to support empty words or prefixes?  
   **Assumption**: Problem usually focuses on non-empty lowercase strings; implementation naturally returns `True` for `startsWith("")` if desired.
4. **Performance**: Target is near `O(L)` per operation where `L` is word/prefix length?  
   **Assumption**: Yes — standard for trie.

## Interview Deduction Process (20 minutes)

**Step 1: Direct data structure choice (5 min)**  
We need fast:
- Insert word
- Exact word lookup
- Prefix lookup

Using a hash set only gives us exact matches, not efficient prefix search. A trie naturally supports both exact and prefix queries in \(O(L)\).

**Step 2: Node design (7 min)**  
Each trie node needs:
- Up to 26 children (one per letter).
- A flag indicating whether a **word ends** at this node.

We can store children as:
- A dictionary `dict[char, node]`, or
- A fixed-size array of length 26 when alphabet is known and small — more compact and faster access.

**Step 3: Operations (8 min)**  
- `insert`:
  - Walk from root following each character.
  - Create missing child nodes as needed.
  - Mark the last node as a word end.
- `search`:
  - Walk down by characters.
  - If any link is missing, return `False`.
  - Return `True` only if the final node is marked as word end.
- `startsWith`:
  - Same traversal as `search`, but we only require reaching the final node (no need for `is_end` to be `True`).

## Solution Approach

We implement:

- `TrieNode`:
  - `links`: `[None] * 26` child pointers.
  - `is_end`: `bool` marking end of a word.
  - Helper methods:
    - `contains_key(ch)`
    - `get(ch)`
    - `put(ch, node)`
    - `set_end()`
    - `is_word()`

- `Trie`:
  - `root`: the root `TrieNode`.
  - `insert`, `_search_prefix`, `search`, `startsWith` methods.

Each operation simply walks characters from root, mapping `ch` to index `ord(ch) - ord('a')`.

### Key Insights

1. **Prefix sharing**  
   All words sharing a prefix reuse the same path from the root, saving memory and time.

2. **`_search_prefix` helper**  
   Both `search` and `startsWith` share the same traversal logic; we can encapsulate it in a helper that returns the last node (or `None`).

3. **`is_end` vs path existence**  
   - Reaching a node means the prefix exists.  
   - `is_end == True` means a full word was inserted ending at that node.

## Python Implementation

```python
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def get(self, ch: str) -> "TrieNode":
        return self.links[ord(ch) - ord("a")]

    def put(self, ch: str, node: "TrieNode") -> None:
        self.links[ord(ch) - ord("a")] = node

    def set_end(self) -> None:
        self.is_end = True

    def is_word(self) -> bool:
        return self.is_end


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def _search_prefix(self, word: str) -> "TrieNode | None":
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_word()

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None
```

## Algorithm Explanation

- **insert**:
  - For each character in `word`, we ensure there is a child node.
  - At the end, mark `is_end = True` for that final node.

- **_search_prefix**:
  - Follow the path for either a full word or a prefix.
  - If at any step a needed child is missing, return `None`.
  - Otherwise return the node at the end of traversal.

- **search**:
  - Uses `_search_prefix` and additionally checks that the final node is a word end.

- **startsWith**:
  - Uses `_search_prefix` and only checks that the returned node is not `None`.

## Complexity Analysis

Let \(L\) be the length of the word or prefix:

- **Time Complexity**:
  - `insert`: \(O(L)\)
  - `search`: \(O(L)\)
  - `startsWith`: \(O(L)\)

- **Space Complexity**:
  - In worst case, \(O(N \cdot \Sigma)\) for all nodes and children, where \(N\) is total characters stored and \(\Sigma = 26\).

## Edge Cases

- Searching for a word that is a prefix of another word (e.g., `"app"` when only `"apple"` is inserted`) — `search("app")` should be `False` but `startsWith("app")` is `True`.
- Duplicated inserts — `search` and `startsWith` remain `True`; we don’t maintain counts here.
- Non-existent prefix — `_search_prefix` returns `None`, and both `search` and `startsWith` handle it gracefully.

## Common Mistakes

- Forgetting to mark the final node as `is_end = True` during insertion, causing `search` to fail even when nodes exist.
- Mixing up exact word search with prefix search, returning `True` for words that are just prefixes.
- Using inefficient per-node structures when alphabet is fixed and small (array is simpler and faster than dict here).

## Related Problems

- [LC 1804: Implement Trie II (Prefix Tree)](/2026/03/03/medium-1804-implement-trie-ii-prefix-tree/) — Extends trie with counts and erase operation.
- [LC 211: Add and Search Word - Data structure design](https://leetcode.com/problems/design-add-and-search-words-data-structure/) — Trie with wildcard matching.
- [LC 212: Word Search II](https://leetcode.com/problems/word-search-ii/) — Use a trie of words to speed up backtracking on a grid.

