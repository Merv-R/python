"""
Given an array of integers of length N. Majority element occurs with a frequency > N/2. Find the majority element.

Constraints:
1 <= N <= 1e6

Example:
Input: [3,2,2,4,2,2]
Output: 2

Explanation:
2 occurs with the frequency of 2 > (6/2 = 3)
"""

from collections import Counter


def majority_element_v1(elements: list[int]) -> int:
    return Counter(elements).most_common(1)[0][0]

def majority_element_v2(elements: list[int]) -> int:
    
    pass