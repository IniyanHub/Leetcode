class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        worker_access = defaultdict(list)
        
        # Group times by worker name
        for name, time in zip(keyName, keyTime):
            worker_access[name].append(time)
            
        alerted_workers = []
        
        for name, times in worker_access.items():
            # A worker needs at least 3 accesses to trigger an alert
            if len(times) < 3:
                continue
                
            # Convert "HH:MM" to minutes and sort
            minutes = []
            for t in times:
                h, m = map(int, t.split(':'))
                minutes.append(h * 60 + m)
            minutes.sort()
            
            # Sliding window to check for 3 accesses within 60 minutes
            for i in range(len(minutes) - 2):
                time_diff = minutes[i+2] - minutes[i]
                if time_diff <= 60:
                    alerted_workers.append(name)
                    break # Move to the next worker once alerted
        
        # Return the sorted list of names
        return sorted(alerted_workers)
        