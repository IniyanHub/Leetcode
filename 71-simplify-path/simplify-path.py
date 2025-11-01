class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        
        # Split the path by '/' to get individual components
        components = path.split('/')
        
        for component in components:
            # Rule 1: Ignore empty strings and single periods
            if component == '' or component == '.':
                continue
            # Rule 2: Handle double periods (parent directory)
            elif component == '..':
                # Pop from the stack if it's not empty (go up one level)
                if stack:
                    stack.pop()
            # Rule 3: Push valid directory/file names onto the stack
            else:
                stack.append(component)
        
        # Reconstruct the canonical path from the stack
        # Join components with '/' and prepend a leading '/'
        # If the stack is empty, "/".join([]) is "", so the result is "/", which is correct.
        return "/" + "/".join(stack)

        