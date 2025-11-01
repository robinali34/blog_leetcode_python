---
layout: post
title: "Python Quick Reference for LeetCode"
date: 2025-09-23 23:33:00 -0000
categories: python data-structures reference cheat-sheet programming containers algorithms competitive-programming
---

# 📚 Python Quick Reference for LeetCode

---

## 🧰 Containers

### ✅ Strings

```python
len(s)                    # Length of the string
s[i]                      # Access character at index
s[pos:pos+len]            # Substring
s.find("abc")             # Find position of substring (-1 if not found)
s.replace(old, new)       # Replace substring
s[start:end]              # Slice string
s += "abc"                # Append
str(x)                    # Convert int to string
int(s)                    # Convert string to int
```

---

### ✅ Lists (Python equivalent of `std::vector`)

```python
len(v)                    # Length
v.append(x)               # Add element at end
v.pop()                   # Remove last element
v.pop(i)                  # Remove element at index i
v[i]                      # Access element at index
v[0]                      # First element
v[-1]                     # Last element
v.clear()                 # Clear list
v.insert(i, x)            # Insert x at index i
v.remove(x)               # Remove first occurrence of x
sorted(v)                 # Return sorted list
v.sort()                  # Sort in place
v.reverse()               # Reverse in place
```

---

### ✅ Arrays (using lists)

```python
arr = [0] * 100           # Array of 100 zeros
arr = [1, 2, 3, 4, 5]     # Initialize array
```

---

### ✅ Sets

```python
s = set()
s.add(x)                  # Add element
s.remove(x)               # Remove element (raises KeyError if not found)
s.discard(x)              # Remove element (no error if not found)
x in s                    # Check membership
len(s)                    # Size
# Note: Sets don't have lower_bound/upper_bound like C++
# Use sorted(set) for ordered operations
```

---

### ✅ Dictionaries (Maps)

```python
m = {}                    # Empty dict
m = dict()                # Empty dict
m[key] = val              # Assign value
m.get(key, default)       # Get value with default
key in m                  # Check if key exists
m.keys()                  # Iterate keys
m.values()                # Iterate values
m.items()                 # Iterate (key, value) pairs
for k, v in m.items():    # Iterate key-value pairs
    pass
```

---

## 🔄 Algorithms

### ✅ Sorting & Searching

```python
sorted(lst)                        # Return sorted list
lst.sort()                         # Sort in place
lst.sort(reverse=True)             # Sort descending
lst.reverse()                      # Reverse in place

import bisect
bisect.bisect_left(lst, x)         # Lower bound (first pos >= x)
bisect.bisect_right(lst, x)        # Upper bound (first pos > x)
x in lst                           # Linear search
```

---

### ✅ Min / Max / Others

```python
min(a, b)
max(a, b)
a, b = b, a                       # Swap
sum(lst)                          # Sum of elements
lst.count(x)                      # Count occurrences of x
from itertools import permutations
list(permutations(lst))           # All permutations
```

---

## 📐 Math Utilities

```python
abs(x)
pow(a, b)
import math
math.sqrt(x)
math.gcd(a, b)                    # GCD
math.lcm(a, b)                    # LCM (Python 3.9+)
```

---

## 🧵 Queues, Stacks, Deques

### ✅ Queue (using collections.deque)

```python
from collections import deque
q = deque()
q.append(x)                       # Add to end
q.popleft()                       # Remove from front
q[0]                              # Front element
q[-1]                             # Back element
len(q) == 0                       # Check if empty
```

### ✅ Stack (using list)

```python
s = []
s.append(x)                       # Push
s.pop()                           # Pop
s[-1]                             # Top
len(s) == 0                       # Check if empty
```

### ✅ Deque

```python
from collections import deque
dq = deque()
dq.appendleft(x)                  # Add to front
dq.append(x)                      # Add to end
dq.popleft()                      # Remove from front
dq.pop()                          # Remove from end
```

### ✅ Priority Queue (Heap)

```python
import heapq
heap = []
heapq.heappush(heap, x)           # Push (min heap)
heapq.heappop(heap)               # Pop minimum
heap[0]                           # Peek minimum
# For max heap, negate values:
heapq.heappush(heap, -x)          # Push negative for max heap
max_val = -heapq.heappop(heap)    # Pop and negate back
```

---

## 🧠 Bit Manipulation

```python
bin(x).count('1')                 # Count 1-bits
x.bit_length()                    # Number of bits
x & (x - 1)                       # Remove lowest 1-bit
x & -x                            # Isolate lowest 1-bit
x >> 1                            # Right shift
x << 1                            # Left shift
```

---

## 📌 Common LeetCode Structures

| Concept       | Python Equivalent              |
|--------------|------------------------------|
| Hash Map     | `dict` or `collections.defaultdict` |
| Hash Set     | `set`                         |
| Tree Map     | Use `dict` (keys are hashed) or `sortedcontainers.SortedDict` |
| Tree Set     | Use `set` or `sortedcontainers.SortedSet` |
| Min Heap     | `heapq` (built-in)            |
| Max Heap     | `heapq` with negated values   |
| Stack        | `list`                        |
| Queue        | `collections.deque`           |
| Deque        | `collections.deque`           |
| StringBuilder| `list` + `''.join()` or `str` with `+=` |
| Graph        | `list[list[int]]` or `dict[list]` |

---

## ✍️ Input/Output Tips

```python
n = int(input())                  # Read integer
s = input()                       # Read line as string
s = input().strip()               # Read and strip whitespace

# Fast reading (multiple integers on one line)
nums = list(map(int, input().split()))

# File I/O
with open('input.txt', 'r') as f:
    data = f.read()
```

---
