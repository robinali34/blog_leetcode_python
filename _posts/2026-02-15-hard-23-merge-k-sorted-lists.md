---
layout: post
title: "[Hard] 23. Merge k Sorted Lists"
date: 2026-02-15 00:00:00 -0700
categories: [leetcode, hard, linked-list, divide-and-conquer, heap]
tags: [leetcode, hard, linked-list, divide-and-conquer, heap, merge]
permalink: /2026/02/15/hard-23-merge-k-sorted-lists/
---

# [Hard] 23. Merge k Sorted Lists

## Problem Statement

You are given an array of `k` linked lists, each sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

## Examples

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order
- The sum of `lists[i].length` will not exceed `10^4`

## Clarification Questions

1. **Empty input**: What if `lists` is empty? (Assumption: Return `None`.)
2. **Empty lists**: Can some lists be empty? (Assumption: Yes; skip them.)
3. **In-place**: Must we merge in place or can we create new nodes? (Assumption: Rewiring pointers is fine; O(1) extra space for divide & conquer.)
4. **Stability**: Any requirement on order of equal elements? (Assumption: Any valid merge order.)
5. **k and N**: Can k be very large? (Assumption: Yes — need O(N log k), not O(kN).)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force (5 min)** — Merge lists one by one: merge list 0 and 1, then merge result with list 2, etc. Time O(kN) in the worst case — too slow when k is large.

**Step 2: Min-heap (7 min)** — Push head of each list into a min-heap; pop smallest, append to result, push its next. Each of N nodes is pushed/popped once, O(log k) per operation → O(N log k). Space O(k) for the heap.

**Step 3: Divide & conquer (8 min)** — Pair lists and merge in rounds (like merge sort). Each round processes all N nodes once; number of rounds is O(log k). Time O(N log k), space O(1) extra. Optimal.

## Solution Approach

Let `k` = number of lists, `N` = total number of nodes. We must touch every node, so $\Omega(N)$.

### Key Insights:

1. **Lower bound**: Time is at least O(N).
2. **Sequential merge is bad**: Merging one-by-one can be O(kN); avoid re-traversing long lists.
3. **Two optimal approaches**: Min-heap (O(N log k) time, O(k) space) or divide & conquer (O(N log k) time, O(1) extra space).
4. **Merge two**: The base operation is merging two sorted lists in O(a + b); use it in a tree of merges.

### Why Sequential Merge Is Bad

If you merge one-by-one:

```
res = merge(lists[0], lists[1])
res = merge(res, lists[2])
res = merge(res, lists[3])
...
```

Worst case time is roughly $N + 2N + 3N + \cdots \approx O(kN)$. This TLEs when `k` is large because earlier merged results keep getting re-traversed.

### Balanced Merging

This is exactly like merge sort -- tree height is $\log k$. Each level processes all $N$ nodes once, so:

$$\text{Time} = O(N \log k)$$

### Why This Is $\log k$

Each round halves the number of lists:

```
k → k/2 → k/4 → k/8 → ... → 1
```

Number of rounds: $\log_2 k$. Each round processes all nodes once. Total: $N \cdot \log k$.

## Approach: Divide & Conquer -- $O(N \log k)$

Pair lists and merge them in rounds, halving the count each time. This avoids the repeated long traversals of sequential merging.

{% raw %}
```python
class Solution:
    def mergeTwo(self, a, b):
        dummy = ListNode(0)
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next

    def mergeKLists(self, lists):
        if not lists:
            return None
        n = len(lists)
        step = 1
        while step < n:
            for i in range(0, n - step, step * 2):
                lists[i] = self.mergeTwo(lists[i], lists[i + step])
            step *= 2
        return lists[0]
```
{% endraw %}

**Time**: $O(N \log k)$
**Space**: $O(1)$ extra (iterative, in-place pointer rewiring)

## Alternative: Min Heap (Priority Queue) -- $O(N \log k)$

Also optimal at $O(N \log k)$, but with $O(k)$ extra space for the heap.

**How it works:**

1. **Initialize** -- push the head of each non-empty list into a min-heap (size at most `k`)
2. **Pop** the smallest node from the heap and append it to the result
3. **Push** that node's `next` into the heap (if it exists)
4. Repeat until the heap is empty

The heap always holds at most one node per list, so each push/pop is $O(\log k)$. Over all $N$ nodes, total time is $O(N \log k)$.

**Why use a custom comparator struct?** Defining `Compare` as a struct makes the comparator reusable and avoids lambda overhead. The `priority_queue` in C++ is a max-heap by default, so we reverse the comparison (`a->val > b->val`) to get min-heap behavior.

{% raw %}
```python
import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        tail = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
```
{% endraw %}

**Time**: $O(N \log k)$ -- each of $N$ nodes is pushed/popped once, each operation $O(\log k)$
**Space**: $O(k)$ for the heap

## What Strong Candidates Notice

- `k` may be large with small lists, or `k` small with very large lists -- balanced merging handles both
- Divide & conquer uses $O(1)$ extra space vs $O(k)$ for the heap
- Sequential merge degrades to $O(kN)$ -- always avoid it

## Edge Cases

- `k = 0` -- return `None`
- Some lists are empty -- skip them
- All lists are empty -- return `None`
- Single list -- return it directly

## Key Takeaways

When you see **"merge k sorted ..."**, immediately think:
- **Multi-way merge** via min heap
- **Divide & conquer** tree merging

This is a pattern problem. Balanced merging prevents repeated long traversals, bringing complexity from $O(kN)$ down to $O(N \log k)$.

### Related Problems:

- [LC 21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — Base case for this problem
- [LC 148: Sort List](https://leetcode.com/problems/sort-list/) — Merge sort on linked list
- [LC 378: Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) — Multi-way merge variant

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
