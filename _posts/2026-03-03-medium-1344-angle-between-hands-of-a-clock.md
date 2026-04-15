---
layout: post
title: "[Medium] 1344. Angle Between Hands of a Clock"
date: 2026-03-03 00:00:00 -0700
categories: [leetcode, medium, math, geometry]
tags: [leetcode, medium, math, geometry, simulation]
permalink: /2026/03/03/medium-1344-angle-between-hands-of-a-clock/
---

# [Medium] 1344. Angle Between Hands of a Clock

## Problem Statement

Given two integers `hour` and `minutes`, return the **smaller angle** (in degrees) formed between the hour hand and the minute hand on a clock.

The answer must be in the range \([0, 180]\).

## Examples

**Example 1:**

```python
Input:  hour = 12, minutes = 30
Output: 165.0
Explanation:
Minute hand: 30 minutes → 30 * 6 = 180 degrees
Hour hand: (12 % 12 + 30/60) * 30 = 15 degrees
Angle = |180 - 15| = 165
```

**Example 2:**

```python
Input:  hour = 3, minutes = 30
Output: 75.0
```

**Example 3:**

```python
Input:  hour = 3, minutes = 15
Output: 7.5
```

## Constraints

- `1 <= hour <= 12`
- `0 <= minutes <= 59`
- Answers are expected as a `float` with reasonable precision.

## Clarification Questions

1. **12 vs 0 o’clock**: Should `hour = 12` be treated the same as `0` on the circle?  
   **Assumption**: Yes — use `hour % 12`.
2. **Return type**: Should we return a float or rounded integer?  
   **Assumption**: Float (Python `float`) with standard precision is acceptable.
3. **Smaller angle**: If the two hands form angles `x` and `360 - x`, should we always return the smaller one?  
   **Assumption**: Yes — answer must be in \([0, 180]\).
4. **Edge cases**: When hands overlap (e.g., `12:00`), is `0.0` a valid answer?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Convert positions to degrees (5 min)**  
On a clock:
- The minute hand moves **6 degrees per minute** (`360 / 60`).
- The hour hand moves **30 degrees per hour** (`360 / 12`), plus it moves continuously as minutes pass.

**Step 2: Formulas (7 min)**  
For a given time `hour`, `minutes`:

- Minute hand angle:

```text
minute_angle = minutes * 6
```

- Hour hand angle:

```text
hour_angle = (hour % 12 + minutes / 60) * 30
```

The absolute difference:

```text
diff = |hour_angle - minute_angle|
```

**Step 3: Smaller of the two angles (8 min)**  
Clock hands split the circle into two angles: `diff` and `360 - diff`.
We need the **smaller** one:

```text
answer = min(diff, 360 - diff)
```

Return `answer`.

## Solution Approach

1. Normalize `hour` with `hour % 12` so `12` is treated as `0`.
2. Compute `hour_angle` using hours plus fractional hours from minutes.
3. Compute `minute_angle` as `minutes * 6`.
4. Take the absolute difference between these two angles.
5. Return the smaller angle between `diff` and `360 - diff`.

### Key Insights

1. **Continuous hour hand**  
   The hour hand is not fixed per hour; it moves as minutes progress, which is why we add `minutes / 60` to `hour`.

2. **Normalize 12 to 0**  
   Using `hour % 12` simplifies math and avoids special casing for `12`.

3. **Two possible angles**  
   Since a circle is 360 degrees, the angle between two directions can be taken in two ways; always pick the smaller.

## Python Solution

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Hour hand: 30 degrees per hour + 0.5 degrees per minute
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        # Minute hand: 6 degrees per minute
        minutes_angle = (minutes % 60) * 6

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
```

## Algorithm Explanation

- The minute hand angle is straightforward: there are 60 minutes on the clock, so each minute is \(360 / 60 = 6\) degrees.
- The hour hand moves 30 degrees per hour; since there are 60 minutes in an hour, it also moves \(30 / 60 = 0.5\) degrees per minute.
- By computing both angles and taking their difference, we get one of the angles between the two hands.
- Taking `min(diff, 360 - diff)` ensures we return the **smaller** of the two possible angles.

## Complexity Analysis

- **Time Complexity**: \(O(1)\) — just a few arithmetic operations.
- **Space Complexity**: \(O(1)\) — constant extra space.

## Edge Cases

- `hour = 12`, `minutes = 0` → both hands at 0 degrees → angle `0.0`.
- `hour = 12`, `minutes = 30` → hands at 15 and 180 degrees → angle `165.0`.
- `hour = 6`, `minutes = 0` → hands at 180 and 0 degrees → angle `180.0`.

## Common Mistakes

- Forgetting to normalize `hour` with `% 12`, which can lead to incorrect angles when `hour = 12`.
- Ignoring the continuous movement of the hour hand during minutes (using `hour * 30` only).
- Returning `diff` directly without taking `min(diff, 360 - diff)`.

## Related Problems

- [LC 1360: Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/) — Another date/time arithmetic problem.
- [LC 1275: Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) — Board-state simulation logic. 

