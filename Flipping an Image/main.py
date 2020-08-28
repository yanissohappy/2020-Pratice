class Solution(object):
    def flipAndInvertImage(self, A):
        for row in A:
            row.reverse()
        for row_index in range(len(A)):
            for bit_index in range(len(A[row_index])):
                A[row_index][bit_index] ^= 1
        return A