class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        position = {num: i for i, num in enumerate(target)}

    # Convert arr into index array
        sequence = []

        for num in arr:
            if num in position:
                sequence.append(position[num])

    # Find LIS
        lis = []

        for num in sequence:
            idx = bisect_left(lis, num)

            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num

    # Minimum operations
        return len(target) - len(lis)
        