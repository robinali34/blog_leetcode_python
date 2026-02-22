---
layout: post
title: "LeetCode 416. Partition Equal Subset Sum"
date: 2026-02-11
categories: [leetcode, medium, dynamic-programming]
tags: [leetcode, medium, dp, knapsack]
permalink: /2026/02/11/medium-416-partition-equal-subset-sum/
---

Given an integer array `nums`, return `true` *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or* `false` *otherwise*.

## Examples

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Approach

This problem is a classic variation of the **0/1 Knapsack Problem**. 

1.  **Total Sum Check**: First, calculate the sum of all elements. If the total sum is odd, it's impossible to split it into two equal integer partitions, so return `false`.
2.  **Target Sum**: If the total sum is even, our goal is to find a subset of elements that sums up to `target = totalSum / 2`. If we find such a subset, the remaining elements will automatically sum to `target` as well.
3.  **Transformation**: The problem becomes: "Can we pick a subset of items from `nums` such that their sum is exactly `target`?"

### 1. Brute Force (DFS)

We can try to include or exclude each element recursively.
- **Base Case**: If `target == 0`, we found a subset. If `target < 0` or we run out of elements, return `false`.
- **Recursive Step**: For index `i`, we can either:
    - Include `nums[i]` in the sum (subtract from target).
    - Exclude `nums[i]` (keep target same).

Time Complexity: $O(2^n)$ - TLE.

### 2. Top-Down DP (Memoization)

The brute force approach re-calculates the same state `(index, currentTarget)` multiple times. We can cache these results.
Note: Using `vector<vector<int>>` (with -1 for unvisited) is preferred over `vector<vector<bool>>` to distinguish between "visited and false" vs "unvisited".

Time Complexity: $O(n \cdot \text{target})$
Space Complexity: $O(n \cdot \text{target})$

### 3. Bottom-Up DP (2D)

We can build a table `dp[i][j]` representing whether sum `j` is possible using the first `i` items.
- `dp[i][j] = dp[i-1][j]` (don't include item `i`) `|| dp[i-1][j - nums[i-1]]` (include item `i`).

### 4. Space Optimized DP (1D)

Notice that `dp[i][j]` only depends on the previous row `dp[i-1]`. We can reduce the space to a 1D array.
When iterating through the 1D array, we must iterate **backwards** from `target` to `nums[i]`. This ensures that when we calculate `dp[j]`, we are using values from the *previous* iteration (effectively `dp[i-1]`), not values we just updated in the *current* iteration.

Time Complexity: $O(n \cdot \text{target})$
Space Complexity: $O(\text{target})$

## Solution

### Approach 1: DFS (Time Limit Exceeded)

{% raw %}
```python
class Solution:
def canPartition(self, nums):
    totalSum = accumulate(nums.begin(), nums.end(), 0)
    if (totalSum % 2 != 0) return False
    subSetSum = totalSum / 2
    return dfs(nums, len(nums) - 1, subSetSum)
def dfs(self, nums, n, subSetSum):
    if (subSetSum == 0) return True
    if (n < 0  or  subSetSum < 0) return False
    return dfs(nums, n - 1, subSetSum - nums[n])  or  dfs(nums, n - 1, subSetSum)
```
{% endraw %}

### Approach 2: DFS with Memoization

{% raw %}
```python
class Solution:
def canPartition(self, nums):
    totalSum = accumulate(nums.begin(), nums.end(), 0)
    if (totalSum % 2 != 0) return False
    subSetSum = totalSum / 2
    n = len(nums)
    // memo[i][j]: -1 unvisited, 0 False, 1 True
    list[list[int>> memo(n, list[int>(subSetSum + 1, -1))
    return dfs(nums, n - 1, subSetSum, memo)
def dfs(self, nums, i, target, memo):
    if (target == 0) return True
    if (i < 0  or  target < 0) return False
    if (memo[i][target] != -1) return memo[i][target]
    bool result = dfs(nums, i - 1, target - nums[i], memo)  or
    dfs(nums, i - 1, target, memo)
    return memo[i][target] = result
```
{% endraw %}

### Approach 3: 2D Dynamic Programming

{% raw %}
```python
class Solution:
def canPartition(self, nums):
    sum = accumulate(nums.begin(), nums.end(), 0)
    if (sum % 2) return False
    subSetSum = sum / 2
    n = len(nums)
    // dp[i][j] means whether sum j is possible using first i items
    list[list[bool>> dp(n + 1, list[bool>(subSetSum + 1, False))
    // Base case: sum 0 is always possible (by choosing nothing)
    for (i = 0 i <= n i += 1) dp[i][0] = True
    for (i = 1 i <= n i += 1) :
    curr = nums[i - 1]
    for (j = 1 j <= subSetSum j += 1) :
    if j < curr:
        dp[i][j] = dp[i - 1][j]
         else :
        dp[i][j] = dp[i - 1][j]  or  dp[i - 1][j - curr]
return dp[n][subSetSum]
```
{% endraw %}

### Approach 4: 1D Dynamic Programming (Space Optimized)

{% raw %}
```python
class Solution:
def canPartition(self, nums):
    sum = accumulate(nums.begin(), nums.end(), 0)
    if (sum % 2) return False
    target = sum / 2
    list[bool> dp(target + 1, False)
    dp[0] = True
    for num in nums:
        // Iterate backwards to avoid using the same element multiple times for the same sum
        for (j = target j >= num j -= 1) :
        dp[j] = dp[j]  or  dp[j - num]
return dp[target]
```
{% endraw %}

## Template Reference

- [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/)
