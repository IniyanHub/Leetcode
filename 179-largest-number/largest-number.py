class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
    
    # Custom comparator
    # If a+b > b+a, a should come before b (return -1 for ascending sort logic to put a first)
    # If a+b < b+a, b should come before a (return 1 to put a later)
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

    # Sort the numbers using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))
    
    # Join the sorted strings into a single number
        largest_num = "".join(str_nums)
    
    # Edge case: If the largest number is 0 (e.g., input [0, 0]), return "0" instead of "00"
        if largest_num[0] == '0':
            return "0"
        
        return largest_num
        