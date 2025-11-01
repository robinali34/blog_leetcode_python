---
layout: post
title: "LC 1249: Minimum Remove to Make Valid Parentheses"
date: 2025-10-22 13:30:00 -0700
categories: leetcode medium string stack
permalink: /posts/2025-10-22-medium-1249-minimum-remove-to-make-valid-parentheses/
tags: [leetcode, medium, string, stack, parentheses, validation]
---

# LC 1249: Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium  
**Category:** String, Stack  
**Companies:** Amazon, Facebook, Microsoft, Google

## Problem Statement

Given a string `s` of `'('`, `')'` and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

### Examples

**Example 1:**
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

**Example 2:**
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3:**
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

### Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('`, `')'`, or lowercase English letter.

## Solution Approaches

### Approach 1: Stack-Based Validation (Recommended)

**Key Insight:** Use a stack to track unmatched parentheses and remove them from the string.

**Algorithm:**
1. Use stack to track indices of unmatched parentheses
2. For each character, push `'('` indices and pop for matching `')'`
3. Remove all indices remaining in stack (unmatched parentheses)
4. Return the modified string

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(idx)
        result = list(s)
        while stack:
            result[stack.pop()] = ''
        return ''.join(result)
```

### Approach 2: Two-Pass String Building

**Algorithm:**
1. First pass: Remove unmatched `')'` by tracking balance
2. Second pass: Remove unmatched `'('` by tracking balance in reverse
3. Build result string

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: remove unmatched ')'
        result = ""
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
                result += c
            elif c == ')':
                if balance > 0:
                    balance -= 1
                    result += c
                # Skip unmatched ')'
            else:
                result += c
        
        # Second pass: remove unmatched '('
        final_result = ""
        balance = 0
        for i in range(len(result) - 1, -1, -1):
            c = result[i]
            if c == ')':
                balance += 1
                final_result = c + final_result
            elif c == '(':
                if balance > 0:
                    balance -= 1
                    final_result = c + final_result
                # Skip unmatched '('
            else:
                final_result = c + final_result
        
        return final_result
```

### Approach 3: Set-Based Tracking

**Algorithm:**
1. Use two passes to identify invalid parentheses
2. Use a set to track indices to remove
3. Build result string excluding tracked indices

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stk = []
        
        # Find unmatched parentheses
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                if not stk:
                    to_remove.add(i)
                else:
                    stk.pop()
        
        # Add remaining unmatched '(' to removal set
        while stk:
            to_remove.add(stk.pop())
        
        # Build result string
        result = ""
        for i in range(len(s)):
            if i not in to_remove:
                result += s[i]
        
        return result
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Stack-Based | O(n) | O(n) | Simple, intuitive | String erasure overhead |
| Two-Pass | O(n) | O(n) | No string modification | More complex logic |
| Set-Based | O(n) | O(n) | Clear separation of concerns | Extra space for set |

### Key Insights

1. **Stack Validation**: Use stack to track parentheses matching
2. **Index Tracking**: Store indices instead of characters for removal
3. **Two-Pass Strategy**: Handle unmatched parentheses in both directions
4. **Minimal Removal**: Remove only the minimum required parentheses

## Implementation Details

### Stack-Based Approach
```python
// Track indices of unmatched parentheses
if(s[idx] == '(') stk.push(idx);
if(s[idx] == ')') {
    if(!stknot   s[stk.top()] == '(') {
        stk.pop();  // Match found
    } else {
        stk.push(idx);  // Unmatched ')'
    }
}
```

### String Modification
```python
# Remove unmatched parentheses from string
result = list(s)
while stk:
    result[stk.pop()] = ''
result = ''.join(result)
```

## Edge Cases

1. **Empty String**: `""` → `""`
2. **No Parentheses**: `"abc"` → `"abc"`
3. **All Unmatched**: `"))(("` → `""`
4. **Nested Valid**: `"(a(b)c)"` → `"(a(b)c)"`
5. **Mixed Characters**: `"a)b(c)d"` → `"ab(c)d"`

## Follow-up Questions

- What if you needed to return all possible valid strings?
- How would you handle multiple types of brackets?
- What if you needed to minimize the number of removals?
- How would you optimize for very large strings?

## Related Problems

- [LC 20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [LC 22: Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [LC 301: Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)

## Optimization Techniques

1. **Stack Index Tracking**: Store indices instead of characters
2. **Single Pass**: Use stack to identify all unmatched parentheses
3. **String Building**: Avoid multiple string modifications
4. **Memory Efficiency**: Use minimal extra space

## Code Quality Notes

1. **Readability**: Stack approach is most intuitive
2. **Performance**: All approaches have O(n) time complexity
3. **Space Efficiency**: O(n) space for stack/set storage
4. **Robustness**: Handles all edge cases correctly

---

*This problem demonstrates the power of stack-based validation for parentheses matching and shows how to efficiently remove invalid characters while preserving valid structure.*
