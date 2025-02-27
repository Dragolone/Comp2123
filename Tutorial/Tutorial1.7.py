"""
算出矩阵上三角平均值 也就是算出数组A[i]到A[j]的平均值
"""


def efficient_summing_up(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = P[i - 1] + A[i - 1]

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            C[i][j] = (P[j + 1] - P[i]) / (j - i + 1)

    return C


if __name__ == "__main__":
    A = [1, 2, 3]
    result = efficient_summing_up(A)
    for row in result:
        print(row)