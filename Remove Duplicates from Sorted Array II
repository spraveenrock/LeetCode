from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array, keeping at most two occurrences of each unique element.
        
        Args:
            nums (List[int]): Input sorted array
        
        Returns:
            int: Length of modified array with duplicates removed
        """
        # Handle arrays with 2 or fewer elements
        if len(nums) <= 2:
            return len(nums)
        
        # Pointer for writing unique elements
        k = 2
        
        # Iterate through the array starting from the third element
        for i in range(2, len(nums)):
            # If current element is different from element two positions back
            # This ensures at most two occurrences of each unique element
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k

def main():
    """
    Demonstrate the usage of removeDuplicates method
    """
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    print("Test Case 1:")
    print("Original Array:", nums1)
    k1 = solution.removeDuplicates(nums1)
    print("Modified Length:", k1)
    print("Modified Array:", nums1[:k1])
    print()
    
    # Test Case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print("Test Case 2:")
    print("Original Array:", nums2)
    k2 = solution.removeDuplicates(nums2)
    print("Modified Length:", k2)
    print("Modified Array:", nums2[:k2])

if __name__ == "__main__":
    main()
