

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        K = r - l + 1
        MOD = 10**9+7
        M = [[0 for _ in range(K*2)] for _ in range(K*2)]
        def multiply_matrices(A, B, MOD):
            n = len(A)
            C = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                r_c = C[i]
                r_a = A[i]
                for k in range(n):
                    val = r_a[k]
                    if not val:
                        continue
                    r_b = B[k]
                    for j in range(n):
                        r_c[j] += val * r_b[j]
                    for j in range(n):
                        r_c[j] %= MOD
            return C
        def matrix_pow(M, n, MOD):
            size = len(M)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            bs = M
            while n > 0:
                if n % 2 == 1:
                    result = multiply_matrices(result, bs, MOD)
                bs = multiply_matrices(bs, bs, MOD)
                n //= 2
            return result
        def multiply_vector_matrix(vector, matrix, MOD):
            n = len(vector)
            result = [0] * n
            for i in range(n):
                current_sum = 0
                for j in range(n):
                    current_sum = (current_sum + vector[j] * matrix[j][i]) % MOD
                result[i] = current_sum
            return result
        for x in range(K):
            for y in range(x + 1, K):
                M[K + y][x] = 1
            for y in range(0, x):
                M[y][K + x] = 1

        matrix = matrix_pow(M, n-1, MOD)
        V1 = [1] * (2 * K)
        Vn = multiply_vector_matrix(V1, matrix, MOD)
        return sum(Vn) % MOD


obj = Solution()
n = 3
l = 4
r = 5
print(obj.zigZagArrays(n, l, r))


