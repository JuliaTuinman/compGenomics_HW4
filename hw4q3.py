import sys

INF = float("inf")
MISMATCH = 3
OPEN = 5  # first column of a gap costs 4 + 1
EXTEND = 1


def main():
    with open(sys.argv[1]) as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    n, m = len(X), len(Y)

    # M: last column pairs X[i-1] with Y[j-1]
    # A: last column is X[i-1] over a gap
    # B: last column is a gap over Y[j-1]
    M = [[INF] * (m + 1) for _ in range(n + 1)]
    A = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[INF] * (m + 1) for _ in range(n + 1)]
    M[0][0] = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0 and j > 0:
                sub = 0 if X[i - 1] == Y[j - 1] else MISMATCH
                M[i][j] = min(M[i - 1][j - 1], A[i - 1][j - 1], B[i - 1][j - 1]) + sub
            if i > 0:
                A[i][j] = min(M[i - 1][j] + OPEN, B[i - 1][j] + OPEN, A[i - 1][j] + EXTEND)
            if j > 0:
                B[i][j] = min(M[i][j - 1] + OPEN, A[i][j - 1] + OPEN, B[i][j - 1] + EXTEND)

    with open(sys.argv[2], "w") as f:
        f.write(f"{M[n][m]} {A[n][m]} {B[n][m]}\n")


main()
