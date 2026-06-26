---
layout: post
title: "[Medium] 1146. Snapshot Array"
date: 2026-03-19 00:00:00 -0700
categories: [leetcode, medium, design, binary-search]
tags: [leetcode, medium, design, binary-search, map]
permalink: /2026/03/19/medium-1146-snapshot-array/
---

# [Medium] 1146. Snapshot Array

Implement a `SnapshotArray` that supports:

- `SnapshotArray(length)` — array of given length (all zeros)
- `set(index, val)` — set `index` to `val`
- `snap()` — take a snapshot, return `snap_id` (starts at 0)
- `get(index, snap_id)` — value at `index` at that snapshot

## Example

`SnapshotArray(3)`, `set(0,5)`, `snap()` → `0`, `set(0,6)`, `get(0,0)` → `5`

## Thinking process

### Naive: copy entire array — O(n) per snap

Copy the working array on every `snap()`. Simple but too slow when snapshots are frequent and changes are sparse.

### Optimal: change log per index + binary search

For each index, store a sorted map of `snap_id → value` (only when `set` is called).  
`snap()` just increments a counter — O(1).  
`get(index, snap_id)` finds the latest entry with key ≤ `snap_id` using `bisect_right` then stepping back one index.

## Solution 1: Naive (copy array)

```python
class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [0] * length
        self.snaps: list[list[int]] = []

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        sid = len(self.snaps)
        self.snaps.append(self.arr[:])
        return sid

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]
```

| Operation | Time | Space |
| --------- | ---- | ----- |
| `set` | O(1) | — |
| `snap` | O(n) | O(n) per snapshot |
| `get` | O(1) | — |

## Solution 2: Dict per index + binary search (optimal)

```python
import bisect


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [{0: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        sid = self.snap_id
        self.snap_id += 1
        return sid

    def get(self, index: int, snap_id: int) -> int:
        history = self.data[index]
        keys = list(history.keys())  # snap ids inserted in order
        i = bisect.bisect_right(keys, snap_id) - 1
        return history[keys[i]]
```

| Operation | Time | Space |
| --------- | ---- | ----- |
| `set` | O(log S) | — |
| `snap` | O(1) | — |
| `get` | O(log S) | — |

`S` = number of `set` calls on that index.

### Why `bisect_right` then step back?

`bisect_right(keys, snap_id)` is the first key **strictly greater** than `snap_id`. The previous key is the latest version active at `snap_id`.

```
data[0] = {0: 5, 3: 10, 7: 2}
get(0, 5) → keys bisect_right(5) → index of 7 → prev key 3 → 10
```

## Comparison

| Approach | `set` | `snap` | `get` | Space |
| -------- | ----- | ------ | ----- | ----- |
| Copy array | O(1) | O(n) | O(1) | O(n · snaps) |
| Dict + bisect | O(log S) | O(1) | O(log S) | O(total sets) |

## Common mistakes

- Forgetting `data[i][0] = 0` at init
- Using `bisect_left` instead of `bisect_right` (off-by-one at snapshot boundary)

## Key takeaways

- **Versioned data with sparse updates** → per-index change log + binary search
- `upper_bound` / `bisect_right` then decrement is the standard “latest version ≤ X” pattern

## Related & templates

- [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- [Data Structure Design](/posts/2025-11-24-leetcode-templates-data-structure-design/)
