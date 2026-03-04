class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # 1. Check for missing character types
        missing_types = 3
        if any('a' <= c <= 'z' for c in password): missing_types -= 1
        if any('A' <= c <= 'Z' for c in password): missing_types -= 1
        if any(c.isdigit() for c in password): missing_types -= 1
        
        # 2. Analyze repeating sequences
        replace = 0       # Total replacements needed to break all repeats
        one_seq = 0       # Count of sequences with len % 3 == 0
        two_seq = 0       # Count of sequences with len % 3 == 1
        
        i = 0
        while i < n:
            length = 1
            # Expand the window as long as characters are the same
            while i + length < n and password[i + length] == password[i]:
                length += 1
            
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one_seq += 1
                elif length % 3 == 1:
                    two_seq += 1
            
            i += length
            
        # 3. Case: Password is too short
        if n < 6:
            # We need insertions. Insertions can fix missing types and break repeats.
            return max(6 - n, missing_types)
        
        # 4. Case: Password is within length limit
        if n <= 20:
            # Only replacements needed. They can fix types and repeats simultaneously.
            return max(missing_types, replace)
        
        # 5. Case: Password is too long
        delete_count = n - 20
        
        # Apply deletions to minimize the number of replacements needed
        
        # Priority 1: Use 1 deletion to save 1 replacement (target len % 3 == 0)
        # We can reduce 'replace' by 1 for every deletion we apply to these sequences
        replace -= min(delete_count, one_seq)
        delete_count -= min(delete_count, one_seq)
        
        # Priority 2: Use 2 deletions to save 1 replacement (target len % 3 == 1)
        replace -= min(delete_count // 2, two_seq)
        delete_count -= min(delete_count // 2, two_seq) * 2
        
        # Priority 3: Use 3 deletions to save 1 replacement (target any remaining sequence)
        # Any 3 deletions can shorten a sequence enough to reduce replacement count by 1
        replace -= delete_count // 3
        
        # Total steps = mandatory deletions + max(remaining replacements, missing types)
        return (n - 20) + max(missing_types, replace)
        