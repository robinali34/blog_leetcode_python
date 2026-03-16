---
layout: post
title: "433. Minimum Genetic Mutation"
date: 2026-03-15 00:00:00 -0700
categories: [leetcode, medium, graph, bfs]
tags: [leetcode, medium, bfs, shortest-path, string]
permalink: /2026/03/15/medium-433-minimum-genetic-mutation/
---

# 433. Minimum Genetic Mutation

## Problem Statement

A gene string is represented by an 8-character string consisting only of `'A'`, `'C'`, `'G'`, and `'T'`.

You are given a **start gene** string `startGene`, an **end gene** string `endGene`, and a list of valid gene strings `bank`.

You may mutate the gene from one string to another **by changing exactly one character at a time**. Each intermediate gene string **must be in `bank`**.

Return the **minimum number of mutations** needed to change `startGene` to `endGene`. If it is impossible, return `-1`.

## Examples

**Example 1:**

```python
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
```

**Example 2:**

```python
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
# One shortest sequence:
# AACCGGTT → AACCGGTA → AAACGGTA
```

**Example 3:**

```python
Input: startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
```

## Constraints

- `startGene.length == 8`
- `endGene.length == 8`
- `1 <= bank.length <= 10^4`
- `bank[i].length == 8`
- `startGene`, `endGene`, and `bank[i]` consist only of `'A'`, `'C'`, `'G'`, `'T'`

## Clarification Questions

1. **Single-character mutation**: Each step must change **exactly one** position?  
   **Assumption**: Yes — Hamming distance between consecutive genes must be 1.
2. **Validity**: Every intermediate gene must belong to `bank`?  
   **Assumption**: Yes, and we can only traverse through genes in `bank`.
3. **Reusing genes**: Can we revisit the same gene multiple times?  
   **Assumption**: We could, but it’s never helpful for shortest path, so we will mark visited genes and avoid revisiting.

## Abstraction

Model this as a **shortest path** problem in an unweighted graph:

- Each valid gene string is a **node** (including `startGene` if not in `bank`).  
- There is an **edge** between two genes if they differ by exactly one character.  
- We want the **minimum number of edges** from `startGene` to `endGene`.

This is a classic BFS-on-strings problem, similar to Word Ladder but with a fixed 4-letter alphabet and fixed length 8.

## Baseline (Naive) — Why it’s suboptimal

Naive idea:

- From current gene, scan all strings in `bank` and check if they differ by one character, then recurse/DFS.

This can:

- Revisit many genes, causing exponential blowup.  
- Not guarantee we find the **shortest** path first (DFS explores deep before shallow).

## Optimized Approach — BFS over gene space

Since each mutation step has **equal cost 1**, **BFS** from `startGene` to `endGene` guarantees the minimum number of mutations.

Strategy:

1. Put all `bank` genes into a set for O(1) membership.\n2. If `endGene` is not in `bank`, return `-1` (cannot end at an invalid gene).\n3. BFS from `startGene`, level by level, treating each mutation as an edge.\n4. For a gene `curr`, generate all possible one-character mutations by trying the 4 bases `'A','C','G','T'` at each position. When a mutation is in `bank_set`, push it to the queue and remove it from the set (mark visited).\n5. When we pop `endGene`, return the current `steps` count.

### Complexity

- Let `L = 8` (fixed gene length), `N = len(bank)`.  
- For each gene we process, we generate `L * 4 = 32` potential neighbors and check membership in a set.  
- In the worst case we process each bank gene at most once.  
- **Time**: O(N * L * 4) ≈ O(N).  
- **Space**: O(N) for the bank set and BFS queue.

### Key Insights

1. **BFS for shortest path** — All edges cost 1 mutation; BFS finds the minimum steps.  
2. **Generate neighbors by position + base** — Instead of precomputing full adjacency, generate possible mutations on the fly.  
3. **Use a set for bank / visited** — O(1) checks for valid, unvisited genes.

## Python Solution (BFS)

```python
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        q = deque([startGene])
        steps = 0
        genes = ["A", "C", "G", "T"]

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endGene:
                    return steps
                for i in range(len(curr)):
                    for g in genes:
                        mutation = curr[:i] + g + curr[i + 1 :]
                        if mutation in bank_set:
                            q.append(mutation)
                            bank_set.remove(mutation)
            steps += 1
        return -1
```

## Algorithm Explanation

We treat each gene as a node in a graph, with edges between genes differing by one character. We start BFS from `startGene` with `steps = 0`. For each level:

- Pop all genes at the current distance.  
- If any equals `endGene`, return `steps`.  
- For each gene, try mutating each position with each of the 4 characters; if the resulting gene is in `bank_set`, we add it to the queue and remove it from `bank_set` to mark it visited.

After exhausting the queue without seeing `endGene`, we return `-1` (no valid mutation sequence).

## Complexity Analysis

- **Time**: O(N * L * 4) where `N = len(bank)` and `L = 8`; effectively O(N).  
- **Space**: O(N) for `bank_set` and the BFS queue.

## Edge Cases

- `endGene` not in `bank` → immediately return `-1`.  
- `startGene == endGene` → if you want to be strict, return 0 (though LeetCode usually ensures `startGene` ≠ `endGene`).  
- Duplicate genes in `bank` are handled by the set.\n\n## Common Mistakes\n\n- **Not checking `endGene` in bank first** — Then you may do unnecessary work or incorrectly return a non-negative value.  
- **Revisiting genes** — Without marking visited (removing from set), BFS can cycle and blow up in time.  
- **Precomputing all edges** — You can, but generating neighbors on the fly is simpler and efficient enough.\n\n## Related Problems\n\n- [LC 127: Word Ladder](https://leetcode.com/problems/word-ladder/) — Similar BFS over string space for shortest transformation sequence.  
- [LC 1091: Shortest Path in Binary Matrix](/2026/03/11/medium-1091-shortest-path-in-binary-matrix/) — BFS for shortest path in a grid.  
- [LC 752: Open the Lock](/2025/10/20-medium-752-open-the-lock/) — BFS over state space with digits.\n*** End Patch"}``` завершается ошибкой because ApplyPatch expects just patch, not JSON. I already provided correctly: good. Let's wait.}-->
