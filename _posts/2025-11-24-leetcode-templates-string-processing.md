---
layout: post
title: "Algorithm Templates: String Processing"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates string
permalink: /posts/2025-11-24-leetcode-templates-string-processing/
tags: [leetcode, templates, string, algorithms]
---

{% raw %}
Minimal, copy-paste Python for sliding window, two pointers, string matching, manipulation, and parsing. See also [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/) for KMP and rolling hash.

## Contents

- [Sliding Window](#sliding-window)
- [Two Pointers](#two-pointers)
- [String Matching](#string-matching)
- [String Manipulation](#string-manipulation)
- [Parsing](#parsing)

## Sliding Window

### Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    cnt = [0] * 256
    dup = 0
    best = 0
    l = 0
    for r in range(len(s)):
        idx = ord(s[r]) % 256
        cnt[idx] += 1
        if cnt[idx] == 2:
            dup += 1
        while dup > 0:
            j = ord(s[l]) % 256
            cnt[j] -= 1
            if cnt[j] == 1:
                dup -= 1
            l += 1
        best = max(best, r - l + 1)
    return best

```

### Minimum Window Substring

```python
def min_window(s: str, t: str) -> str:
    from collections import Counter

    need = Counter(t)
    window: dict[str, int] = {}
    left = right = 0
    valid = 0
    start, min_len = 0, 10**9
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        while valid == len(need):
            if right - left < min_len:
                start = left
                min_len = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return "" if min_len == 10**9 else s[start : start + min_len]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 424 | Longest Repeating Character Replacement | [Link](https://leetcode.com/problems/longest-repeating-character-replacement/) | - |

## Two Pointers

### Valid Palindrome

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

```

### Reverse String

```python
def reverse_string_list(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

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
def build_kmp_lps(pattern: str) -> list[int]:
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    lps = build_kmp_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        if i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | - |

## String Manipulation

### Group Anagrams

```python
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for w in strs:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | - |
| 242 | Valid Anagram | [Link](https://leetcode.com/problems/valid-anagram/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/07/easy-242-valid-anagram/) |
| 383 | Ransom Note | [Link](https://leetcode.com/problems/ransom-note/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/07/easy-383-ransom-note/) |
| 893 | Groups of Special-Equivalent Strings | [Link](https://leetcode.com/problems/groups-of-special-equivalent-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/easy-893-groups-of-special-equivalent-strings/) |

### Remove Duplicates

```python
# Remove All Adjacent Duplicates
def remove_adjacent_duplicates(s: str) -> str:
    st: list[str] = []
    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)
    return "".join(st)


# Remove All Adjacent Duplicates II (k duplicates)
def remove_adjacent_duplicates_k(s: str, k: int) -> str:
    st: list[list] = []  # [char, count]
    for c in s:
        if st and st[-1][0] == c:
            st[-1][1] += 1
            if st[-1][1] == k:
                st.pop()
        else:
            st.append([c, 1])
    return "".join(ch * cnt for ch, cnt in st)

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-49-group-anagrams/) |
| 1047 | Remove All Adjacent Duplicates In String | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-1047-remove-all-adjacent-duplicates-in-string/) |
| 1209 | Remove All Adjacent Duplicates in String II | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-1209-remove-all-adjacent-duplicates-in-string-ii/) |

### Run-Length Encoding

```python
# Two-pointer grouping for consecutive runs (illustrative RLE)
def run_length_encode(s: str) -> str:
    parts: list[str] = []
    j = 0
    n = len(s)
    while j < n:
        k = j
        while k < n and s[k] == s[j]:
            k += 1
        parts.append(str(k - j) + s[j])
        j = k
    return "".join(parts)

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 38 | Count and Say | [Link](https://leetcode.com/problems/count-and-say/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/16/medium-38-count-and-say/) |
| 443 | String Compression | [Link](https://leetcode.com/problems/string-compression/) | - |

## Parsing

### Valid Word Abbreviation

```python
def valid_word_abbreviation(word: str, abbr: str) -> bool:
    i = j = 0
    n, m = len(word), len(abbr)
    while i < n and j < m:
        if abbr[j].isdigit():
            if abbr[j] == "0":
                return False
            num = 0
            while j < m and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1
    return i == n and j == m

```

### Decode String

```python
def decode_string(s: str) -> str:
    num_stack: list[int] = []
    str_stack: list[str] = []
    current = ""
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            num_stack.append(num)
            str_stack.append(current)
            num = 0
            current = ""
        elif c == "]":
            repeat = num_stack.pop()
            prev = str_stack.pop()
            current = prev + current * repeat
        else:
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

