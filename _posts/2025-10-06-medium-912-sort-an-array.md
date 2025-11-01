---
layout: post
title: "[Medium] 912. Sort an Array"
date: 2025-10-06 00:00:00 -0000
categories: python sorting merge-sort heap-sort counting-sort data-structures divide-conquer problem-solving
---

# [Medium] 912. Sort an Array

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem in **O(n log n)** time complexity and with the smallest possible space complexity.

## Examples

**Example 1:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2:**
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

## Solution 1: Merge Sort

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

Merge sort is a divide-and-conquer algorithm that divides the array into two halves, sorts them recursively, and then merges the sorted halves.

```python
class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        cache = [0] * len(nums)
        self.mergeSort(nums, 0, len(nums) - 1, cache)
        return nums
    
    def merge(self, arr: list[int], left: int, pivot: int, right: int, cache: list[int]) -> None:
        start1 = left
        start2 = pivot + 1
        n1 = pivot - left + 1
        n2 = right - pivot

        # Copy both halves to cache
        for i in range(n1):
            cache[start1 + i] = arr[start1 + i]
        for i in range(n2):
            cache[start2 + i] = arr[start2 + i]
        
        # Merge the two halves back into arr
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if cache[start1 + i] <= cache[start2 + j]:
                arr[k] = cache[start1 + i]
                i += 1
            else:
                arr[k] = cache[start2 + j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < n1:
            arr[k] = cache[start1 + i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = cache[start2 + j]
            j += 1
            k += 1
    
    def mergeSort(self, arr: list[int], left: int, right: int, cache: list[int]) -> None:
        if left >= right:
            return
        pivot = left + (right - left) // 2
        self.mergeSort(arr, left, pivot, cache)
        self.mergeSort(arr, pivot + 1, right, cache)
        self.merge(arr, left, pivot, right, cache)
```

### How Merge Sort Works:

1. **Divide**: Split the array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the sorted halves back together

The merge operation compares elements from both halves and places them in the correct order.

## Solution 2: Heap Sort

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

Heap sort uses a max-heap to sort the array in-place.

```python
class Solution:
    def heapify(self, arr: list[int], n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Find the largest among root and children
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # If largest is not root, swap and heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    
    def heapSort(self, arr: list[int]) -> None:
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Move max to end
            self.heapify(arr, i, 0)  # Heapify reduced heap
    
    def sortArray(self, nums: list[int]) -> list[int]:
        self.heapSort(nums)
        return nums
```

### How Heap Sort Works:

1. **Build Max Heap**: Convert array to max-heap
2. **Extract Maximum**: Repeatedly extract the maximum element and place it at the end
3. **Heapify**: Maintain heap property after each extraction

## Solution 3: Counting Sort

**Time Complexity:** O(n + k) where k is the range of input  
**Space Complexity:** O(k)

Counting sort works well when the range of numbers is small.

```python
class Solution:
    def countSort(self, arr: list[int]) -> None:
        from collections import defaultdict
        counts = defaultdict(int)
        minVal = min(arr)
        maxVal = max(arr)
        
        # Count frequency of each element
        for val in arr:
            counts[val] += 1
        
        # Reconstruct sorted array
        idx = 0
        for val in range(minVal, maxVal + 1):
            if val in counts:
                while counts[val] > 0:
                    arr[idx] = val
                    idx += 1
                    counts[val] -= 1


    def sortArray(self, nums: list[int]) -> list[int]:
        self.countSort(nums)
        return nums
```

### How Counting Sort Works:

1. **Count**: Count frequency of each element
2. **Reconstruct**: Place elements back in sorted order based on their counts

## Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Stability | In-Place |
|-----------|----------------|------------------|-----------|----------|
| Merge Sort | O(n log n) | O(n) | Stable | No |
| Heap Sort | O(n log n) | O(1) | Unstable | Yes |
| Counting Sort | O(n + k) | O(k) | Stable | No |

## When to Use Each Algorithm

- **Merge Sort**: When you need a stable sort and have O(n) extra space
- **Heap Sort**: When you need in-place sorting and don't care about stability
- **Counting Sort**: When the range of numbers is small compared to array size

## Key Insights

1. **Merge Sort** guarantees O(n log n) time complexity and is stable
2. **Heap Sort** is in-place but not stable
3. **Counting Sort** can be very fast when the range is small
4. All three solutions meet the O(n log n) requirement for this problem

## Related Problems

- [75. Sort Colors](https://leetcode.com/problems/sort-colors/) - Counting sort variant
- [148. Sort List](https://leetcode.com/problems/sort-list/) - Merge sort on linked list
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Heap-based approach
