---
layout: post
title: "[Medium] 394. Decode String"
date: 2025-10-19 17:24:19 -0700
categories: python stack string-processing problem-solving
---

# [Medium] 394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there won't be input like `3a` or `2[4]`.

## Examples

**Example 1:**
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Explanation: 
- "3[a]" decodes to "aaa"
- "2[bc]" decodes to "bcbc"
- Combined: "aaabcbc"
```

**Example 2:**
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
Explanation: 
- "3[a2[c]]" decodes to "accaccacc"
- Inner "2[c]" decodes to "cc"
- Outer "3[a...]" decodes to "accaccacc"
```

**Example 3:**
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Explanation: 
- "2[abc]" decodes to "abcabc"
- "3[cd]" decodes to "cdcdcd"
- "ef" remains as "ef"
- Combined: "abcabccdcdcdef"
```

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'['` and `']'`.
- `s` is a valid encoded string, that is always possible to decode.
- All the integers in `s` are in the range `[1, 300]`.

## Solution: Stack-Based Decoding

**Time Complexity:** O(n) where n is the length of the decoded string  
**Space Complexity:** O(n) for the stack and result string

Use two stacks to handle nested encoded strings: one for counts and one for strings.

```python
class Solution:

    def decodeString(self, s: str) -> str:
        counts = []
        strings = []
        curr = ""
        k = 0
        
        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                counts.append(k)
                strings.append(curr)
                curr = ""
                k = 0
            elif ch == ']':
                decode = strings.pop()
                count = counts.pop()
                curr = decode + curr * count
            else:
                curr += ch
        
        return curr
```

## How the Algorithm Works

**Key Insight:** Use two stacks to handle nested encoded strings and maintain the current string being built.

**Steps:**
1. **Process each character** in the input string
2. **For digits:** Build the count number
3. **For '[':** Push count and current string to stacks, reset for nested processing
4. **For ']':** Pop from stacks, repeat current string, and update current string
5. **For letters:** Add to current string
6. **Return final** decoded string

## Step-by-Step Example

### Example: `s = "3[a2[c]]"`

| Character | Action | Counts Stack | Strings Stack | Current String | Explanation |
|-----------|--------|--------------|---------------|----------------|-------------|
| '3' | Build count | [] | [] | "" | k = 3 |
| '[' | Push to stacks | [3] | [""] | "" | Save state, reset |
| 'a' | Add to current | [3] | [""] | "a" | Add letter |
| '2' | Build count | [3] | [""] | "a" | k = 2 |
| '[' | Push to stacks | [3,2] | ["","a"] | "" | Save state, reset |
| 'c' | Add to current | [3,2] | ["","a"] | "c" | Add letter |
| ']' | Decode | [3] | [""] | "cc" | Repeat "c" 2 times |
| ']' | Decode | [] | [] | "accaccacc" | Repeat "cc" 3 times |

**Final result:** `"accaccacc"`

## Algorithm Breakdown

### Character Processing:
```python
for ch in s:
    if ch.isdigit():
        k = k * 10 + int(ch)
    elif ch == '[':
        counts.append(k)
        strings.append(curr)
        curr = ""
        k = 0
    elif ch == ']':
        decode = strings.pop()
        count = counts.pop()
        curr = decode + curr * count
    else:
        curr += ch
```

**Process:**
1. **Digit:** Build multi-digit count
2. **'[':** Save current state to stacks
3. **']':** Decode by repeating current string
4. **Letter:** Add to current string

### Stack Operations:

**Push Operation (on '['):**
```python
counts.push(k);
strings.push(curr);
curr = "";
k = 0;
```

**Pop Operation (on ']'):**
```python
string decode = strings.top();
strings.pop();
int count = counts.top();
while(count--) decode += curr;
counts.pop();
curr = decode;
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Character processing | O(n) | O(n) |
| Stack operations | O(n) | O(n) |
| String concatenation | O(m) | O(m) |
| **Total** | **O(n + m)** | **O(n + m)** |

Where n is the input length and m is the decoded string length.

## Edge Cases

1. **Single letter:** `s = "a"` → `"a"`
2. **Single repetition:** `s = "2[a]"` → `"aa"`
3. **No nesting:** `s = "3[a]2[b]"` → `"aaabb"`
4. **Deep nesting:** `s = "2[3[4[a]]]"` → `"aaaaaaaaaaaaaaaaaaaaaaaa"`

## Key Insights

### Stack-Based Approach:
1. **Two stacks:** One for counts, one for strings
2. **State preservation:** Save current state when entering nested brackets
3. **State restoration:** Restore state when exiting nested brackets
4. **Efficient processing:** Handle arbitrary nesting levels

### String Building:
1. **Current string:** Maintains the string being built
2. **Repetition:** Repeat current string by count
3. **Concatenation:** Build final result incrementally
4. **Memory efficient:** Process character by character

## Detailed Example Walkthrough

### Example: `s = "2[abc]3[cd]ef"`

| Character | Action | Counts Stack | Strings Stack | Current String | Explanation |
|-----------|--------|--------------|---------------|----------------|-------------|
| '2' | Build count | [] | [] | "" | k = 2 |
| '[' | Push to stacks | [2] | [""] | "" | Save state |
| 'a' | Add to current | [2] | [""] | "a" | Add letter |
| 'b' | Add to current | [2] | [""] | "ab" | Add letter |
| 'c' | Add to current | [2] | [""] | "abc" | Add letter |
| ']' | Decode | [] | [] | "abcabc" | Repeat "abc" 2 times |
| '3' | Build count | [] | [] | "abcabc" | k = 3 |
| '[' | Push to stacks | [3] | ["abcabc"] | "" | Save state |
| 'c' | Add to current | [3] | ["abcabc"] | "c" | Add letter |
| 'd' | Add to current | [3] | ["abcabc"] | "cd" | Add letter |
| ']' | Decode | [] | [] | "abcabccdcdcd" | Repeat "cd" 3 times |
| 'e' | Add to current | [] | [] | "abcabccdcdcde" | Add letter |
| 'f' | Add to current | [] | [] | "abcabccdcdcdef" | Add letter |

**Final result:** `"abcabccdcdcdef"`

## Alternative Approaches

### Approach 1: Recursive Solution
```python
class Solution:
    def decodeString(self, s: str, i: list[int]) -> str:
        result = ""
        while i[0] < len(s) and s[i[0]] != ']':
            if s[i[0]].isdigit():
                k = 0
                while i[0] < len(s) and s[i[0]].isdigit():
                    k = k * 10 + int(s[i[0]])
                    i[0] += 1
                i[0] += 1  # skip '['
                decoded = self.decodeString(s, i)
                i[0] += 1  # skip ']'
                result += decoded * k
            else:
                result += s[i[0]]
                i[0] += 1
        return result
    
    def decodeString(self, s: str) -> str:
        return self.decodeString(s, [0])
```

**Time Complexity:** O(n + m)  
**Space Complexity:** O(n) for recursion stack

### Approach 2: Iterative with Single Stack
```python
class Solution:

    def decodeString(self, s: str) -> str:
        st = []
        curr = ""
        k = 0
        
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                st.append(str(k))
                st.append(curr)
                curr = ""
                k = 0
            elif c == ']':
                prev = st.pop()
                count = int(st.pop())
                temp = curr * count
                curr = prev + temp
            else:
                curr += c
        return curr
```

**Time Complexity:** O(n + m)  
**Space Complexity:** O(n)

## Common Mistakes

1. **Wrong count handling:** Not building multi-digit numbers correctly
2. **Stack order:** Pushing/popping in wrong order
3. **String concatenation:** Not handling nested repetitions properly
4. **Edge cases:** Not handling single characters or no brackets

## Related Problems

- [71. Simplify Path](https://leetcode.com/problems/simplify-path/)
- [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)

## Why This Solution Works

### Stack-Based Approach:
1. **Two stacks:** Efficiently handle nested structures
2. **State preservation:** Save current state when entering brackets
3. **State restoration:** Restore state when exiting brackets
4. **Arbitrary nesting:** Handle any level of nesting

### String Processing:
1. **Character by character:** Process input incrementally
2. **Count building:** Handle multi-digit numbers
3. **String repetition:** Efficiently repeat strings
4. **Memory efficient:** Build result incrementally

### Key Algorithm Properties:
1. **Correctness:** Always produces valid decoded string
2. **Efficiency:** O(n + m) time complexity
3. **Simplicity:** Easy to understand and implement
4. **Scalability:** Handles arbitrary nesting levels
