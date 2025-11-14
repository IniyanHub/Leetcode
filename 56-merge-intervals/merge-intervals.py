class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:                     # edge case: empty input
            return []

    # 1️⃣ Sort by start coordinate
        intervals.sort(key=lambda x: x[0])

        merged = []                            # result list
        cur_start, cur_end = intervals[0]      # initialise with first interval

        for start, end in intervals[1:]:
            if start <= cur_end:               # intervals overlap (or touch)
            # extend the current interval
                cur_end = max(cur_end, end)
            else:
            # no overlap → finalize current interval
                merged.append([cur_start, cur_end])
                cur_start, cur_end = start, end

    # Append the last interval we were building
        merged.append([cur_start, cur_end])
        return merged