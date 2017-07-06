class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        num_rows = A * 2 - 1
        result = []
        for i in range(num_rows):
            row = []
            for j in range(num_rows):
                r = i
                if i >= A:
                    r = num_rows-i-1
                c = j
                if j >= A:
                    c = num_rows-j-1
                row.append(A - min(r,c))
            result.append(row)
        return result
