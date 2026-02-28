---
layout: post
title: "[Medium] 316. Remove Duplicate Letters"
date: 2025-10-17 22:23:33 -0700
categories: python stack monotonic-stack greedy problem-solving
---

# [Medium] 316. Remove Duplicate Letters

Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the **smallest in lexicographical order** among all possible results.

## Examples

**Example 1:**
```
Input: s = "bcabc"
Output: "abc"
Explanation: 
- Remove duplicate 'b' and 'c'
- Result "abc" is lexicographically smallest
```

**Example 2:**
```
Input: s = "cbacdcbc"
Output: "acdb"
Explanation: 
- Remove duplicate 'c' and 'b'
- Result "acdb" is lexicographically smallest
```

**Example 3:**
```
Input: s = "bbcaac"
Output: "bac"
Explanation: 
- Remove duplicate 'b' and 'c'
- Result "bac" is lexicographically smallest
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters only.

## Solution: Monotonic Stack with Greedy Approach

**Time Complexity:** O(n) where n is the length of string  
**Space Complexity:** O(1) since we use at most 26 characters

Use a monotonic stack to maintain lexicographically smallest result while ensuring each character appears exactly once.

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = [0] * 26
        visited = [False] * 26
        stack = []
        for c in s:
            count[ord(c) - ord('a')] += 1
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] -= 1
                if visited[idx]:
                    continue
                    while stack and stack[-1] > c and count[ord(stack[-1]) - ord('a')] > 0:
                        visited[ord(stack[-1]) - ord('a')] = False
                        stack.pop()
                        stack.append(c)
                        visited[idx] = True
                        return "".join(stack)


```

## How the Algorithm Works

**Key Insight:** Use a monotonic stack to maintain lexicographically smallest result while ensuring each character appears exactly once.

**Steps:**
1. **Count frequency** of each character in the string
2. **Use visited array** to track characters already in result
3. **For each character:**
   - Skip if already processed
   - Remove characters from stack that are:
     - Greater than current character (lexicographically)
     - Will appear again later (count > 0)
4. **Add current character** to stack and mark as visited
5. **Build result** from stack

## Step-by-Step Example

### Example: `s = "cbacdcbc"`

**Initial state:**
- `count = [2,2,2,1]` (a=2, b=2, c=2, d=1)
- `visited = [false,false,false,false]`
- `stack = []`

**Processing each character:**

| Char | Count After | Visited | Stack Operation | Stack State |
|------|-------------|---------|-----------------|-------------|
| 'c' | [2,2,1,1] | [f,f,t,f] | Push 'c' | ['c'] |
| 'b' | [2,1,1,1] | [f,t,t,f] | Push 'b' | ['c','b'] |
| 'a' | [1,1,1,1] | [t,t,t,f] | Pop 'b','c', Push 'a' | ['a'] |
| 'c' | [1,1,0,1] | [t,t,t,f] | Skip (already visited) | ['a'] |
| 'd' | [1,1,0,0] | [t,t,t,t] | Push 'd' | ['a','d'] |
| 'c' | [1,1,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |
| 'b' | [1,0,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |
| 'c' | [0,0,0,0] | [t,t,t,t] | Skip (already visited) | ['a','d'] |

**Final result:** `"acdb"`

## Algorithm Breakdown

### Core Logic:
```python
for c in s:
    count[ord(c) - ord('a')] -= 1
    if visited[ord(c) - ord('a')]:
        continue
        while stack and stack[-1] > c and count[ord(stack[-1]) - ord('a')] > 0:
            visited[ord(stack[-1]) - ord('a')] = False
            stack.pop()
            stack.append(c)
            visited[ord(c) - ord('a')] = True




```

**Process:**
1. **Decrement count** for current character
2. **Skip if already processed** (visited)
3. **Remove larger characters** that will appear again
4. **Add current character** to stack
5. **Mark as visited**

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Count frequency | O(n) | O(1) |
| Process characters | O(n) | O(1) |
| Stack operations | O(n) | O(1) |
| Build result | O(n) | O(1) |
| **Total** | **O(n)** | **O(1)** |

Where n is the length of the string.

## Edge Cases

1. **Single character:** `s = "a"` → `"a"`
2. **All same characters:** `s = "aaaa"` → `"a"`
3. **Already sorted:** `s = "abc"` → `"abc"`
4. **Reverse sorted:** `s = "cba"` → `"abc"`

## Key Insights

### Greedy Strategy:
1. **Lexicographically smallest:** Always prefer smaller characters
2. **One occurrence:** Each character appears exactly once
3. **Future availability:** Consider if character will appear again
4. **Stack property:** Maintains order and allows efficient removal

### Monotonic Stack:
1. **Maintains order:** Characters in lexicographical order
2. **Efficient removal:** Can remove multiple characters at once
3. **Future consideration:** Checks if characters will appear again
4. **Optimal result:** Ensures smallest lexicographical order

## Detailed Example Walkthrough

### Example: `s = "bcabc"`

**Initial state:**
- `count = [1,2,2]` (a=1, b=2, c=2)
- `visited = [false,false,false]`
- `stack = []`

**Processing each character:**

| Char | Count After | Visited | Stack Operation | Stack State | Explanation |
|------|-------------|---------|-----------------|-------------|-------------|
| 'b' | [1,1,2] | [f,t,f] | Push 'b' | ['b'] | First 'b', add to stack |
| 'c' | [1,1,1] | [f,t,t] | Push 'c' | ['b','c'] | First 'c', add to stack |
| 'a' | [0,1,1] | [t,t,t] | Pop 'c','b', Push 'a' | ['a'] | 'a' < 'c','b', and 'c','b' will appear again |
| 'b' | [0,0,1] | [t,t,t] | Skip (already visited) | ['a'] | 'b' already in result |
| 'c' | [0,0,0] | [t,t,t] | Skip (already visited) | ['a'] | 'c' already in result |

**Final result:** `"abc"`

## Alternative Approaches

### Approach 1: Recursive with Backtracking
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                pos = 0
                for i, ch in enumerate(s):
                    if ch < s[pos]:
                        pos = i
                        count[ord(ch) - ord('a')] -= 1
                        if count[ord(ch) - ord('a')] == 0:
                            break
                            first = s[pos]
                            remaining = s[pos + 1:].replace(first, "")
                            return first + self.removeDuplicateLetters(remaining)


```

**Time Complexity:** O(n^2)  
**Space Complexity:** O(n)

### Approach 2: Set-based Approach
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        result = []
        for c in s:
            if c not in seen:
                seen.add(c)
                result.append(c)
                result.sort()
                return "".join(result)


```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

## Common Mistakes

1. **Wrong removal condition:** Not checking if character will appear again
2. **Missing visited check:** Processing same character multiple times
3. **Incorrect stack order:** Not maintaining lexicographical order
4. **Count management:** Not properly decrementing counts

## Related Problems

- [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
- [321. Create Maximum Number](https://leetcode.com/problems/create-maximum-number/)
- [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)
- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

## Why This Solution Works

### Greedy Strategy:
1. **Lexicographically smallest:** Always prefer smaller characters
2. **One occurrence:** Each character appears exactly once
3. **Future availability:** Consider if character will appear again
4. **Optimal choice:** Make locally optimal choice at each step

### Monotonic Stack:
1. **Maintains order:** Characters in lexicographical order
2. **Efficient removal:** Can remove multiple characters at once
3. **Future consideration:** Checks if characters will appear again
4. **Optimal result:** Ensures smallest lexicographical order

### Key Algorithm Properties:
1. **Correctness:** Always produces valid result
2. **Optimality:** Produces lexicographically smallest result
3. **Efficiency:** O(n) time complexity
4. **Simplicity:** Easy to understand and implement
