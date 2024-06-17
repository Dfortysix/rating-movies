def max_square(n,m,matrix):
    heights = [0] * (m + 1)
    max_area = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        stack = [-1]
        for j in range(m + 1):
            while heights[j] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = j - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(j)

    return max_area


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = max_square(n,m,matrix)
print(result)