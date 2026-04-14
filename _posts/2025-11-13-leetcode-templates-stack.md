---
layout: post
title: "Algorithm Templates: Stack"
date: 2025-11-13 19:40:15 -0800
categories: leetcode templates stack data-structures
permalink: /posts/2025-11-13-leetcode-templates-stack/
tags: [leetcode, templates, stack, data-structures]
---

Minimal, copy-paste C++ for parentheses matching, expression evaluation, nested structures, and monotonic stack.

## Contents

- [Parentheses Matching](#parentheses-matching)
- [Expression Evaluation](#expression-evaluation)
- [Nested Structure Processing](#nested-structure-processing)
- [Monotonic Stack](#monotonic-stack)
- [Stack for State Management](#stack-for-state-management)
- [Stack Design](#stack-design-minmax-stack)

## Parentheses Matching

Use stack's LIFO property to match opening and closing brackets in reverse order.

```python
def is_valid_parentheses(s: str) -> bool:
    st: list[str] = []
    closing = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "({[":
            st.append(c)
        else:
            if not st or st[-1] != closing[c]:
                return False
            st.pop()
    return not st

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 20 | Valid Parentheses | [Link](https://leetcode.com/problems/valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-easy-20-valid-parentheses/) |
| 921 | Minimum Add to Make Valid Parentheses | [Link](https://leetcode.com/problems/minimum-add-to-make-valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-medium-921-minimum-add-to-make-valid-parentheses/) |
| 1249 | Minimum Remove to Make Valid Parentheses | [Link](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-22-medium-1249-minimum-remove-to-make-valid-parentheses/) |

## Expression Evaluation

Use stack to handle operator precedence and parentheses in mathematical expressions.

```python
def calculate_basic(s: str) -> int:
    stk: list[int] = []
    result = num = 0
    sign = 1
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in "+-":
            result += sign * num
            num = 0
            sign = 1 if c == "+" else -1
        elif c == "(":
            stk.append(result)
            stk.append(sign)
            result = num = 0
            sign = 1
        elif c == ")":
            result += sign * num
            num = 0
            result *= stk.pop()
            result += stk.pop()
    return result + sign * num

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 150 | Evaluate Reverse Polish Notation | [Link](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-150-evaluate-reverse-polish-notation/) |
| 224 | Basic Calculator | [Link](https://leetcode.com/problems/basic-calculator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-224-basic-calculator/) |
| 227 | Basic Calculator II | [Link](https://leetcode.com/problems/basic-calculator-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-medium-227-basic-calculator-ii/) |
| 772 | Basic Calculator III | [Link](https://leetcode.com/problems/basic-calculator-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-13-hard-772-basic-calculator-iii/) |

## Nested Structure Processing

Use stack to process nested structures like strings, expressions, or function calls.

```python
def decode_string(s: str) -> str:
    stack: list = []
    cur = ""
    k = 0
    for c in s:
        if c.isdigit():
            k = k * 10 + int(c)
        elif c == "[":
            stack.append(cur)
            stack.append(k)
            cur, k = "", 0
        elif c == "]":
            repeat = stack.pop()
            prev = stack.pop()
            cur = prev + cur * repeat
        else:
            cur += c
    return cur

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |
| 636 | Exclusive Time of Functions | [Link](https://leetcode.com/problems/exclusive-time-of-functions/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-636-exclusive-time-of-functions/) |
| 71 | Simplify Path | [Link](https://leetcode.com/problems/simplify-path/) | - |

## Monotonic Stack

Maintain a stack with elements in monotonic order (increasing or decreasing) to efficiently find next/previous greater/smaller elements.

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    st: list[int] = []
    for i in range(n):
        while st and nums[st[-1]] < nums[i]:
            result[st.pop()] = nums[i]
        st.append(i)
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 42 | Trapping Rain Water | [Link](https://leetcode.com/problems/trapping-rain-water/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/17/hard-42-trapping-rain-water/) |
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/hard-84-largest-rectangle-in-histogram/) |
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 496 | Next Greater Element I | [Link](https://leetcode.com/problems/next-greater-element-i/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/easy-496-next-greater-element-i/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-503-next-greater-element-ii/) |
| 316 | Remove Duplicate Letters | [Link](https://leetcode.com/problems/remove-duplicate-letters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/17/medium-316-remove-duplicate-letters/) |
| 1944 | Visible People in Queue | [Link](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/09/hard-1944-number-of-visible-people-in-a-queue/) |

## Stack for State Management

Use stack to save and restore state when processing nested or hierarchical structures.

```python
# Example: exclusive time of functions (simplified)
def exclusive_time(n: int, logs: list[str]) -> list[int]:
    res = [0] * n
    st: list[tuple[int, int]] = []  # (func_id, start_time)
    for log in logs:
        parts = log.split(":")
        fid, typ, t = int(parts[0]), parts[1], int(parts[2])
        if typ == "start":
            st.append((fid, t))
        else:
            fid, start = st.pop()
            duration = t - start + 1
            res[fid] += duration
            if st:
                res[st[-1][0]] -= duration
    return res

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 636 | Exclusive Time of Functions | [Link](https://leetcode.com/problems/exclusive-time-of-functions/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-636-exclusive-time-of-functions/) |
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |

## Stack Design (Min/Max Stack)

Maintaining extra information (like minimums or frequencies) alongside the primary stack data.

```python
class MinStack:
    def __init__(self) -> None:
        self.stk: list[int] = []
        self.min_stk: list[int] = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.min_stk.append(val if not self.min_stk else min(val, self.min_stk[-1]))

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-155-min-stack/) |
| 716 | Max Stack | [Link](https://leetcode.com/problems/max-stack/) | - |

## Key Patterns

1. **LIFO Property**: Stack naturally handles reverse-order matching (parentheses, brackets)
2. **State Preservation**: Save state before entering nested structures, restore after exiting
3. **Operator Precedence**: Use stack to defer low-precedence operations
4. **Monotonic Order**: Maintain sorted order to efficiently find extrema
5. **Index Tracking**: Store indices instead of values when you need position information

## When to Use Stack

- ✅ Matching problems (parentheses, brackets, tags)
- ✅ Expression evaluation with precedence
- ✅ Nested structure processing
- ✅ Finding next/previous greater/smaller elements
- ✅ Reversing order or processing in reverse
- ✅ Undo/redo functionality
- ✅ Function call tracking

## Common Mistakes

1. **Forgetting to check empty stack** before `st.top()` or `st.pop()`
2. **Wrong stack order** when pushing/popping multiple values
3. **Not resetting state** after processing elements
4. **Index vs value** confusion in monotonic stack problems

## More templates

- **Data structures (monotonic stack/queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

