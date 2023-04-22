class NumArray:
    def __init__(self, nums:List[int]):
        self.nums = nums
    def sumRange(self, left: int, right:int) -> int:
        return sum(self.nums[left:right+1])
"""
You are given an integer array nums, and you need to implement the NumArray class to handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive, where left <= right.
The NumArray class should have the following two methods:

NumArray(int[] nums): Initializes the object with the integer array nums.
int sumRange(int left, int right): Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
For example, if the input nums array is [1, 2, 3, 4, 5] and we call sumRange(0, 2), the output should be 6 (since the sum of the elements between indices 0 and 2 inclusive is 1 + 2 + 3 = 6).

To solve this problem, you need to implement the NumArray class and the sumRange method. The NumArray constructor should initialize the private instance variable nums to the input nums array. The sumRange method should iterate over the elements of nums between the given indices left and right, and add them up to get the sum.
"""
