import sys
sys.setrecursionlimit(10 ** 6)


def isValid(m, n, i, j):
    return 0 <= i < m and 0 <= j < n;


def findLongestPath(mat, m, n, i, j, isChecked):
    if not isValid(m, n, i, j):
        return 0

    isChecked[i][j] = 1
    count = 1

    if j > 0 and mat[i][j - 1] == mat[i][j] and isChecked[i][j - 1] == 0:
        count += findLongestPath(mat, m, n, i, j - 1, isChecked)

    if i > 0 and mat[i - 1][j] == mat[i][j] and isChecked[i - 1][j] == 0:
        count += findLongestPath(mat, m, n, i - 1, j, isChecked)

    if j + 1 < n and mat[i][j + 1] == mat[i][j] and isChecked[i][j + 1] == 0:
        count += findLongestPath(mat, m, n, i, j + 1, isChecked)

    if i + 1 < m and mat[i + 1][j] == mat[i][j] and isChecked[i + 1][j] == 0:
        count += findLongestPath(mat, m, n, i + 1, j, isChecked)

    return count


def isCheckedArrayToZero(isChecked,m,n):
    for k in range(m):
        isChecked.append([])
        for e in range(n):
            isChecked[k].append(0)

def output(test):

    mat = []
    with open(test, 'r') as f:
        m, n = [int(x) for x in next(f).split()]
        for line in f:
            mat.append(list(line.split()))

    res_size = 0

    for i in range(m):
        for j in range(n):

            isChecked = []
            isCheckedArrayToZero(isChecked,m,n);

            size = findLongestPath(mat, m, n, i, j, isChecked)

            if size > res_size:
                res_size = size

    print(res_size)


if __name__ == '__main__':

    print(str(sys.argv))
    args = sys.argv

    for arg in args[1:]:
        output(arg+'.txt')


