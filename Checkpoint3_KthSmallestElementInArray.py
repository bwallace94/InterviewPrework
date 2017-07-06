class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        sort = sorted(A)
        return sort[k-1]
