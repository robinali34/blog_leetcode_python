---
layout: post
title: "309. Best Time to Buy and Sell Stock with Cooldown"
date: 2026-03-20 00:00:00 -0700
categories: [leetcode, medium, dp, stock]
tags: [leetcode, medium, dynamic-programming, cooldown]
permalink: /2026/03/20/medium-309-best-time-to-buy-and-sell-stock-with-cooldown/
---

# 309. Best Time to Buy and Sell Stock with Cooldown

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on the `ith` day.

Find the **maximum profit** you can achieve with the following rules:

- You may complete as many transactions as you like (buy one stock, then sell it).
- After you sell your stock, you cannot buy stock on the **next day** (cooldown one day).
- You may not hold multiple stocks at the same time (must sell before buying again).

## Examples

**Example 1:**

```python
Input: prices = [1,2,3,0,2]
Output: 3
# Transactions: buy(1) -> sell(2), cooldown, buy(0) -> sell(2)
```

**Example 2:**

```python
Input: prices = [1]
Output: 0
```

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Clarification Questions

1. **Cooldown definition**: After selling on day `i`, buying is not allowed on day `i+1`?  
   **Assumption**: Yes.
2. **Multiple transactions**: You can buy/sell multiple times as long as cooldown and “one stock at a time” are respected.  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: State view (5 min)**  
On each day, your situation is one of:

- `hold`: you currently hold a stock.
- `sold`: you sold today (so tomorrow is cooldown).
- `rest`: you do not hold a stock and you are free to buy today.

We want the maximum profit over time respecting transitions.

**Step 2: Naive baseline (5 min)**  
Try all sequences of buy/sell days (backtracking). This branches heavily and is exponential.

**Step 3: Bottleneck**  
The same “day, best profit with certain state” gets recomputed for many choices.

**Step 4: Optimization with DP (10 min)**  
Use DP with constant states updated day-by-day.

## Solution Approach

This is a classic DP-by-state-machine:

Let:

- `hold`: max profit after day `i` if we are holding a stock.
- `sold`: max profit after day `i` if we just sold (entering cooldown tomorrow).
- `rest`: max profit after day `i` if we are resting (not holding, not selling today).

Transitions (from day `i-1` to day `i`):

- `hold = max(prev_hold, prev_rest - prices[i])`
  - keep holding, or
  - buy today from a rested state
- `sold = prev_hold + prices[i]`
  - sell today if we were holding yesterday
- `rest = max(prev_rest, prev_sold)`
  - stay at rest, or
  - cooldown ends (move from sold to rest)

Answer is `max(sold, rest)` (cannot end holding a stock for realized profit).

## Key Insights

1. **Cool-down is captured by state** — after `sold`, the next day cannot buy because transitions only allow buy from `rest`.
2. **Only 3 states** — keeps DP compact and O(1) space.
3. **Day-by-day update** — each day depends only on previous day states.

## Python Solution

### DP with (hold, sold, rest)

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initial day (day 0):
        # - hold: buy on day 0 => -prices[0]
        # - sold: impossible on day 0 => 0
        # - rest: do nothing => 0
        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, len(prices)):
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)
```

### Alternative DP phrasing (explicit arrays)

You can also write:

- `dp_hold[i]`, `dp_sold[i]`, `dp_rest[i]`

but it uses O(n) space; the optimized solution above is equivalent.

## Algorithm Explanation

We iterate through days, updating the maximum profit for each state. The cooldown constraint is enforced by only allowing buy transitions from `rest` (not from `sold`).

## Complexity Analysis

- **Time**: O(n)
- **Space**: O(1)

## Edge Cases

- `len(prices) == 1` → profit is 0.
- Monotonically decreasing prices → never profitable → 0.
- Prices with frequent spikes → DP captures the best tradeoff around cooldown days.

## Common Mistakes

- Buying immediately after selling: make sure the transition to `hold` uses `rest`, not `sold`.
- Returning `hold` as the answer: realized profit must be from `sold` or `rest`.

## Related Problems

- [LC 121: Best Time to Buy and Sell Stock](/2026/03/20/medium-121-best-time-to-buy-and-sell-stock/)
- [LC 122: Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [LC 123: Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

