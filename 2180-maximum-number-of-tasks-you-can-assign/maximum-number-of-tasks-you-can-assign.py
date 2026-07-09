class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can(k):
            dq = deque()
            p = pills
            j = len(workers) - 1

            # process tasks from hardest to easiest
            for i in range(k - 1, -1, -1):

                # add every worker that can do this task after taking a pill
                while j >= len(workers) - k and workers[j] + strength >= tasks[i]:
                    dq.appendleft(workers[j])
                    j -= 1

                if not dq:
                    return False

                # strongest worker can do it without pill
                if dq[-1] >= tasks[i]:
                    dq.pop()
                else:
                    # use weakest eligible worker with a pill
                    if p == 0:
                        return False
                    p -= 1
                    dq.popleft()

            return True

        left, right = 0, min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1) // 2

            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left
        