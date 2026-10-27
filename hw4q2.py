import sys


def main():
    with open(sys.argv[1]) as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    n, m = len(X), len(Y)

    # D[i][j]: edit distance of X[:i], Y[:j]; C[i][j]: number of optimal alignments.
    D = [[0] * (m + 1) for _ in range(n + 1)]
    C = [[1] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cands = [
                (D[i - 1][j - 1] + (X[i - 1] != Y[j - 1]), C[i - 1][j - 1]),
                (D[i - 1][j] + 1, C[i - 1][j]),
                (D[i][j - 1] + 1, C[i][j - 1]),
            ]
            D[i][j] = min(d for d, _ in cands)
            C[i][j] = sum(c for d, c in cands if d == D[i][j])

    with open(sys.argv[2], "w") as f:
        f.write(f"{D[n][m]} {C[n][m]}\n")


main()
