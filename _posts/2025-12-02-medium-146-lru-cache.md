---
layout: post
title: "[Medium] 146. LRU Cache"
date: 2025-12-02 00:00:00 -0800
categories: leetcode algorithm medium cpp design data-structures hash-map linked-list problem-solving
---

# [Medium] 146. LRU Cache

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in **O(1)** average time complexity.

## Examples

**Example 1:**
```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **LRU definition**: What does "Least Recently Used" mean? (Assumption: The item that hasn't been accessed for the longest time - need to track access order)

2. **Cache operations**: What operations should the cache support? (Assumption: get(key) - retrieve value, put(key, value) - insert/update, both operations mark item as recently used)

3. **Eviction policy**: When should we evict items? (Assumption: When cache is full and we need to add a new item, evict the least recently used item)

4. **Capacity**: What is the cache capacity? (Assumption: Fixed capacity specified in constructor - cannot exceed this limit)

5. **Return values**: What should get() return if key doesn't exist? (Assumption: Return -1 - key not found in cache)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Use a hash map to store key-value pairs and a list/array to track access order. For `get`, search the list to find the key, move it to the end, and return the value. For `put`, add/update the hash map and move the key to the end of the list. When capacity is exceeded, remove the first element from the list. This approach has O(n) time for `get` operations due to list searching, which doesn't meet the O(1) requirement.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a hash map and a doubly linked list: hash map stores key-to-node mappings, doubly linked list maintains access order. For `get`, use hash map to find the node in O(1), move it to the end of the list. For `put`, add/update hash map, add node to end of list, remove head if capacity exceeded. However, implementing a doubly linked list from scratch requires careful pointer management and can be error-prone.

**Step 3: Optimized Solution (8 minutes)**

Use hash map + `std::list`: hash map stores `key -> iterator` mappings, `std::list` maintains access order with pairs `(key, value)`. For `get`, use hash map to get iterator in O(1), use `splice` to move node to end in O(1). For `put`, if key exists, update value and move to end. If new key, add to end and remove head if capacity exceeded. This achieves O(1) for both operations using standard library containers. The key insight is that `std::list::splice` allows O(1) node movement, and hash map provides O(1) lookup, combining to achieve O(1) operations.

## Solution: Hash Map + Doubly Linked List

**Time Complexity:** O(1) for both `get` and `put`  
**Space Complexity:** O(capacity)

We use a combination of hash map and doubly linked list to achieve O(1) operations. The hash map stores key-to-iterator mappings, and the doubly linked list maintains the order of recently used items.

### Solution: OrderedDict (same idea as hash map + linked order)

Python’s `OrderedDict` keeps insertion order and supports `move_to_end` and `popitem(last=False)` in O(1) amortized time—equivalent to the C++ `list` + `unordered_map` + `splice` pattern.

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            return
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### Key Points

1. **`OrderedDict`**: Preserves insertion order; the oldest item is at the front (LRU) after evictions.
2. **`move_to_end(key)`**: Marks a key as most recently used after a `get` or when updating an existing key.
3. **`popitem(last=False)`**: Evicts the LRU entry when size exceeds `capacity`.
4. **`get()`**: If the key exists, move it to the MRU side and return the value; otherwise `-1`.
5. **`put()`**: Insert or update; if the cache grows past `capacity`, remove the front (LRU) item.

## Thread-Safe LRU Cache

Thread-safe version using a lock: `get` and `put` both mutate order, so they take the same exclusive lock. A read–write lock only helps if `get` were read-only, which it is not for an LRU.

```python
import threading
from collections import OrderedDict


class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: int) -> int:
        with self._lock:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        with self._lock:
            if key in self.cache:
                self.cache.move_to_end(key)
                self.cache[key] = value
                return
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)

    def size(self) -> int:
        with self._lock:
            return len(self.cache)
```

### Thread-Safe Implementation Details

1. **`threading.Lock`**: One mutex protects the `OrderedDict`; every method that reads or mutates the cache holds this lock.
2. **`get` and `put`**: Both take the same lock because LRU order changes on every successful `get` (move-to-end) and on `put`.
3. **`size()`**: Uses the same lock so the count is not observed mid-mutation from another thread.
4. **Note**: A read–write lock only helps if `get` were read-only; for an LRU, `get` updates order, so an exclusive lock (or the same pattern as here) is appropriate.

## How the Algorithm Works

### Data Structure Design

```
Hash Map:                    Doubly Linked List:
key -> (value, iterator)      [1] <-> [2] <-> [3]
                              (LRU)            (MRU)
```

### Operation Flow

**Get Operation:**
1. Look up key in hash map → O(1)
2. If found, move node to end (most recently used) using `splice()` → O(1)
3. Return value

**Put Operation:**
1. Check if key exists via `get()` → O(1)
2. If exists: update value (already moved to end by `get()`) → O(1)
3. If new:
   - Check capacity
   - If full: remove front node (LRU) → O(1)
   - Insert at end → O(1)

### Example Walkthrough

```
capacity = 2

put(1, 1):  cache = {1: (1, it1)}
            list: [1]

put(2, 2):  cache = {1: (1, it1), 2: (2, it2)}
            list: [1] <-> [2]

get(1):     Move 1 to end using splice
            list: [2] <-> [1]
            return 1

put(3, 3):  get(3) returns -1, capacity full
            Remove front (key 2), insert 3 at end
            cache = {1: (1, it1), 3: (3, it3)}
            list: [1] <-> [3]
```

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| `get(key)` | O(1) | O(1) |
| `put(key, value)` | O(1) | O(1) |
| **Overall** | **O(1)** | **O(capacity)** |

## Why This Approach Works

1. **Hash map**: Provides O(1) lookup by key
2. **Doubly linked list**: Maintains insertion order and allows O(1) removal/insertion
3. **Iterator storage**: Hash map stores iterators to list nodes for O(1) access
4. **`splice()` optimization**: Moves nodes without copying, maintaining O(1) complexity

## Edge Cases

1. **Capacity = 1**: Only one item can exist
2. **Get non-existent key**: Returns -1
3. **Update existing key**: Moves to end, doesn't increase size
4. **Multiple puts**: Evicts oldest when capacity exceeded

## Common Mistakes

1. **Not moving to end on get**: Must update access order
2. **Wrong eviction order**: Remove from front (LRU), not back
3. **Invalid iterator after modification**: Use `splice()` which preserves iterators
4. **Not handling existing key in put**: Must check and update, not just insert

## Related Problems

- [460. LFU Cache](https://leetcode.com/problems/lfu-cache/) - Least Frequently Used
- [432. All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)
- [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)

