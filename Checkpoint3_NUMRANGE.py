class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        result = 0
        sum_dict = {}
        for start in range(len(A)):
            for end in range(start,len(A)):
                if (start,end-1) in sum_dict:
                    total = sum_dict[(start,end-1)] + A[end]
                else:
                    total = sum(A[start:end+1])
                sum_dict[(start,end)] = total
                if total > C:
                    break
                if B <= total <= C:
                    result += 1
        return result