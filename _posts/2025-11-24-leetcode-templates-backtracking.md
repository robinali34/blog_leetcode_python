---
layout: post
title: "Algorithm Templates: Backtracking"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates backtracking
permalink: /posts/2025-11-24-leetcode-templates-backtracking/
tags: [leetcode, templates, backtracking, dfs]
---
Welcome to the backtracking templates! Backtracking is one of the most versatile problem-solving techniques in competitive programming—once you learn the core pattern, you can tackle a huge family of problems from permutations to Sudoku. This page gives you battle-tested C++ templates for every major backtracking pattern, ready to adapt and submit.

> **New to Backtracking?** Backtracking = DFS + undo. You try a choice, recurse deeper, and if it doesn't work out, you undo the choice and try the next one. It's how you systematically explore all possibilities without missing any.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" style="max-width:720px;width:100%;height:auto;display:block;margin:1.5em auto;">
  <style>
    .node { rx: 18; ry: 18; stroke-width: 2; }
    .label { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 13px; fill: #4a4a4a; text-anchor: middle; dominant-baseline: central; }
    .title { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 15px; fill: #5b5b5b; font-weight: 600; text-anchor: middle; }
    .edge-label { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 11px; fill: #7a8a7a; text-anchor: middle; }
    .edge { stroke-width: 1.8; fill: none; }
    .legend { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 11px; fill: #6b6b6b; }
  </style>
  <text x="360" y="22" class="title">Subsets of [1, 2, 3] — Backtracking Decision Tree</text>
  <!-- Level 0: root {} -->
  <rect x="325" y="40" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="360" y="56" class="label">{ }</text>
  <!-- Level 1 branches -->
  <line x1="345" y1="72" x2="180" y2="130" class="edge" stroke="#a3b5a0"/>
  <text x="255" y="95" class="edge-label">+1</text>
  <line x1="375" y1="72" x2="540" y2="130" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="465" y="95" class="edge-label">skip 1</text>
  <!-- Level 1 nodes -->
  <rect x="145" y="130" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="180" y="146" class="label">{1}</text>
  <rect x="505" y="130" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="540" y="146" class="label">{ }</text>
  <!-- Level 2 from {1} -->
  <line x1="160" y1="162" x2="90" y2="220" class="edge" stroke="#a3b5a0"/>
  <text x="118" y="185" class="edge-label">+2</text>
  <line x1="200" y1="162" x2="270" y2="220" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="242" y="185" class="edge-label">skip 2</text>
  <!-- Level 2 from skip-1 side -->
  <line x1="525" y1="162" x2="460" y2="220" class="edge" stroke="#a3b5a0"/>
  <text x="485" y="185" class="edge-label">+2</text>
  <line x1="555" y1="162" x2="630" y2="220" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="600" y="185" class="edge-label">skip 2</text>
  <!-- Level 2 nodes -->
  <rect x="55" y="220" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="90" y="236" class="label">{1,2}</text>
  <rect x="235" y="220" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="270" y="236" class="label">{1}</text>
  <rect x="425" y="220" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="460" y="236" class="label">{2}</text>
  <rect x="595" y="220" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="630" y="236" class="label">{ }</text>
  <!-- Level 3 from {1,2} -->
  <line x1="75" y1="252" x2="35" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="48" y="275" class="edge-label">+3</text>
  <line x1="105" y1="252" x2="145" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="132" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {1} skip-2 -->
  <line x1="255" y1="252" x2="220" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="230" y="275" class="edge-label">+3</text>
  <line x1="285" y1="252" x2="320" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="310" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {2} -->
  <line x1="445" y1="252" x2="405" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="418" y="275" class="edge-label">+3</text>
  <line x1="475" y1="252" x2="515" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="502" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {} skip-all -->
  <line x1="630" y1="252" x2="630" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="645" y="275" class="edge-label">+3</text>
  <line x1="655" y1="252" x2="700" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="690" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 leaf nodes -->
  <rect x="5" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="40" y="326" class="label">{1,2,3}</text>
  <rect x="115" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="150" y="326" class="label">{1,2}</text>
  <rect x="190" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="225" y="326" class="label">{1,3}</text>
  <rect x="290" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="325" y="326" class="label">{1}</text>
  <rect x="375" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="410" y="326" class="label">{2,3}</text>
  <rect x="485" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="520" y="326" class="label">{2}</text>
  <rect x="600" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="635" y="326" class="label">{3}</text>
  <rect x="675" y="310" width="45" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="697" y="326" class="label">{ }</text>
  <!-- Legend -->
  <line x1="200" y1="380" x2="240" y2="380" class="edge" stroke="#a3b5a0"/>
  <text x="300" y="383" class="legend">Include element</text>
  <line x1="380" y1="380" x2="420" y2="380" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="476" y="383" class="legend">Skip element</text>
  <rect x="236" y="400" width="16" height="16" rx="4" fill="#b0c4b0" stroke="#8aaa8a" stroke-width="1.5"/>
  <text x="310" y="411" class="legend">Leaf = final subset</text>
  <text x="360" y="445" class="legend" text-anchor="middle">Each root-to-leaf path is one subset · 2³ = 8 subsets total</text>
</svg>

## Contents

- [Permutations](#permutations-all-arrangements)
- [Combinations](#combinations-choose-k-from-n)
- [Subsets](#subsets-all-subsets)
- [Combination Sum](#combination-sum-unboundedreuse-elements)
- [Grid Backtracking](#grid-backtracking-word-search-path-finding)
- [Constraint Satisfaction](#constraint-satisfaction-n-queens-sudoku)
- [Palindrome Partitioning](#palindrome-partitioning)
- [General Backtracking Template](#general-backtracking-template)

## Introduction

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") partial candidates that cannot lead to valid solutions. It's essentially a depth-first search with pruning.

**Key Characteristics:**
- Builds solutions incrementally
- Abandons partial solutions that cannot be completed (pruning)
- Uses recursion to explore the solution space
- Restores state after recursive calls (backtracking step)

**The Backtracking Template** — nearly every problem on this page follows this skeleton:

```
backtrack(current_state):
    if is_solution(current_state):
        record solution
        return
    for each choice in available_choices:
        if is_valid(choice):        ← pruning
            make_choice()
            backtrack(next_state)    ← recurse
            undo_choice()            ← backtrack
```

## Permutations (All Arrangements)

**When to use:** The problem asks for "all arrangements", "all orderings", "every possible order", or "rearrange".

Generate all permutations of distinct elements.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 340" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="20" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Permutation Tree for [1, 2, 3] — pick one unused element per level</text>
  <!-- Edges Root to L1 -->
  <line x1="370" y1="56" x2="120" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="56" x2="370" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="56" x2="620" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="232" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 1</text>
  <text x="382" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 2</text>
  <text x="508" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 3</text>
  <!-- Edges L1 to L2 -->
  <line x1="120" y1="130" x2="60" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="120" y1="130" x2="180" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="130" x2="310" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="130" x2="430" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="620" y1="130" x2="560" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="620" y1="130" x2="680" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="82" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="158" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="332" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="408" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="582" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="658" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <!-- Edges L2 to L3 (single child each) -->
  <line x1="60" y1="202" x2="60" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="180" y1="202" x2="180" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="310" y1="202" x2="310" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="430" y1="202" x2="430" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="560" y1="202" x2="560" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="680" y1="202" x2="680" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="50" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="170" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="300" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="420" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="550" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="670" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <!-- Root node -->
  <rect x="340" y="36" width="60" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="51" text-anchor="middle" font-size="12" fill="#3A3530">[ ]</text>
  <!-- L1 nodes -->
  <rect x="90" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="120" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[1]</text>
  <rect x="340" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[2]</text>
  <rect x="590" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="620" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[3]</text>
  <!-- L2 nodes -->
  <rect x="25" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="60" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[1,2]</text>
  <rect x="145" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="180" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[1,3]</text>
  <rect x="275" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="310" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[2,1]</text>
  <rect x="395" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="430" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[2,3]</text>
  <rect x="525" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="560" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[3,1]</text>
  <rect x="645" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="680" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[3,2]</text>
  <!-- L3 leaves (green-ish completed permutations) -->
  <rect x="15" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="60" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[1,2,3]</text>
  <rect x="135" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="180" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[1,3,2]</text>
  <rect x="265" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="310" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[2,1,3]</text>
  <rect x="385" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="430" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[2,3,1]</text>
  <rect x="515" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="560" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[3,1,2]</text>
  <rect x="635" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="680" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[3,2,1]</text>
  <!-- Legend -->
  <rect x="195" y="302" width="14" height="14" rx="4" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="215" y="313" font-size="10" fill="#7A7772">Partial path</text>
  <rect x="320" y="302" width="14" height="14" rx="4" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1"/>
  <text x="340" y="313" font-size="10" fill="#7A7772">Complete permutation (leaf)</text>
  <text x="370" y="335" text-anchor="middle" font-size="10" fill="#9A9792">3! = 6 permutations · each root-to-leaf path is one arrangement</text>
</svg>

### Permutations without duplicates

```python
# Permutations without duplicates
def permute_backtrack(nums: list[int], cur: list[int], used: list[bool], res: list[list[int]]) -> None:
    if len(cur) == len(nums):
        res.append(cur.copy())
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        cur.append(nums[i])
        permute_backtrack(nums, cur, used, res)
        cur.pop()
        used[i] = False
```

### Permutations with duplicates

Avoid duplicates by sorting first, then skipping duplicates at the same level when the previous duplicate hasn't been used.

```python
# Permutations with duplicates (sort first; skip same value at same level if prev unused)
def permute_unique_backtrack(nums: list[int], cur: list[int], used: list[bool], res: list[list[int]]) -> None:
    if len(cur) == len(nums):
        res.append(cur.copy())
        return
    for i in range(len(nums)):
        if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
            continue
        used[i] = True
        cur.append(nums[i])
        permute_unique_backtrack(nums, cur, used, res)
        cur.pop()
        used[i] = False


def permute_unique(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res: list[list[int]] = []
    permute_unique_backtrack(nums, [], [False] * len(nums), res)
    return res
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 46 | Permutations | [Link](https://leetcode.com/problems/permutations/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-46-permutations/) |
| 47 | Permutations II | [Link](https://leetcode.com/problems/permutations-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-47-permutations-ii/) |

## Combinations (Choose k from n)

**When to use:** The problem says "choose k from n", "select k items", or "all groups of size k" where order doesn't matter.

Generate all combinations of k elements from n elements. Order doesn't matter, so we use `start` index to avoid duplicates.

```python
# Combinations C(n, k) — choose k numbers from 1..n
def combine_backtrack(start: int, n: int, k: int, cur: list[int], res: list[list[int]]) -> None:
    if len(cur) == k:
        res.append(cur.copy())
        return
    for i in range(start, n + 1):
        cur.append(i)
        combine_backtrack(i + 1, n, k, cur, res)
        cur.pop()
```

**Key insight:** Use `start` parameter to ensure we only consider elements after the current position, preventing duplicate combinations.

| ID | Title | Link | Solution |
|---|---|---|---|
| 77 | Combinations | [Link](https://leetcode.com/problems/combinations/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-77-combinations/) |
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/medium-22-generate-parentheses/) |

## Subsets (All Subsets)

**When to use:** The problem asks for "all subsets", "power set", "all subsequences", or "every possible selection".

Generate all subsets (power set) of an array. This includes the empty set and the set itself.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 330" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="18" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Subsets of [1, 2, 3] — Include / Exclude at Each Level</text>
  <!-- Edges Root to L1 -->
  <line x1="370" y1="50" x2="185" y2="98" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="370" y1="50" x2="555" y2="98" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="264" y="68" text-anchor="middle" font-size="10" fill="#8B9B86">incl 1</text>
  <text x="476" y="68" text-anchor="middle" font-size="10" fill="#B8A5A0">excl 1</text>
  <!-- Edges L1 to L2 -->
  <line x1="185" y1="122" x2="95" y2="170" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="185" y1="122" x2="275" y2="170" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="555" y1="122" x2="465" y2="170" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="555" y1="122" x2="645" y2="170" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="132" y="142" text-anchor="middle" font-size="10" fill="#8B9B86">+2</text>
  <text x="238" y="142" text-anchor="middle" font-size="10" fill="#B8A5A0">skip 2</text>
  <text x="502" y="142" text-anchor="middle" font-size="10" fill="#8B9B86">+2</text>
  <text x="608" y="142" text-anchor="middle" font-size="10" fill="#B8A5A0">skip 2</text>
  <!-- Edges L2 to L3 -->
  <line x1="95" y1="194" x2="55" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="95" y1="194" x2="135" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="275" y1="194" x2="235" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="275" y1="194" x2="315" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="465" y1="194" x2="425" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="465" y1="194" x2="505" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="645" y1="194" x2="605" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="645" y1="194" x2="685" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="68" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="122" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="248" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="302" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="438" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="492" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="618" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="672" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <!-- Root node -->
  <rect x="342" y="30" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="45" text-anchor="middle" font-size="12" fill="#3A3530">{ }</text>
  <!-- L1 nodes -->
  <rect x="157" y="102" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="185" y="117" text-anchor="middle" font-size="12" fill="#3A3530">{1}</text>
  <rect x="527" y="102" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="555" y="117" text-anchor="middle" font-size="12" fill="#3A3530">{ }</text>
  <!-- L2 nodes -->
  <rect x="62" y="174" width="66" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="95" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{1,2}</text>
  <rect x="247" y="174" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="275" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{1}</text>
  <rect x="437" y="174" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="465" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{2}</text>
  <rect x="617" y="174" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="645" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{ }</text>
  <!-- L3 leaf nodes (green-ish, all subsets) -->
  <rect x="14" y="246" width="82" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="55" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,2,3}</text>
  <rect x="101" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="135" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,2}</text>
  <rect x="201" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="235" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,3}</text>
  <rect x="288" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="315" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1}</text>
  <rect x="391" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="425" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{2,3}</text>
  <rect x="478" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="505" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{2}</text>
  <rect x="578" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="605" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{3}</text>
  <rect x="658" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="685" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{ }</text>
  <!-- Legend -->
  <line x1="190" y1="296" x2="225" y2="296" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="235" y="300" font-size="10" fill="#7A7772">Include element</text>
  <line x1="350" y1="296" x2="385" y2="296" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="395" y="300" font-size="10" fill="#7A7772">Exclude element</text>
  <text x="370" y="322" text-anchor="middle" font-size="10" fill="#9A9792">Each root-to-leaf path is one subset · 2³ = 8 subsets total</text>
</svg>

### Subsets without duplicates

```python
# Subsets without duplicates
def subsets_backtrack(start: int, nums: list[int], cur: list[int], res: list[list[int]]) -> None:
    res.append(cur.copy())
    for i in range(start, len(nums)):
        cur.append(nums[i])
        subsets_backtrack(i + 1, nums, cur, res)
        cur.pop()
```

### Subsets with duplicates

Sort first, then skip duplicates at the same level.

```python
# Subsets with duplicates (sort first, skip duplicates at same level)
def subsets_dup_backtrack(start: int, nums: list[int], cur: list[int], res: list[list[int]]) -> None:
    res.append(cur.copy())
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        cur.append(nums[i])
        subsets_dup_backtrack(i + 1, nums, cur, res)
        cur.pop()


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []
    subsets_dup_backtrack(0, nums, [], res)
    return res
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 78 | Subsets | [Link](https://leetcode.com/problems/subsets/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/05/medium-78-subsets/) |
| 90 | Subsets II | [Link](https://leetcode.com/problems/subsets-ii/) | - |

## Combination Sum (Unbounded/Reuse Elements)

**When to use:** The problem asks for "all combinations that sum to target", "target sum with reuse allowed", or "find numbers adding to k".

Find all combinations that sum to target. Elements can be reused or used once depending on the problem.

### Combination Sum (can reuse same element)

```python
# Combination Sum (can reuse same element)
def combination_sum_backtrack(
    start: int, candidates: list[int], target: int, cur: list[int], res: list[list[int]]
) -> None:
    if target == 0:
        res.append(cur.copy())
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        cur.append(candidates[i])
        combination_sum_backtrack(i, candidates, target - candidates[i], cur, res)
        cur.pop()

```

### Combination Sum II (each element used once, duplicates exist)

```python
# Combination Sum II (each element used once, duplicates exist)
def combination_sum2_backtrack(
    start: int, candidates: list[int], target: int, cur: list[int], res: list[list[int]]
) -> None:
    if target == 0:
        res.append(cur.copy())
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        cur.append(candidates[i])
        combination_sum2_backtrack(i + 1, candidates, target - candidates[i], cur, res)
        cur.pop()


def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res: list[list[int]] = []
    combination_sum2_backtrack(0, candidates, target, [], res)
    return res

```

### Combination Sum III (choose k numbers from 1-9 that sum to n)

```python
# Combination Sum III: choose k numbers from 1-9 that sum to n
def combination_sum3_backtrack(start: int, k: int, n: int, cur: list[int], res: list[list[int]]) -> None:
    if len(cur) == k and n == 0:
        res.append(cur.copy())
        return
    if len(cur) >= k or n < 0:
        return
    for i in range(start, 10):
        cur.append(i)
        combination_sum3_backtrack(i + 1, k, n - i, cur, res)
        cur.pop()

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 39 | Combination Sum | [Link](https://leetcode.com/problems/combination-sum/) | - |
| 40 | Combination Sum II | [Link](https://leetcode.com/problems/combination-sum-ii/) | - |
| 216 | Combination Sum III | [Link](https://leetcode.com/problems/combination-sum-iii/) | - |

## Grid Backtracking (Word Search, Path Finding)

**When to use:** The problem says "find a path in a grid", "word search", "explore all directions", or involves marking/unmarking visited cells.

Backtrack on 2D grid with constraints. Mark cells as visited during exploration, then restore them.

### Word Search

```python
# Word Search: find if word exists in grid
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def word_search_dfs(board: list[list[str]], i: int, j: int, word: str, idx: int) -> bool:
    if idx == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] != word[idx]:
        return False
    temp = board[i][j]
    board[i][j] = "#"
    for di, dj in DIRS:
        if word_search_dfs(board, i + di, j + dj, word, idx + 1):
            board[i][j] = temp
            return True
    board[i][j] = temp
    return False


def word_exist(board: list[list[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if word_search_dfs(board, i, j, word, 0):
                return True
    return False

```

**Key points:**
- Mark cell as visited before recursion
- Restore cell value after recursion (backtracking)
- Check bounds and constraints before recursing

| ID | Title | Link | Solution |
|---|---|---|---|
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/medium-79-word-search/) |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) | - |
| 351 | Android Unlock Patterns | [Link](https://leetcode.com/problems/android-unlock-patterns/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/02/medium-351-android-unlock-patterns/) |
| 425 | Word Squares | [Link](https://leetcode.com/problems/word-squares/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/12/31/hard-425-word-squares/) |
| 489 | Robot Room Cleaner | [Link](https://leetcode.com/problems/robot-room-cleaner/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-hard-489-robot-room-cleaner/) |

## Constraint Satisfaction (N-Queens, Sudoku)

**When to use:** The problem involves "placing items with constraints", "N-Queens", "Sudoku", or "valid placement" where each choice must satisfy multiple rules.

Backtracking with complex constraints. Validate each move before placing.

### N-Queens

```python
# N-Queens: place n queens on n×n board (board is list[list[str]])
def n_queens_is_safe(board: list[list[str]], row: int, col: int, n: int) -> bool:
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True


def n_queens_backtrack(row: int, n: int, board: list[list[str]], res: list[list[str]]) -> None:
    if row == n:
        res.append(["".join(r) for r in board])
        return
    for col in range(n):
        if n_queens_is_safe(board, row, col, n):
            board[row][col] = "Q"
            n_queens_backtrack(row + 1, n, board, res)
            board[row][col] = "."

```

### Sudoku Solver

```python
# Sudoku Solver (mutates board in place)
def sudoku_valid(board: list[list[str]], row: int, col: int, ch: str) -> bool:
    for i in range(9):
        if board[row][i] == ch:
            return False
        if board[i][col] == ch:
            return False
    br, bc = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[br + i][bc + j] == ch:
                return False
    return True


def solve_sudoku(board: list[list[str]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                continue
            for d in "123456789":
                if not sudoku_valid(board, i, j, d):
                    continue
                board[i][j] = d
                if solve_sudoku(board):
                    return True
                board[i][j] = "."
            return False
    return True

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 51 | N-Queens | [Link](https://leetcode.com/problems/n-queens/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/hard-51-n-queens/) |
| 52 | N-Queens II | [Link](https://leetcode.com/problems/n-queens-ii/) | - |
| 37 | Sudoku Solver | [Link](https://leetcode.com/problems/sudoku-solver/) | - |

## Palindrome Partitioning

**When to use:** The problem asks to "partition a string into palindromes", "split into palindromic substrings", or "all ways to cut a string".

Partition string into palindromic substrings. Check if substring is palindrome before partitioning.

```python
# Palindrome Partitioning
def is_pal_sub(s: str, l: int, r: int) -> bool:
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def partition_backtrack(start: int, s: str, cur: list[str], res: list[list[str]]) -> None:
    if start == len(s):
        res.append(cur.copy())
        return
    for end in range(start, len(s)):
        if is_pal_sub(s, start, end):
            cur.append(s[start : end + 1])
            partition_backtrack(end + 1, s, cur, res)
            cur.pop()

```

**Optimization:** Precompute palindrome table to avoid repeated checks.

```python
# Optimized: precompute palindrome table dp[i][j]
def precompute_palindromes(s: str) -> list[list[bool]]:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            elif j == i + 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
    return dp

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 131 | Palindrome Partitioning | [Link](https://leetcode.com/problems/palindrome-partitioning/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/30/medium-131-palindrome-partitioning/) |
| 132 | Palindrome Partitioning II | [Link](https://leetcode.com/problems/palindrome-partitioning-ii/) | - |
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/08/medium-5-longest-palindromic-substring/) |
| 647 | Palindromic Substrings | [Link](https://leetcode.com/problems/palindromic-substrings/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-647-palindromic-substrings/) |

## Parentheses Generation

Generate all valid parentheses combinations using backtracking.

```python
# Generate Parentheses: generate all valid n pairs
def gen_parentheses_backtrack(n: int, open_cnt: int, close_cnt: int, path: list[str], res: list[str]) -> None:
    if len(path) == 2 * n:
        res.append("".join(path))
        return
    if open_cnt < n:
        path.append("(")
        gen_parentheses_backtrack(n, open_cnt + 1, close_cnt, path, res)
        path.pop()
    if close_cnt < open_cnt:
        path.append(")")
        gen_parentheses_backtrack(n, open_cnt, close_cnt + 1, path, res)
        path.pop()

```

**Key constraints:**
- `open < n`: Can add opening parenthesis if not all used
- `close < open`: Can add closing parenthesis if there are unmatched openings
- Base case: path length equals `2 * n`

| ID | Title | Link | Solution |
|---|---|---|---|
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/medium-22-generate-parentheses/) |
| 1087 | Brace Expansion | [Link](https://leetcode.com/problems/brace-expansion/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/26/medium-1087-brace-expansion/) |

## General Backtracking Template

```python
# Sketch — fill in problem-specific helpers
def backtrack_sketch(state, constraints, current_solution, results):
    if is_complete(current_solution):
        results.append(list(current_solution))
        return
    for candidate in iter_candidates(state):
        if not is_valid_move(candidate, constraints):
            continue
        make_move(candidate, current_solution)
        backtrack_sketch(next_state(state, candidate), constraints, current_solution, results)
        undo_move(candidate, current_solution)

```

**Key Points:**
- **Base Case**: When solution is complete, add to results
- **Pruning**: Skip invalid candidates early to reduce search space
- **Make Move**: Add candidate to current solution and update state
- **Recurse**: Explore further with updated state
- **Backtrack**: Remove candidate and restore state to try next option

**Common Optimizations:**
1. **Early pruning**: Check constraints before recursing
2. **Memoization**: Cache results for repeated subproblems (if applicable)
3. **Sorting**: Sort input to handle duplicates efficiently
4. **Precomputation**: Precompute expensive checks (e.g., palindrome table)

**Time Complexity:** Typically exponential O(2^n) or O(n!) depending on problem
**Space Complexity:** O(depth) for recursion stack + O(solution_size) for current solution

## Quick Reference

| Pattern | Signal | # Solutions | Time |
|---|---|---|---|
| Permutations | "all arrangements", "ordering" | n! | O(n × n!) |
| Combinations | "choose k from n" | C(n,k) | O(C(n,k)) |
| Subsets | "all subsets", "power set" | 2^n | O(n × 2^n) |
| Combination Sum | "target sum with reuse" | varies | O(2^n) |
| Grid | "find path in grid" | varies | O(4^(m×n)) |
| Constraint | "N-Queens", "Sudoku" | varies | O(n!) |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
