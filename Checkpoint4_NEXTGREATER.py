class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        result = []
        for i,number in enumerate(A):
            found = False
            for j in A[i+1:]:
                if j > number:
                    result.append(j)
                    found = True
                    break
            if not found:
                result.append(-1)
        return result