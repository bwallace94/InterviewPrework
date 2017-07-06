class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A = set(A)
        dictA = {}
        for i in A:
            dictA[i] = False
        longest = 0
        for i in A:
            if dictA[i] == False:
                number = i
                longest_so_far = 1
                while (number+1) in dictA:
                    longest_so_far += 1
                    dictA[number+1] = True
                    number += 1
                longest = max(longest, longest_so_far)
        return longest
            
