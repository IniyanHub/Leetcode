class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        rest = total - mx

        if mx <= rest + 1:
            return total
        else:
            return 2 * rest + 1
        