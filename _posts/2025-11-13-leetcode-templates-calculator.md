---
layout: post
title: "Algorithm Templates: Calculator"
date: 2025-11-13 19:40:15 -0800
categories: leetcode templates calculator expression-evaluation
permalink: /posts/2025-11-13-leetcode-templates-calculator/
tags: [leetcode, templates, calculator, expression-evaluation, stack]
---

Minimal, copy-paste C++ for expression evaluation with +, −, ×, ÷ and parentheses. See also [Stack](/posts/2025-11-13-leetcode-templates-stack/) for RPN and nested expressions.

## Contents

- [Basic Calculator (+, -, parentheses)](#basic-calculator---parentheses)
- [Basic Calculator II (+, -, *, /)](#basic-calculator-ii---)
- [Basic Calculator III (All operators + parentheses)](#basic-calculator-iii-all-operators--parentheses)
- [Common Patterns](#common-patterns)
- [Comparison Table](#comparison-table)

## Basic Calculator (+, -, parentheses)

Handles addition, subtraction, and parentheses. Use stack to save state before entering parentheses.

```python
def calculate(self, s):
    list[int> stk
    result = 0, num = 0, sign = 1
    for c in s:
        if isdigit(c):
            num = num  10 + (c - '0')
        switch(c) :
        case '+':
        result += sign  num
        sign = 1
        num = 0
        break
        case '-':
        result += sign  num
        sign = -1
        num = 0
        break
        case '(':
        stk.push(result)
        stk.push(sign)
        sign = 1
        result = 0
        break
        case ')':
        result += sign  num
        result = stk.top() stk.pop()
        result += stk.top() stk.pop()
        num = 0
        break
return result + (sign  num)

```

**Key Points:**
- Save `result` and `sign` before `(`
- Apply saved `sign` and add to saved `result` after `)`
- Track current `sign` for each number

| ID | Title | Link | Solution |
|---|---|---|---|
| 224 | Basic Calculator | [Link](https://leetcode.com/problems/basic-calculator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-224-basic-calculator/) |

## Basic Calculator II (+, -, *, /)

Handles all four operators without parentheses. Evaluate `*` and `/` immediately, defer `+` and `-`.

```python
def calculate(self, s):
    list[int> stk
    char operation = '+'
    curr = 0
    for(i = 0 i < s.length() i += 1) :
    char ch = s[i]
    if isdigit(ch):
        curr = (curr  10) + (ch - '0')
    if (not isdigit(ch)  and  not isspace(ch))  or  i == s.length() - 1:
        switch(operation) :
        case '+':
        stk.push(curr)
        break
        case '-':
        stk.push(-curr)
        break
        case '':
        stk.top() = curr
        break
        case '/':
        stk.top() /= curr
        break
    operation = ch
    curr = 0
result = 0
while not not stk:
    result += stk.top()
    stk.pop()
return result

```

**Key Points:**
- Evaluate `*` and `/` immediately (high precedence)
- Defer `+` and `-` by pushing to stack
- Sum all stack elements at the end

**Optimized Version (O(1) space):**
```python
def calculate(self, s):
    curr = 0, last = 0, result = 0
    char sign = '+'
    for(i = 0 i < s.length() i += 1) :
    char c = s[i]
    if isdigit(c):
        curr = curr  10 + (c - '0')
    if (not isdigit(c)  and  not isspace(c))  or  i == s.length() - 1:
        if sign == '+'  or  sign == '-':
            result += last
            (curr if                 last = (sign == '+')  else -curr)
             else if(sign == '') :
            last = last  curr
             else if(sign == '/') :
            last = last / curr
        sign = c
        curr = 0
return result + last

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 227 | Basic Calculator II | [Link](https://leetcode.com/problems/basic-calculator-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-227-basic-calculator-ii/) |

## Basic Calculator III (All operators + parentheses)

Combines all operators with parentheses. Use recursion or stack to handle nesting.

```python
class Solution:
    def parseExpr(self, s, idx):
        op = '+'
        stk = []

        while idx < len(s):
            if s[idx].isspace():
                idx += 1
                continue

            num = 0

            if s[idx] == '(':
                idx += 1
                num, idx = self.parseExpr(s, idx)

            elif s[idx].isdigit():
                num, idx = self.parseNum(s, idx)
                idx -= 1

            elif s[idx] == ')':
                break

            else:
                op = s[idx]
                idx += 1
                continue

            if op == '+':
                stk.append(num)
            elif op == '-':
                stk.append(-num)
            elif op == '*':
                stk[-1] = stk[-1] * num
            elif op == '/':
                stk[-1] = stk[-1] // num

            if idx < len(s):
                if idx + 1 < len(s):
                    op = s[idx + 1]

            idx += 1

        result = sum(stk)
        return result, idx

    def parseNum(self, s, idx):
        num = 0

        while idx < len(s) and s[idx].isdigit():
            num = num * 10 + (ord(s[idx]) - ord('0'))
            idx += 1

        return num, idx

    def calculate(self, s):
        idx = 0
        result, _ = self.parseExpr(s, idx)
        return result
```

**Key Points:**
- Recursion naturally handles nested parentheses
- Combine stack approach for operators with recursive approach for parentheses
- Evaluate `*` and `/` immediately, defer `+` and `-`

| ID | Title | Link | Solution |
|---|---|---|---|
| 772 | Basic Calculator III | [Link](https://leetcode.com/problems/basic-calculator-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-hard-772-basic-calculator-iii/) |

## Common Patterns

### 1. Number Building
```python
num = 0
for c in s:
    if isdigit(c):
        num = num  10 + (c - '0')

```

### 2. Sign Tracking
```python
sign = 1  # 1 for positive, -1 for negative
# Apply: result += sign  num


```

### 3. Operator Precedence
```python
# High precedence: evaluate immediately
if op == '*'  or  op == '/':
    # Immediate evaluation
     else :
    # Defer to stack

```

### 4. Parentheses Handling
```python
# Stack approach
if c == '(':
    stk.push(result)
    stk.push(sign)
    result = 0
    sign = 1
     else if(c == ')') :
    result += sign  num
    result = stk.top() stk.pop()
    result += stk.top() stk.pop()
# Recursive approach
if c == '(':
    num = parseExpr(s, idx += 1)

```

## Comparison Table

| Problem | Operators | Parentheses | Approach | Complexity |
|---------|-----------|-------------|----------|------------|
| **224** | `+`, `-` | ✅ | Stack (save state) | O(n) time, O(n) space |
| **227** | `+`, `-`, `*`, `/` | ❌ | Stack or variables | O(n) time, O(n) or O(1) space |
| **772** | `+`, `-`, `*`, `/` | ✅ | Recursion + Stack | O(n) time, O(n) space |

## Key Insights

1. **Operator Precedence**: `*` and `/` have higher precedence than `+` and `-`
2. **Immediate vs Deferred**: High precedence operators are evaluated immediately
3. **Parentheses**: Create nested evaluation contexts - use stack or recursion
4. **Sign Propagation**: Track signs through parentheses using stack
5. **Number Building**: Accumulate digits to form multi-digit numbers

## Related Problems

- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Postfix notation
- [394. Decode String](https://leetcode.com/problems/decode-string/) - Nested structure processing
- [71. Simplify Path](https://leetcode.com/problems/simplify-path/) - Path processing with stack

## Common Mistakes

1. **Forgetting final number**: Not adding `sign * num` at the end
2. **Wrong operator precedence**: Evaluating `+` before `*`
3. **Stack order**: Pushing/popping in wrong order for parentheses
4. **Sign handling**: Not applying saved sign correctly after `)`
5. **Number reset**: Not resetting `num` after processing operators

## More templates

- **Stack (parentheses, RPN, decode string):** [Stack](/posts/2025-11-13-leetcode-templates-stack/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

