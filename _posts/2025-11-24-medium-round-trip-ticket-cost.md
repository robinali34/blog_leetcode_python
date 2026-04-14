---
layout: post
title: "[Medium] Round Trip Ticket Cost Minimization"
date: 2025-11-24 00:00:00 -0800
categories: algorithm medium cpp array optimization problem-solving
permalink: /posts/2025-11-24-medium-round-trip-ticket-cost/
tags: [algorithm, medium, array, optimization, greedy, two-pointers]
---

# [Medium] Round Trip Ticket Cost Minimization

Given two lists representing round trip ticket prices, select the cheapest outbound and return tickets where the return follows the outbound. Implement a function to find the minimum total cost of the trip.

## Problem Statement

You are given two lists of ticket prices:
- `outbound`: List of outbound ticket prices
- `return_trip`: List of return ticket prices

Both lists have the same length `n`, and you must select:
- One outbound ticket at index `i`
- One return ticket at index `j` (can be any index, no ordering constraint)

**Note:** Based on the example, it appears there's no strict ordering constraint between outbound and return ticket indices. The "return follows outbound" likely refers to the logical sequence of the trip rather than array indices.

Find the minimum total cost of such a round trip.

## Requirements

- Write a function `int minimizeRoundTripCost(vector<int>& outbound, vector<int>& returnTrip)`
- Both lists are of length `n`, and the values range from 1 to 1000
- Ensure the selected outbound precedes the return in the trip (index-wise)
- Return the minimum total trip cost

## Examples

**Example 1:**
{% raw %}
```python
# Example 1 (unconstrained pairing: any i with any j)
outbound = [9, 1, 5]
return_trip = [4, 5, 3]
# Best sum: 1 + 3 = 4  (outbound[1] + return_trip[2])
# If you require return index before outbound index, the story changes — see j > i below.

```
{% endraw %}

**Example 2:**
{% raw %}
```python
# Example 2 sketch — compare unconstrained vs j >= i vs j > i on paper
outbound = [3, 2, 1]
return_trip = [1, 2, 3]

```
{% endraw %}

## Constraints

- `1 <= n <= 10^5`
- `1 <= outbound[i], return_trip[i] <= 1000`
- Both lists have the same length `n`

## Solution: Find Minimum Return Price

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Since we can pair any outbound ticket with any return ticket, we simply need to find:
1. The minimum return ticket price overall
2. For each outbound ticket, calculate the sum with the minimum return price
3. Return the minimum of all such sums

Alternatively, we can find the minimum outbound price and minimum return price separately, but we need to be careful - the optimal solution might pair a specific outbound with a specific return that isn't the global minimum.

### Solution 1: Brute Force - Check All Pairs (O(n²))

```python
def minimize_round_trip_all_pairs(outbound: list[int], return_trip: list[int]) -> int:
    n = len(outbound)
    best = 10**9
    for i in range(n):
        for j in range(n):
            best = min(best, outbound[i] + return_trip[j])
    return best

```

### Solution 2: Optimized - Find Minimums Separately (O(n))

```python
def minimize_with_global_min_return(outbound: list[int], return_trip: list[int]) -> int:
    """Unconstrained pairing: best is min(outbound) + min(return_trip)."""
    mr = min(return_trip)
    return min(o + mr for o in outbound)

```

**Why this works:**
- Since we can pair any outbound with any return, the optimal strategy is:
  - Find the minimum return price overall
  - Pair each outbound with this minimum return price
  - Choose the outbound that gives the minimum sum

**Time Complexity:** O(n) - one pass to find min return, one pass through outbound  
**Space Complexity:** O(1)

## How the Algorithm Works

### Key Insight: Precompute Minimum Return Prices

**Problem:** For each outbound ticket at index `i`, we need the minimum return ticket price from indices `i+1` to `n-1`.

**Solution:** Precompute `minReturn[i]` = minimum return price from index `i` to the end.

**Why this works:**
- For outbound[i], we can pair with returnTrip[j] where `j > i`
- The minimum return price available is `minReturn[i+1]`
- Total cost = `outbound[i] + minReturn[i+1]`
- Find minimum over all valid `i`

### Step-by-Step Example: `outbound = {9, 1, 5}, returnTrip = {4, 5, 3}`

```
Step 1: Find minimum return price
  minReturn = min(returnTrip) = min(4, 5, 3) = 3

Step 2: Calculate cost for each outbound paired with minimum return
  i = 0: outbound[0] + minReturn = 9 + 3 = 12
  i = 1: outbound[1] + minReturn = 1 + 3 = 4
  i = 2: outbound[2] + minReturn = 5 + 3 = 8
  
  Minimum: min(12, 4, 8) = 4

Note: The example output is 5 (outbound[1] = 1 + returnTrip[0] = 4), 
but the optimal solution is 4 (outbound[1] = 1 + returnTrip[2] = 3).
The example might be showing a valid but not optimal solution.
```

**Visual Representation:**
{% raw %}
```
outbound:  {9,  1,  5}
            │   │   │
            │   └───┼───> Can pair with return[2] = 3 → cost = 4
            └───────┼───> Can pair with return[1] = 5 or return[2] = 3
                    │    Best: return[2] = 3 → cost = 12
                    └───> No return after index 2

returnTrip: {4,  5,  3}
              │   │   │
              └───┴───┘
              minReturn = {3, 3, 3}
```
{% endraw %}

## Key Insights

1. **Precompute minimums**: Build array of minimum return prices from right to left
2. **Pair optimally**: For each outbound, pair with minimum available return
3. **Boundary handling**: Last outbound ticket cannot pair with any return
4. **Greedy approach**: Always choose minimum return price for each outbound

## Algorithm Breakdown

### Step 1: Precompute Minimum Return Prices

```python
def suffix_min_return(return_trip: list[int]) -> list[int]:
    n = len(return_trip)
    suf = [0] * n
    suf[-1] = return_trip[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = min(return_trip[i], suf[i + 1])
    return suf

```

**Why:**
- Start from the end: `minReturn[n-1] = returnTrip[n-1]`
- For each index `i`, `minReturn[i]` is the minimum return price from `i` to the end
- Build from right to left to reuse previous computations

### Step 2: Find Minimum Cost

```python
def min_cost_j_gt_i(outbound: list[int], return_trip: list[int]) -> int:
    """Require return index j > outbound index i."""
    n = len(outbound)
    if n < 2:
        return 10**9
    suf = [0] * n
    suf[-1] = return_trip[-1]
    for i in range(n - 2, -1, -1):
        suf[i] = min(return_trip[i], suf[i + 1])
    return min(outbound[i] + suf[i + 1] for i in range(n - 1))

```

**Why:**
- For outbound[i], minimum return price available is `minReturn[i]` (includes returnTrip[i] and all after)
- Calculate cost for each valid pairing
- Track minimum cost seen so far

## Alternative Solutions

### Solution 2: O(1) Space Optimization

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Instead of storing the entire `minReturn` array, we can iterate backwards and track the minimum return price seen so far.

```python
def min_cost_j_gt_i_o1_space(outbound: list[int], return_trip: list[int]) -> int:
    n = len(outbound)
    if n < 2:
        return 10**9
    best = 10**9
    s = return_trip[-1]
    for i in range(n - 2, -1, -1):
        best = min(best, outbound[i] + s)
        s = min(return_trip[i], s)
    return best

```

**Pros:**
- O(1) extra space
- Same time complexity
- More memory efficient

**Cons:**
- Slightly less intuitive
- Iterates backwards

### Solution 3: Brute Force (For Comparison)

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

```python
def min_cost_j_gt_i_bruteforce(outbound: list[int], return_trip: list[int]) -> int:
    n = len(outbound)
    best = 10**9
    for i in range(n):
        for j in range(i + 1, n):
            best = min(best, outbound[i] + return_trip[j])
    return best

```

**Pros:**
- Simple and straightforward
- Easy to understand

**Cons:**
- O(n²) time complexity
- Inefficient for large inputs

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Precompute Array** | O(n) | O(n) | Clear logic, easy to understand | Extra space |
| **O(1) Space** | O(n) | O(1) | Memory efficient | Backwards iteration |
| **Brute Force** | O(n²) | O(1) | Simple | Too slow |

## Edge Cases

1. **Single ticket**: `n = 1` → No valid pairing, return infinity or handle appropriately
2. **Two tickets**: `n = 2` → Only one possible pairing
3. **All same prices**: Algorithm still works correctly
4. **Decreasing return prices**: Optimal to choose later return tickets
5. **Increasing return prices**: Optimal to choose earlier return tickets

## Implementation Details

### Why Iterate Backwards?

**For O(1) space solution:**
- We need minimum return price from `i+1` to `n-1`
- By iterating backwards, we can maintain `min_return_price` as we go
- At each step, we've seen all return prices from current position to the end

### Why Precompute Array?

**For O(n) space solution:**
- More intuitive: build array of minimums first
- Then use it to calculate costs
- Easier to understand and debug

### Handling Edge Cases

```python
if len(outbound) < 2:
    pass  # no pair with j > i

```

**Why:** Need at least 2 tickets (one outbound, one return) for a valid round trip.

## Common Mistakes

1. **Wrong index constraint**: Using `j >= i` instead of `j > i` (or vice versa)
2. **Missing boundary check**: Not handling case when `n < 2`
3. **Wrong minimum calculation**: Not correctly computing minimum return prices
4. **Index out of bounds**: Accessing `min_return[i+1]` when `i = n-1`
5. **Not iterating backwards**: Trying to compute minimums from left to right

## Optimization Tips

1. **Use O(1) space solution**: If memory is a concern
2. **Early termination**: Not applicable here (need to check all pairs)
3. **Precompute once**: Build min_return array once, use multiple times if needed

## Related Problems

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Similar pattern of finding min/max with ordering constraint
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Multiple transactions
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) - At most two transactions
- Array problems with ordering constraints

## Real-World Applications

1. **Travel Planning**: Finding cheapest round trip flights
2. **Resource Scheduling**: Optimizing resource allocation with time constraints
3. **Cost Optimization**: Minimizing costs with ordering requirements
4. **Pairing Problems**: Finding optimal pairs with constraints

## Pattern Recognition

This problem demonstrates the **"Precompute Minimums/Maximums"** pattern:

```
1. Identify that we need min/max of a subarray
2. Precompute min/max array from one direction
3. Use precomputed values to solve the problem efficiently
```

Similar problems:
- Stock buying/selling problems
- Array range queries
- Optimization with constraints

## Step-by-Step Trace: `outbound = {3, 2, 1}, returnTrip = {1, 2, 3}`

{% raw %}
```
Step 1: Precompute minReturn
  minReturn[2] = returnTrip[2] = 3
  minReturn[1] = min(returnTrip[1], minReturn[2]) = min(2, 3) = 2
  minReturn[0] = min(returnTrip[0], minReturn[1]) = min(1, 2) = 1
  
  minReturn = {1, 2, 3}

Step 2: Calculate costs
  i = 0: outbound[0] + minReturn[1] = 3 + 2 = 5
  i = 1: outbound[1] + minReturn[2] = 2 + 3 = 5
  
  Minimum: min(5, 5) = 5
```
{% endraw %}

## Why This Solution Works

**Optimal Substructure:**
- For each outbound ticket, the optimal return ticket is the minimum available
- We can compute this independently for each outbound ticket
- The overall minimum is the minimum of all optimal pairings

**Greedy Choice:**
- For each outbound ticket, always choose the minimum return ticket available
- This local optimal choice leads to global optimum

**Time Efficiency:**
- Precomputation: O(n) time
- Finding minimum: O(n) time
- Total: O(n) time, much better than O(n²) brute force

## Test Cases

Here are several test cases to verify the solution:

### Test Case 1
{% raw %}
```python
outbound = [9, 1, 5]
return_trip = [4, 5, 3]
# unconstrained min sum: min(o + min(return_trip)) = 1 + 3 = 4

```
{% endraw %}

### Test Case 2
{% raw %}
```python
outbound = [5, 7, 10]
return_trip = [20, 9, 1]
# min sum: 5 + 1 = 6

```
{% endraw %}

### Test Case 3
{% raw %}
```python
outbound = [1, 100, 200]
return_trip = [1000, 400, 2]
# min sum: 1 + 2 = 3

```
{% endraw %}

### Test Case 4
{% raw %}
```python
outbound = [8, 4, 2]
return_trip = [5, 3, 6]
# min sum: 2 + 3 = 5

```
{% endraw %}

### Test Case 5
{% raw %}
```python
outbound = [1, 2, 3]
return_trip = [10, 9, 8]
# min sum: 1 + 8 = 9

```
{% endraw %}

### Test Case Verification Code

{% raw %}
```python
def minimize_unconstrained(outbound: list[int], return_trip: list[int]) -> int:
    mr = min(return_trip)
    return min(o + mr for o in outbound)


TESTS = [
    ([9, 1, 5], [4, 5, 3], 4),
    ([5, 7, 10], [20, 9, 1], 6),
    ([1, 100, 200], [1000, 400, 2], 3),
    ([8, 4, 2], [5, 3, 6], 5),
    ([1, 2, 3], [10, 9, 8], 9),
]
for ob, rt, exp in TESTS:
    assert minimize_unconstrained(ob, rt) == exp

```
{% endraw %}

---

*This problem demonstrates how precomputing minimums can optimize array problems with ordering constraints, reducing time complexity from O(n²) to O(n).*

