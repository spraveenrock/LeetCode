# majority_element.py
from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find the majority element in the array using Boyer-Moore Voting Algorithm.
        
        Args:
            nums (List[int]): Input array of integers
        
        Returns:
            int: Majority element that appears more than ⌊n / 2⌋ times
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            count += 1 if num == candidate else -1
        
        return candidate

    def majorityElement_hashmap(self, nums: List[int]) -> int:
        """
        Find majority element using hash map counting approach.
        
        Args:
            nums (List[int]): Input array of integers
        
        Returns:
            int: Majority element
        """
        counts = collections.Counter(nums)
        return max(counts, key=counts.get)

def main():
    """
    Demonstrate multiple approaches to finding the majority element
    """
    solution = Solution()
    
    # Test Cases
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [1],
        [1, 1, 1, 2, 2, 2, 1]
    ]
    
    # Demonstrate different methods
    for i, nums in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print("Input Array:", nums)
        
        # Boyer-Moore Method (Recommended)
        boyer_result = solution.majorityElement(nums)
        print("Boyer-Moore Result:", boyer_result)
        
        # Hash Map Method
        hashmap_result = solution.majorityElement_hashmap(nums)
        print("Hash Map Result:", hashmap_result)
        print()

if __name__ == "__main__":
    main()
