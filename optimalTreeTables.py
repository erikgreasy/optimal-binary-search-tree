INT_MAX = 2147483647


def optimalTreeTables(p, q, n):
    # INIT TABLES
    e = [[0 for _ in range(1, n + 2)] for i in range(n+1)]
    w = [[0 for _ in range(1, n + 2)] for i in range(n+1)]
    root = [[0 for _ in range(1, n+1)] for i in range(1, n+1)]

    for i in range(1, n+1):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]

    for l in range(1, n+1):
        for i in range(1, n-l+1):
            j = i+l-1
            e[i][j] = INT_MAX
            w[i][j] = w[i][j-1] + p[j] + q[j]

            for r in range(i, j + 1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]

                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return (e, root)
