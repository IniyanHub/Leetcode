# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        
        # If the string does not start with '[', it is a single integer
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        result = None
        
        # Variables to track the number being parsed
        curr_num = 0
        is_negative = False
        num_started = False
        
        for char in s:
            if char == '[':
                # Create a new NestedInteger representing a list
                ni = NestedInteger()
                
                # If stack is not empty, add this new list to the top of the stack
                if stack:
                    stack[-1].add(ni)
                else:
                    # If stack is empty, this is our root result
                    result = ni
                
                # Push the new list onto the stack
                stack.append(ni)
                
                # Reset number parsing state
                curr_num = 0
                is_negative = False
                num_started = False
                
            elif char == '-':
                is_negative = True
                num_started = True
                
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
                num_started = True
                
            elif char == ',' or char == ']':
                # If we were parsing a number, it has ended.
                # Add the number to the NestedInteger at the top of the stack.
                if num_started:
                    val = -curr_num if is_negative else curr_num
                    stack[-1].add(NestedInteger(val))
                    
                    # Reset number parsing state
                    curr_num = 0
                    is_negative = False
                    num_started = False
                
                # If we encounter ']', we are done with the current list scope
                if char == ']':
                    stack.pop()
        
        return result
        