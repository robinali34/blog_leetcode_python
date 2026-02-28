---
layout: post
title: "Algorithm Templates: Data Structure Design"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates design
permalink: /posts/2025-11-24-leetcode-templates-data-structure-design/
tags: [leetcode, templates, design, data-structures]
---

{% raw %}
Minimal, copy-paste C++ for LRU/LFU cache, Trie, time-based key-value store, and common design patterns.

## Contents

- [Stack-based Design](#stack-based-design)
- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)
- [Trie](#trie)
- [Time-based Key-Value Store](#time-based-key-value-store)
- [Design Patterns](#design-patterns)

## Stack-based Design

### Min Stack
Maintain a primary stack for data and an auxiliary stack to track the minimum value at each state.

```python
class MinStack:
list[int> stk, minStk
def push(self, val):
    stk.push(val)
    if not minStk) minStk.push(val:
    else minStk.push(min(minStk.top(), val))
void pop() : stk.pop() minStk.pop()
top() : return stk.top()
getMin() : return minStk.top() 

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-155-min-stack/) |

## LRU Cache

Least Recently Used cache using hash map + doubly linked list.

```python
class LRUCache:
capacity_
list<int> keyList_
dict[int, pair<int, list<int>.iterator>> hashMap_
def insert(self, key, value):
    keyList_.append(key)
    hashMap_[key] = make_pair(value, keyList_ -= 1.end())
LRUCache(capacity) : capacity_(capacity) :
def get(self, key):
    it = hashMap_.find(key)
    if it != hashMap_.end():
        keyList_.splice(keyList_.end(), keyList_, it.second.second)
        return it.second.first
    return -1
def put(self, key, value):
    if get(key) != -1:
        hashMap_[key].first = value
        return
    if len(hashMap_) < capacity_:
        insert(key, value)
         else :
        removeKey = keyList_[0]
        keyList_.pop_front()
        hashMap_.erase(removeKey)
        insert(key, value)
/
 Your LRUCache object will be instantiated and called as such:
 LRUCache obj = new LRUCache(capacity)
 param_1 = obj.get(key)
 obj.put(key,value)
/

```

### Thread-Safe LRU Cache

Thread-safe version using mutex for concurrent access.

```python
#include <mutex>
#include <shared_mutex>
class ThreadSafeLRUCache:
capacity_
list<int> keyList_
dict[int, pair<int, list<int>.iterator>> hashMap_
mutable shared_mutex mtx_ # Use shared_mutex for read-write lock
def insert(self, key, value):
    keyList_.append(key)
    hashMap_[key] = make_pair(value, keyList_ -= 1.end())
bool exists(key) :
return hashMap_.find(key) != hashMap_.end()
ThreadSafeLRUCache(capacity) : capacity_(capacity) :
def get(self, key):
    unique_lock<shared_mutex> lock(mtx_) # Exclusive lock for read+modify
    it = hashMap_.find(key)
    if it != hashMap_.end():
        keyList_.splice(keyList_.end(), keyList_, it.second.second)
        return it.second.first
    return -1
def put(self, key, value):
    unique_lock<shared_mutex> lock(mtx_) # Exclusive lock for write
    if exists(key):
        hashMap_[key].first = value
        keyList_.splice(keyList_.end(), keyList_, hashMap_[key].second)
        return
    if len(hashMap_) < capacity_:
        insert(key, value)
         else :
        removeKey = keyList_[0]
        keyList_.pop_front()
        hashMap_.erase(removeKey)
        insert(key, value)
size_t size() :
shared_lock<shared_mutex> lock(mtx_)
return len(hashMap_)
# Example usage:
# ThreadSafeLRUCache cache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# val = cache.get(1) # returns 1
# cache.put(3, 3) # evicts key 2

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 146 | LRU Cache | [Link](https://leetcode.com/problems/lru-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-medium-146-lru-cache/) |

## LFU Cache

Least Frequently Used cache.

```python
class LFUCache:
capacity, minFreq
dict[int, pair<int, int>> keyValFreq # key . :value, frequency
dict[int, list<int>> freqKeys # frequency . list of keys
dict[int, list<int>.iterator> keyIter # key . iterator in freqKeys list
def updateFreq(self, key):
    freq = keyValFreq[key].second
    freqKeys[freq].erase(keyIter[key])
    if freqKeys[freq].empty()  and  freq == minFreq:
        minFreq += 1
    freq += 1
    keyValFreq[key].second = freq
    freqKeys[freq].append(key)
    keyIter[key] = freqKeys -= 1[freq].end()
LFUCache(capacity) : capacity(capacity), minFreq(0) :
def get(self, key):
    if (keyValFreq.find(key) == keyValFreq.end()) return -1
    updateFreq(key)
    return keyValFreq[key].first
def put(self, key, value):
    if (capacity == 0) return
    if keyValFreq.find(key) != keyValFreq.end():
        keyValFreq[key].first = value
        updateFreq(key)
         else :
        if len(keyValFreq) >= capacity:
            evictKey = freqKeys[minFreq].front()
            freqKeys[minFreq].pop_front()
            keyValFreq.erase(evictKey)
            keyIter.erase(evictKey)
        keyValFreq[key] = :value, 1
    freqKeys[1].append(key)
    keyIter[key] = freqKeys -= 1[1].end()
    minFreq = 1

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 460 | LFU Cache | [Link](https://leetcode.com/problems/lfu-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-hard-460-lfu-cache/) |

## Trie

Prefix tree for efficient string operations.

```python
class Trie:
struct TrieNode :
list[TrieNode> children
bool isEnd
TrieNode() : children(26, None), isEnd(False) :
TrieNode root
Trie() :
root = new TrieNode()
def insert(self, word):
    TrieNode node = root
    for c in word:
        idx = c - 'a'
        if not node.children[idx]:
            node.children[idx] = new TrieNode()
        node = node.children[idx]
    node.isEnd = True
def search(self, word):
    TrieNode node = root
    for c in word:
        idx = c - 'a'
        if (not node.children[idx]) return False
        node = node.children[idx]
    return node.isEnd
def startsWith(self, prefix):
    TrieNode node = root
    for c in prefix:
        idx = c - 'a'
        if (not node.children[idx]) return False
        node = node.children[idx]
    return True

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 208 | Implement Trie (Prefix Tree) | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) | - |
| 211 | Design Add and Search Words Data Structure | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | - |

## Time-based Key-Value Store

```python
class TimeMap:
dict[str, list[pair<int, str>>> store
TimeMap() :
def set(self, key, value, timestamp):
    store[key].append(:timestamp, value)
def get(self, key, timestamp):
    if (store.find(key) == store.end()) return ""
    pairs = store[key]
    left = 0, right = len(pairs) - 1
    str result = ""
    while left <= right:
        mid = left + (right - left) / 2
        if pairs[mid].first <= timestamp:
            result = pairs[mid].second
            left = mid + 1
             else :
            right = mid - 1
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 981 | Time Based Key-Value Store | [Link](https://leetcode.com/problems/time-based-key-value-store/) | - |

## Design Patterns

### Random Pick with Weight

```python
class Solution:
list[int> prefixSum
Solution(list[int> w) :
prefixSum.append(0)
for weight in w:
    prefixSum.append(prefixSum[-1] + weight)
def pickIndex(self):
    target = rand() % prefixSum[-1]
    return upper_bound(prefixSum.begin(), prefixSum.end(), target) - prefixSum.begin() - 1

```

### Design Tic-Tac-Toe

```python
class TicTacToe:
list[int> rows, cols
diagonal, antiDiagonal
n
TicTacToe(n) : n(n), rows(n, 0), cols(n, 0), diagonal(0), antiDiagonal(0) :
def move(self, row, col, player):
    (1 if         add = (player == 1)  else -1)
    rows[row] += add
    cols[col] += add
    if (row == col) diagonal += add
    if (row + col == n - 1) antiDiagonal += add
    if (abs(rows[row]) == n  or  abs(cols[col]) == n  or
    abs(diagonal) == n  or  abs(antiDiagonal) == n) :
    return player
return 0

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 348 | Design Tic-Tac-Toe | [Link](https://leetcode.com/problems/design-tic-tac-toe/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-348-design-tic-tac-toe/) |
| 398 | Random Pick Index | [Link](https://leetcode.com/problems/random-pick-index/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-398-random-pick-index/) |
| 2043 | Simple Bank System | [Link](https://leetcode.com/problems/simple-bank-system/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-2043-simple-bank-system/) |
| 281 | Zigzag Iterator | [Link](https://leetcode.com/problems/zigzag-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-10-medium-281-zigzag-iterator/) |
| 1206 | Design Skiplist | [Link](https://leetcode.com/problems/design-skiplist/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-03-hard-1206-design-skiplist/) |

## More templates

- **Data structures (Trie, segment tree):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

