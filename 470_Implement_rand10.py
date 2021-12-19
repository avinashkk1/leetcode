# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand49 = 40
        while rand49 >= 40:
            rand49 = 7 * (rand7() - 1) + (rand7() - 1)
        
        return (rand49 % 10) + 1
            
        
        