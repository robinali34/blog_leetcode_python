---
layout: post
title: "Algorithm Templates: Greedy"
date: 2025-12-14 00:00:00 -0800
categories: leetcode templates greedy
permalink: /posts/2025-12-14-leetcode-templates-greedy/
tags: [leetcode, templates, greedy, algorithms]
---

{% raw %}
Greedy algorithms are among the most elegant tools in competitive programming — when they work, they're simpler and faster than dynamic programming. This guide covers the core greedy patterns you'll encounter on LeetCode, with ready-to-use C++ templates for interval scheduling, activity selection, fractional knapsack, and greedy strategies on arrays and strings. Each section includes the key intuition so you know *why* the greedy choice is correct, not just *how* to code it.

> **New to Greedy?** Greedy algorithms make the locally best choice at each step. Unlike DP, you never reconsider previous choices. The challenge is proving that local optimality leads to global optimality — if you can, greedy is simpler and faster than DP.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 320" width="520" height="320" font-family="Segoe UI, Arial, sans-serif" font-size="14">
  <defs>
    <marker id="ah" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#7a6e6a"/>
    </marker>
  </defs>
  <rect width="520" height="320" rx="12" fill="#f4f0ec"/>
  <text x="260" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#5b4f4a">Greedy vs DP — Which one?</text>
  <rect x="140" y="50" width="240" height="48" rx="8" fill="#c5b4a7" stroke="#7a6e6a" stroke-width="1.5"/>
  <text x="260" y="70" text-anchor="middle" fill="#3b302b" font-size="13">Can I prove local choice</text>
  <text x="260" y="87" text-anchor="middle" fill="#3b302b" font-size="13">is globally optimal?</text>
  <line x1="200" y1="98" x2="130" y2="145" stroke="#7a6e6a" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="145" y="125" text-anchor="middle" fill="#6b8e6b" font-weight="bold" font-size="13">Yes</text>
  <line x1="320" y1="98" x2="390" y2="145" stroke="#7a6e6a" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="375" y="125" text-anchor="middle" fill="#b07070" font-weight="bold" font-size="13">No</text>
  <rect x="50" y="148" width="160" height="44" rx="8" fill="#a8c3a8" stroke="#6b8e6b" stroke-width="1.5"/>
  <text x="130" y="175" text-anchor="middle" fill="#2d4a2d" font-weight="bold" font-size="14">Use Greedy</text>
  <rect x="310" y="148" width="160" height="44" rx="8" fill="#c3a8a8" stroke="#b07070" stroke-width="1.5"/>
  <text x="390" y="175" text-anchor="middle" fill="#4a2d2d" font-weight="bold" font-size="14">Try DP</text>
  <rect x="20" y="210" width="220" height="95" rx="8" fill="#d6ccc4" stroke="#b0a49a" stroke-width="1"/>
  <text x="130" y="232" text-anchor="middle" fill="#5b4f4a" font-size="12" font-weight="bold">Greedy is great when:</text>
  <text x="130" y="252" text-anchor="middle" fill="#5b4f4a" font-size="11">- Optimal substructure exists</text>
  <text x="130" y="269" text-anchor="middle" fill="#5b4f4a" font-size="11">- Greedy choice property holds</text>
  <text x="130" y="286" text-anchor="middle" fill="#5b4f4a" font-size="11">- O(n log n) or O(n) typical</text>
  <rect x="280" y="210" width="220" height="95" rx="8" fill="#d6ccc4" stroke="#b0a49a" stroke-width="1"/>
  <text x="390" y="232" text-anchor="middle" fill="#5b4f4a" font-size="12" font-weight="bold">DP is needed when:</text>
  <text x="390" y="252" text-anchor="middle" fill="#5b4f4a" font-size="11">- Overlapping subproblems</text>
  <text x="390" y="269" text-anchor="middle" fill="#5b4f4a" font-size="11">- Must explore all choices</text>
  <text x="390" y="286" text-anchor="middle" fill="#5b4f4a" font-size="11">- O(n²) or O(n·W) typical</text>
</svg>
</div>

## Contents

- [Greedy Algorithm Overview](#greedy-algorithm-overview)
- [Interval Scheduling](#interval-scheduling)
- [Activity Selection](#activity-selection)
- [Fractional Knapsack](#fractional-knapsack)
- [Greedy on Arrays](#greedy-on-arrays)
- [Greedy on Strings](#greedy-on-strings)
- [Greedy with Sorting](#greedy-with-sorting)

## Greedy Algorithm Overview

Greedy algorithms make locally optimal choices at each step, hoping to find a global optimum. They work well when:
- The problem has optimal substructure
- The greedy choice property holds (locally optimal choice leads to global optimum)
- No need to reconsider previous choices

### Key Principles

1. **Greedy Choice Property**: A global optimum can be reached by making locally optimal choices. At every step, you pick what looks best *right now* and trust that this leads to the best overall answer.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems. After making a greedy choice, the remaining problem is a smaller instance of the same type.
3. **No Backtracking**: Once a choice is made, it's never reconsidered. This is what makes greedy algorithms fast — but it also means you need to *prove* the greedy strategy is correct before relying on it.
4. **Exchange Argument**: The standard proof technique — assume an optimal solution differs from the greedy one, then show you can "exchange" a choice to match the greedy solution without making it worse.

## Interval Scheduling

**When to use:** The problem mentions "non-overlapping intervals", "minimum rooms", "merge intervals", or asks you to maximize/minimize a count of intervals that don't conflict.

Greedy approach: Sort by end time, always pick the interval that ends earliest.

```python
# Non-overlapping Intervals
def eraseOverlapIntervals(self, intervals):
    if(not intervals) return 0
    sort(intervals.begin(), intervals.end(), [](list[int> a, list[int> b) :
    return a[1] < b[1]  # Sort by end time
    )
    count = 1
    end = intervals[0][1]
    for(i = 1 i < len(intervals) i += 1) :
    if intervals[i][0] >= end:
        count += 1
        end = intervals[i][1]
return len(intervals) - count

```

## Activity Selection

**When to use:** The problem says "maximum activities", "schedule as many as possible", or "select non-conflicting events" — essentially interval scheduling phrased as a selection problem.

Similar to interval scheduling, select maximum number of non-overlapping activities.

```python
# Maximum number of non-overlapping intervals
def maxNonOverlappingIntervals(self, intervals):
    if(not intervals) return 0
    sort(intervals.begin(), intervals.end(), [](list[int> a, list[int> b) :
    return a[1] < b[1]
    )
    count = 1
    end = intervals[0][1]
    for(i = 1 i < len(intervals) i += 1) :
    if intervals[i][0] >= end:
        count += 1
        end = intervals[i][1]
return count

```

## Fractional Knapsack

**When to use:** You can take *fractions* of items (unlike 0/1 knapsack which needs DP). Look for "maximize value with limited capacity" where partial selections are allowed.

Greedy approach: Sort items by value/weight ratio, take items with highest ratio first.

```python
# Fractional Knapsack (not a LeetCode problem, but classic greedy)
struct Item :
value, weight
double ratio
def fractionalKnapsack(self, W, items):
    sort(items.begin(), items.end(), [](Item a, Item b) :
    return a.ratio > b.ratio
    )
    double totalValue = 0.0
    remainingWeight = W
    for item in items:
        if remainingWeight >= item.weight:
            totalValue += item.value
            remainingWeight -= item.weight
             else :
            totalValue += item.value  ((double)remainingWeight / item.weight)
            break
    return totalValue

```

## Greedy on Arrays

**When to use:** Look for "jump game", "maximum subarray", "best time to buy/sell", or any problem where you scan an array and maintain a running best/state — local decisions at each index build up to the global answer.

Greedy choices on array elements, often with two pointers or sliding window.

```python
# Maximum Subarray (Kadane's Algorithm)
def maxSubArray(self, nums):
    maxSum = nums[0]
    currentSum = nums[0]
    for(i = 1 i < len(nums) i += 1) :
    currentSum = max(nums[i], currentSum + nums[i])
    maxSum = max(maxSum, currentSum)
return maxSum
# Best Time to Buy and Sell Stock II
def maxProfit(self, prices):
    profit = 0
    for(i = 1 i < len(prices) i += 1) :
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i-1]
return profit
# Candy - Greedy with sequence tracking
def candy(self, ratings):
    N = len(ratings)
    rtn = 1
    inc = 1, dec = 0, pre = 1
    for(i = 1 i < N i += 1) :
    if ratings[i] >= ratings[i - 1]:
        dec = 0
        (1 if             pre = ratings[i] == ratings[i - 1] * else pre + 1)
        rtn += pre
        inc = pre
         else :
        dec += 1
        if dec == inc:
            dec += 1
        rtn += dec
        pre = 1
return rtn
# Wiggle Subsequence - Greedy with difference tracking
def wiggleMaxLength(self, nums):
    N = len(nums)
    if(N < 2) return N
    prevDiff = nums[1] - nums[0]
    (2 if     rtn = prevDiff != 0 else 1)
    for(i = 2 i < N i += 1) :
    diff = nums[i] - nums[i - 1]
    if((diff > 0  and  prevDiff <= 0)  or
    diff < 0  and  prevDiff >= 0) :
    rtn += 1
    prevDiff = diff
return rtn

```

## Greedy on Strings

**When to use:** The problem says "smallest subsequence", "remove duplicate letters", "minimum swaps", or involves character frequency / ordering decisions — often solved with a stack-based greedy approach.

Greedy choices when processing strings, often with character frequency or ordering.

```python
# Is Subsequence
def isSubsequence(self, s, t):
    i = 0, j = 0
    while i < s.length()  and  j < t.length():
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == s.length()
# Minimum Swaps to Make Strings Equal - Mismatch pairing
def minimumSwap(self, s1, s2):
    xy = 0, yx = 0
    for(i = 0 i < (int) s1.length() i += 1) :
    if s1[i] == 'x'  and  s2[i] == 'y':
        xy += 1
         else if(s1[i] == 'y'  and  s2[i] == 'x') :
        yx += 1
if (xy + yx) % 2 == 1:
    return -1  # Impossible if odd total mismatches
return xy / 2 + yx / 2 + xy % 2 + yx % 2
# Construct K Palindrome Strings - Frequency-based greedy
def canConstruct(self, s, k):
    right = s.length()
    occ[26] = :0
for ch in s:
    occ[ch - 'a']++
left = 0
for(i = 0 i < 26 i += 1) :
if occ[i] % 2 == 1:
    left += 1
left = max(left, 1)
return left <= k  and  k <= right

```

## Greedy with Sorting

**When to use:** The problem says "assign cookies", "queue reconstruction", "two city scheduling", or any scenario where sorting by one dimension (size, cost difference, height) unlocks a simple greedy scan.

Many greedy problems require sorting first to make optimal choices.

```python
# Assign Cookies
def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    i = 0, j = 0
    count = 0
    while i < len(g)  and  j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
        j += 1
    return count
# Array Partition - Maximize sum of minimums
def arrayPairSum(self, nums):
    nums.sort()
    sum = 0
    for(i = 0 i < (int)len(nums) i += 2) :
    sum += nums[i]
return sum
# Maximum Units on a Truck - Fractional knapsack style
def maximumUnits(self, boxTypes, truckSize):
    sort(boxTypes.begin(), boxTypes.end(), [](u, v):
    return u[1] > v[1]  # Sort by units per box (descending)
    )
    remainSize = truckSize
    maximumUnits = 0
    for boxType in boxTypes:
        if(remainSize == 0) break
        cnt = min(remainSize, boxType[0])
        maximumUnits += cnt  boxType[1]
        remainSize -= cnt
    return maximumUnits
# Minimum Cost to Move Chips - Parity-based greedy
def minCostToMoveChips(self, position):
    even = 0, odd = 0
    for pos in position:
        if pos % 2 == 0:
            odd += 1  # Count even positions
             else :
            even += 1  # Count odd positions
    return min(odd, even)  # Move minority parity to majority
# Two City Scheduling - Sort by cost difference
def twoCitySchedCost(self, costs):
    sort(costs.begin(), costs.end(), [](u, autov) :
    return (u[0] - u[1] < v[0] - v[1])
    )
    total = 0
    N = len(costs) / 2
    for(i = 0 i < N i += 1) :
    total += costs[i][0] + costs[i + N][1]
return total
# Find Valid Matrix Given Row and Column Sums - Greedy two pointers
def restoreMatrix(self, rowSum, colSum):
    N = len(rowSum), M = len(colSum)
    list[list[int>> matrix(N, list[int>(M, 0))
    i = 0, j = 0
    while i < N  and  j < M:
        v = min(rowSum[i], colSum[j])
        matrix[i][j] = v
        rowSum[i] -= v
        colSum[j] -= v
        if(rowSum[i] == 0) i += 1
        if(colSum[j] == 0) j += 1
    return matrix
# Queue Reconstruction by Height
def reconstructQueue(self, people):
    sort(people.begin(), people.end(), [](list[int> a, list[int> b) :
    (a[1] < b[1] if         return a[0] == b[0] * else a[0] > b[0])
    )
    list[list[int>> result
    for person in people:
        result.insert(result.begin() + person[1], person)
    return result

```

## Easy Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 455 | Assign Cookies | [Link](https://leetcode.com/problems/assign-cookies/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/easy-455-assign-cookies/) |
| 860 | Lemonade Change | [Link](https://leetcode.com/problems/lemonade-change/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/easy-860-lemonade-change/) |
| 392 | Is Subsequence | [Link](https://leetcode.com/problems/is-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/easy-392-is-subsequence/) |
| 406 | Queue Reconstruction by Height | [Link](https://leetcode.com/problems/queue-reconstruction-by-height/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/19/medium-406-queue-reconstruction-by-height/) |
| 53 | Maximum Subarray | [Link](https://leetcode.com/problems/maximum-subarray/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-53-maximum-subarray/) |
| 435 | Non-overlapping Intervals | [Link](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/medium-435-non-overlapping-intervals/) |
| 452 | Minimum Number of Arrows to Burst Balloons | [Link](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/medium-452-minimum-number-of-arrows-to-burst-balloons/) |
| 561 | Array Partition | [Link](https://leetcode.com/problems/array-partition/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/easy-561-array-partition/) |
| 1029 | Two City Scheduling | [Link](https://leetcode.com/problems/two-city-scheduling/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-1029-two-city-scheduling/) |
| 122 | Best Time to Buy and Sell Stock II | [Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/medium-122-best-time-to-buy-and-sell-stock-ii/) |
| 1710 | Maximum Units on a Truck | [Link](https://leetcode.com/problems/maximum-units-on-a-truck/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/easy-1710-maximum-units-on-a-truck/) |
| 1217 | Minimum Cost to Move Chips to The Same Position | [Link](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/easy-1217-minimum-cost-to-move-chips-to-the-same-position/) |

## Medium Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 763 | Partition Labels | [Link](https://leetcode.com/problems/partition-labels/) | - |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 435 | Non-overlapping Intervals | [Link](https://leetcode.com/problems/non-overlapping-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/medium-435-non-overlapping-intervals/) |
| 55 | Jump Game | [Link](https://leetcode.com/problems/jump-game/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/03/medium-55-jump-game/) |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-22-medium-1094-car-pooling/) |
| 45 | Jump Game II | [Link](https://leetcode.com/problems/jump-game-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-medium-45-jump-game-ii/) |
| 134 | Gas Station | [Link](https://leetcode.com/problems/gas-station/) | - |
| 1024 | Video Stitching | [Link](https://leetcode.com/problems/video-stitching/) | - |
| 1247 | Minimum Swaps to Make Strings Equal | [Link](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-1247-minimum-swaps-to-make-strings-equal/) |
| 1400 | Construct K Palindrome Strings | [Link](https://leetcode.com/problems/construct-k-palindrome-strings/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-1400-construct-k-palindrome-strings/) |
| 1605 | Find Valid Matrix Given Row and Column Sums | [Link](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-1605-find-valid-matrix-given-row-and-column-sums/) |
| 376 | Wiggle Subsequence | [Link](https://leetcode.com/problems/wiggle-subsequence/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/medium-376-wiggle-subsequence/) |
| 274 | H-Index | [Link](https://leetcode.com/problems/h-index/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/17/medium-274-h-index/) |

## Hard Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 135 | Candy | [Link](https://leetcode.com/problems/candy/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/04/hard-135-candy/) |
| 871 | Minimum Number of Refueling Stops | [Link](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | - |
| 818 | Race Car | [Link](https://leetcode.com/problems/race-car/) | - |
| 410 | Split Array Largest Sum | [Link](https://leetcode.com/problems/split-array-largest-sum/) | - |
| 420 | Strong Password Checker | [Link](https://leetcode.com/problems/strong-password-checker/) | - |
| 68 | Text Justification | [Link](https://leetcode.com/problems/text-justification/) | - |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 1799 | Maximize Score After N Operations | [Link](https://leetcode.com/problems/maximize-score-after-n-operations/) | - |

## Common Greedy Patterns

### 1. Interval Problems
- Sort by end time
- Always pick the interval that ends earliest
- Examples: Non-overlapping Intervals, Minimum Arrows to Burst Balloons

### 2. Two Pointers
- Use two pointers to make greedy choices
- Examples: Is Subsequence, Assign Cookies

### 3. Sorting + Greedy
- Sort first, then apply greedy strategy
- Examples: Queue Reconstruction by Height, Two City Scheduling

### 4. Local Optimization
- Make best local choice at each step
- Examples: Best Time to Buy and Sell Stock II, Maximum Subarray

### 5. Jump Problems
- Greedy choice: jump as far as possible
- Examples: Jump Game, Jump Game II

### 6. Scheduling Problems
- Sort and schedule optimally
- Examples: Task Scheduler, Car Pooling

## Key Insights

1. **When to use Greedy**: 
   - Problem has optimal substructure
   - Greedy choice property holds
   - No need to reconsider previous choices

2. **Common Mistakes**:
   - Not sorting when needed
   - Wrong sorting criteria
   - Not considering edge cases
   - Assuming greedy always works (need to prove correctness)

3. **Proving Greedy Correctness**:
   - Show greedy choice property
   - Show optimal substructure
   - Use exchange argument or contradiction

## Related Topics

- Dynamic Programming (when greedy doesn't work)
- Sorting Algorithms
- Interval Problems
- Two Pointers
- Sliding Window

## References

- [Mastering Greedy Algorithms with LeetCode](https://leetcode.com/discuss/post/5330283/mastering-greedy-algorithms-with-leetcod-d0dq/) - Comprehensive guide to greedy algorithms with LeetCode problems

## Pattern Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Interval Scheduling | "non-overlapping", "minimum rooms" | Sort by end time, pick earliest |
| Activity Selection | "maximum activities", "schedule" | Sort by end, greedily select |
| Greedy on Arrays | "jump game", "max subarray" | Local decisions, running state |
| Greedy on Strings | "smallest subsequence", "remove duplicates" | Stack-based greedy |
| Greedy + Sorting | "assign cookies", "queue reconstruction" | Sort first, then greedily assign |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **DP (when greedy doesn't apply):** [Dynamic Programming](/posts/2025-10-29-leetcode-templates-dp/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

{% endraw %}

