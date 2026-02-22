---
layout: post
title: "Algorithm Templates: String Processing"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates string
permalink: /posts/2025-11-24-leetcode-templates-string-processing/
tags: [leetcode, templates, string, algorithms]
---

{% raw %}
Minimal, copy-paste C++ for sliding window, two pointers, string matching, manipulation, and parsing. See also [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/) for KMP and rolling hash.

## Contents

- [Sliding Window](#sliding-window)
- [Two Pointers](#two-pointers)
- [String Matching](#string-matching)
- [String Manipulation](#string-manipulation)
- [Parsing](#parsing)

## Sliding Window

### Longest Substring Without Repeating Characters

```python
def lengthOfLongestSubstring(self, s):
    list[int> cnt(256, 0)
    dup = 0, best = 0
    for (l = 0, r = 0 r < len(s) r += 1) :
    dup += (cnt += 1[(unsigned char)s[r]] == 2)
    while dup > 0:
        dup -= (cnt -= 1[(unsigned char)s[l += 1]] == 1)
    best = max(best, r - l + 1)
return best
```

### Minimum Window Substring

```python
def minWindow(self, s, t):
    dict[char, int> need, window
    for (char c : t) need[c]++
    left = 0, right = 0
    valid = 0
    start = 0, len = INT_MAX
    while right < len(s):
        char c = s[right += 1]
        if need.count(c):
            window[c]++
            if (window[c] == need[c]) valid += 1
        while valid == len(need):
            if right - left < len:
                start = left
                len = right - left
            char d = s[left += 1]
            if need.count(d):
                if (window[d] == need[d]) valid -= 1
                window[d]--
    ("" if     return len == INT_MAX  else s.substr(start, len))
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 424 | Longest Repeating Character Replacement | [Link](https://leetcode.com/problems/longest-repeating-character-replacement/) | - |

## Two Pointers

### Valid Palindrome

```python
def isPalindrome(self, s):
    left = 0, right = len(s) - 1
    while left < right:
        while (left < right  and  not isalnum(s[left])) left += 1
        while (left < right  and  not isalnum(s[right])) right -= 1
        if tolower(s[left]) != tolower(s[right]):
            return False
        left += 1
        right -= 1
    return True
```

### Reverse String

```python
def reverseString(self, s):
    left = 0, right = len(s) - 1
    while left < right:
        swap(s[left += 1], s[right -= 1])
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) |
| 125 | Valid Palindrome | [Link](https://leetcode.com/problems/valid-palindrome/) | - |
| 344 | Reverse String | [Link](https://leetcode.com/problems/reverse-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-29-easy-344-reverse-string/) |
| 647 | Palindromic Substrings | [Link](https://leetcode.com/problems/palindromic-substrings/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) |

## String Matching

### KMP Algorithm

```python
def buildKMP(self, pattern):
    m = len(pattern)
    list[int> lps(m, 0)
    len = 0, i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            lps[i += 1] = len += 1
             else :
            if len != 0:
                len = lps[len - 1]
                 else :
                lps[i += 1] = 0
    return lps
def kmpSearch(self, text, pattern):
    n = len(text), m = len(pattern)
    list[int> lps = buildKMP(pattern)
    i = 0, j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j // Found at index i - j
             else if (i < n  and  text[i] != pattern[j]) :
            if j != 0:
                j = lps[j - 1]
                 else :
                i += 1
    return -1
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | - |

## String Manipulation

### Group Anagrams

```python
def groupAnagrams(self, strs):
    dict[str, list[str>> groups
    for str in strs:
        str key = str
        key.sort()
        groups[key].append(str)
    list[list[str>> result
    for ([key, values] : groups) :
    result.append(values)
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | - |
| 893 | Groups of Special-Equivalent Strings | [Link](https://leetcode.com/problems/groups-of-special-equivalent-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/easy-893-groups-of-special-equivalent-strings/) |

### Remove Duplicates

```python
// Remove All Adjacent Duplicates
def removeDuplicates(self, s):
    str result
    for c in s:
        if not not result  and  result[-1] == c:
            result.pop()
             else :
            result.append(c)
    return result
// Remove All Adjacent Duplicates II (k duplicates)
def removeDuplicates(self, s, k):
    list[pair<char, int>> st
    for c in s:
        if not not st  and  st[-1].first == c:
            st[-1].second += 1
            if st[-1].second == k:
                st.pop()
             else :
            st.append(:c, 1)
    str result
    for ([c, count] : st) :
    result.append(count, c)
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-49-group-anagrams/) |
| 1047 | Remove All Adjacent Duplicates In String | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-1047-remove-all-adjacent-duplicates-in-string/) |
| 1209 | Remove All Adjacent Duplicates in String II | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-1209-remove-all-adjacent-duplicates-in-string-ii/) |

### Run-Length Encoding

```python
// Two-pointer grouping for consecutive runs
def runLengthEncode(self, s):
    str result
    for (j = 0, k = 0 j < (int)len(s) j = k) :
    while (k < (int)len(s)  and  s[k] == s[j]) k += 1
    result += to_string(k - j) + s[j]
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 38 | Count and Say | [Link](https://leetcode.com/problems/count-and-say/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/16/medium-38-count-and-say/) |
| 443 | String Compression | [Link](https://leetcode.com/problems/string-compression/) | - |

## Parsing

### Valid Word Abbreviation

```python
def validWordAbbreviation(self, word, abbr):
    i = 0, j = 0
    n = len(word), m = len(abbr)
    while i < n  and  j < m:
        if isdigit(abbr[j]):
            if (abbr[j] == '0') return False // Leading zero
            num = 0
            while j < m  and  isdigit(abbr[j]):
                num = num  10 + (abbr[j] - '0')
                j += 1
            i += num
             else :
            if (word[i] != abbr[j]) return False
            i += 1
            j += 1
    return i == n  and  j == m
```

### Decode String

```python
def decodeString(self, s):
    list[int> numStack
    list[str> strStack
    str current
    num = 0
    for c in s:
        if isdigit(c):
            num = num  10 + (c - '0')
             else if (c == '[') :
            numStack.push(num)
            strStack.push(current)
            num = 0
            current = ""
             else if (c == ']') :
            repeat = numStack.top()
            numStack.pop()
            str temp = current
            current = strStack.top()
            strStack.pop()
            while repeat -= 1:
                current += temp
             else :
            current += c
    return current
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 408 | Valid Word Abbreviation | [Link](https://leetcode.com/problems/valid-word-abbreviation/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-408-valid-word-abbreviation/) |
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |

## More templates

- **Arrays & Strings (KMP, Manacher):** [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/)
- **Stack (decode string):** [Stack](/posts/2025-11-13-leetcode-templates-stack/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

