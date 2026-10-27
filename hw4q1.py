import sys


def main():
    with open(sys.argv[1]) as f:
        X = f.readline().strip()
        Y = f.readline().strip()
    n, m = len(X), len(Y)

    # D[i][j]: best score aligning some suffix of X[:i] with Y[:j].
    # First column is 0 (suffix of X may start anywhere); first row is
    # -2*j (prefix of Y must start at Y[0], so it is all insertions).
    prev = [-2 * j for j in range(m + 1)]
    for i in range(1, n + 1):
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            s = 1 if X[i - 1] == Y[j - 1] else -2
            cur[j] = max(prev[j - 1] + s, prev[j] - 2, cur[j - 1] - 2)
        prev = cur

    # prev is now the last row (alignments reaching the end of X).
    best_len, best = 0, prev[0]
    for j in range(m + 1):
        if prev[j] >= best:
            best, best_len = prev[j], j

    with open(sys.argv[2], "w") as f:
        f.write(f"{best_len} {best}\n")


main()
