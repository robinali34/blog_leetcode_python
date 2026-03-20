---
layout: post
title: "Python Quick Reference for LeetCode"
date: 2025-09-23 23:33:00 -0000
categories: python data-structures reference cheat-sheet programming containers algorithms competitive-programming
---

# 📚 Python Quick Reference for LeetCode

---

## Quick Imports

```python
from collections import Counter, defaultdict, deque
from functools import lru_cache
import bisect
import heapq
import math
```

## 🧰 Core Containers

### ✅ Strings

```python
len(s)                     # Length
s[i]                       # Access character
s[l:r]                     # Slice [l, r)
s.find("abc")              # First index or -1
s.count("a")               # Count substring/char
s.startswith("ab")         # Prefix check
s.endswith("yz")           # Suffix check
s.replace(old, new)        # Replace all
"-".join(parts)            # Join list[str] -> str
list(s)                    # str -> list[char]
int("123"), str(123)       # Conversion
```

### ✅ Lists (`std::vector` equivalent)

```python
v = [1, 2, 3]
len(v)
v.append(x)
v.pop()                    # pop last
v.pop(i)                   # pop index i
v.insert(i, x)
v.remove(x)                # first occurrence
v.extend([4, 5])
v.sort()                   # in-place
sorted(v)                  # new list
v.reverse()
v[::-1]                    # reversed copy
```

### ✅ 2D Arrays

```python
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]   # Correct
# Avoid: [[0] * cols] * rows  (shared rows bug)
```

### ✅ Set

```python
s = set()
s.add(x)
s.discard(x)               # no error if missing
s.remove(x)                # KeyError if missing
x in s
```

### ✅ Dict / Map

```python
m = {}
m[key] = val
val = m.get(key, 0)
key in m
for k, v in m.items():
    pass

dd = defaultdict(list)
dd[k].append(v)

freq = Counter(nums)       # value -> count
```

## 🔄 Sorting / Searching

```python
nums.sort()
nums.sort(reverse=True)
nums.sort(key=lambda x: (x[0], x[1]))

i = bisect.bisect_left(nums, x)   # first idx >= x
j = bisect.bisect_right(nums, x)  # first idx > x
```

### Binary Search Template

```python
def lower_bound(lo: int, hi: int, ok) -> int:
    # smallest x in [lo, hi] such that ok(x) is True
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## 🧵 Stack / Queue / Heap

### ✅ Stack

```python
st = []
st.append(x)
x = st.pop()
```

### ✅ Queue / BFS

```python
q = deque([start])
while q:
    node = q.popleft()
    for nei in graph[node]:
        q.append(nei)
```

### ✅ Heap (Priority Queue)

```python
heap = []
heapq.heappush(heap, x)
x = heapq.heappop(heap)
top = heap[0]

# max heap via negatives
heapq.heappush(heap, -x)
mx = -heapq.heappop(heap)
```

## 📐 Math + Bit

```python
abs(x)
math.gcd(a, b)
math.lcm(a, b)             # Python 3.9+
pow(a, b, mod)             # fast modular power

bin(x).count("1")          # popcount
x.bit_count()              # popcount (Python 3.8+)
x.bit_length()             # number of bits
x & (x - 1)                # clear lowest set bit
x & -x                     # isolate lowest set bit
x >> 1, x << 1
```

## 🧠 Common Patterns

### Prefix Sum

```python
pre = [0]
for x in nums:
    pre.append(pre[-1] + x)
# sum(nums[l:r+1]) = pre[r+1] - pre[l]
```

### Difference Array (range increment)

```python
diff = [0] * (n + 1)
for l, r, val in updates:
    diff[l] += val
    if r + 1 < len(diff):
        diff[r + 1] -= val

arr = [0] * n
cur = 0
for i in range(n):
    cur += diff[i]
    arr[i] = cur
```

### Sliding Window (longest valid window)

```python
left = 0
for right in range(len(nums)):
    # add nums[right]
    while not valid_window():
        # remove nums[left]
        left += 1
    # update answer using [left, right]
```

### Two Pointers (sorted array)

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        break
    if s < target:
        l += 1
    else:
        r -= 1
```

### Monotonic Stack (next greater)

```python
res = [-1] * len(nums)
st = []  # store indices, decreasing values
for i, x in enumerate(nums):
    while st and nums[st[-1]] < x:
        res[st.pop()] = i
    st.append(i)
```

## 🌳 Trees / Graphs Templates

### DFS (recursive tree)

```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
```

### DFS (graph with visited)

```python
def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(v)
```

### BFS Levels

```python
q = deque([start])
visited = {start}
steps = 0
while q:
    for _ in range(len(q)):
        u = q.popleft()
        if u == target:
            return steps
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    steps += 1
```

### Topological Sort (Kahn)

```python
indeg = [0] * n
for u in range(n):
    for v in graph[u]:
        indeg[v] += 1

q = deque([i for i in range(n) if indeg[i] == 0])
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
# DAG iff len(order) == n
```

### Union-Find (DSU)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
```

## 🧾 DP Quick Templates

### 1D DP

```python
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 1]  # transition example
```

### 2D DP

```python
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # example
```

### Memo DFS

```python
from functools import lru_cache

@lru_cache(None)
def solve(i, j):
    if base_case(i, j):
        return 0
    return min(solve(i - 1, j), solve(i, j - 1)) + cost(i, j)
```

## 📌 Common LeetCode Structures

| Concept | Python Equivalent |
|---|---|
| Hash Map | `dict`, `defaultdict` |
| Hash Set | `set` |
| Min Heap | `heapq` |
| Max Heap | `heapq` with negatives |
| Queue | `collections.deque` |
| Stack | `list` |
| Graph | `list[list[int]]` or `defaultdict(list)` |
| Frequency | `collections.Counter` |
| Ordered Map/Set | `sortedcontainers` (external lib) |

## ✍️ Fast I/O Tips

```python
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
```

## ⚠️ Common Python Pitfalls in Interviews

```python
# 1) Mutable default arguments (bad)
def f(x, memo={}): ...

# 2) 2D array aliasing (bad)
grid = [[0] * m] * n

# 3) Recursion depth (for deep DFS trees/graphs)
import sys
sys.setrecursionlimit(10**6)
```

---
