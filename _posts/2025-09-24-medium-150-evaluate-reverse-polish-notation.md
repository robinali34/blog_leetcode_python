---
layout: post
title: "[Medium] 150. Evaluate Reverse Polish Notation"
date: 2025-09-24 20:00:00 -0000
categories: python reverse-polish-notation rpn problem-solving
---

# [Medium] 150. Evaluate Reverse Polish Notation

This is a classic stack problem that requires evaluating mathematical expressions written in Reverse Polish Notation (RPN). The key insight is using a stack to process operands and operators in the correct order.

## Problem Description

Given an array of strings representing a valid Reverse Polish Notation expression, evaluate the expression and return the result.

In Reverse Polish Notation:
- Operands come before operators
- Each operator takes its two preceding operands
- Division truncates toward zero

### Examples

**Example 1:**
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
```

### Constraints
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]

## Approach

The solution uses a stack-based approach:

1. **Stack Processing**: Use a stack to store operands
2. **Operator Detection**: Check if current token is an operator
3. **Operation Execution**: Pop two operands, perform operation, push result
4. **Final Result**: The remaining element in stack is the answer

## Solution 1: Using List as Stack

**Time Complexity:** O(n) - Process each token once  
**Space Complexity:** O(n) - Stack can hold up to n/2 operands

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:  # token == '/'
                    result = int(num1 / num2)  # Truncate towards zero
                stack.append(result)
        return stack[-1]
```

## Solution 2: Using List with Index Tracking

**Time Complexity:** O(n) - Process each token once  
**Space Complexity:** O(n) - List can hold up to n/2 operands

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        n = len(tokens)
        stack = [0] * ((n + 1) // 2)
        idx = -1
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if len(token) > 1 or token not in ops:
                idx += 1
                stack[idx] = int(token)
            else:
                if token == '+':
                    idx -= 1
                    stack[idx] += stack[idx + 1]
                elif token == '-':
                    idx -= 1
                    stack[idx] -= stack[idx + 1]
                elif token == '*':
                    idx -= 1
                    stack[idx] *= stack[idx + 1]
                else:  # token == '/'
                    idx -= 1
                    stack[idx] = int(stack[idx] / stack[idx + 1])  # Truncate towards zero
        return stack[idx]
```

## Step-by-Step Example

Let's trace through Solution 1 with tokens = `["2","1","+","3","*"]`:

**Step 1:** Process "2"
- Not an operator, push to stack: `[2]`

**Step 2:** Process "1"  
- Not an operator, push to stack: `[2, 1]`

**Step 3:** Process "+"
- Operator detected, pop two operands: `num2=1, num1=2`
- Perform addition: `2 + 1 = 3`
- Push result to stack: `[3]`

**Step 4:** Process "3"
- Not an operator, push to stack: `[3, 3]`

**Step 5:** Process "*"
- Operator detected, pop two operands: `num2=3, num1=3`
- Perform multiplication: `3 * 3 = 9`
- Push result to stack: `[9]`

**Result:** `9`

## Key Insights

1. **Stack LIFO**: Last In, First Out property matches RPN evaluation order
2. **Operator Precedence**: RPN eliminates need for operator precedence rules
3. **Operand Order**: First popped operand is the second operand in the operation
4. **Integer Division**: Division truncates toward zero (Python behavior)

## Solution Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **List Stack** | Clean API, easy to understand | Slight overhead from list operations |
| **List with Index** | More efficient, direct array access | Manual index management |

## Edge Cases

- **Single Operand**: Expression with only one number
- **Negative Numbers**: Tokens like "-11" (length > 1)
- **Division by Zero**: Not possible with valid RPN
- **Large Numbers**: Integer overflow considerations

## Common Mistakes

- **Operand Order**: Swapping the order of popped operands
- **Negative Number Detection**: Not handling multi-character tokens correctly
- **Stack Underflow**: Not checking if stack has enough operands
- **Integer Division**: Forgetting that division truncates toward zero

---
