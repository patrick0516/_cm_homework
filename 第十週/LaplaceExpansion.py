def calculate_determinant(matrix):
    # 取得矩陣大小 (n x n)
    n = len(matrix)

    # 基礎情況：2x2 矩陣直接計算
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # 基礎情況：1x1 矩陣
    if n == 1:
        return matrix[0][0]

    det = 0
    # 沿著第一列 (Row 0) 進行展開
    for j in range(n):
        # 1. 取得「餘子矩陣」：劃掉第 0 列與第 j 行
        # 這裡用列表生成式快速過濾掉不需要的列與行
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        
        # 2. 計算項數值：符號 * 元素 * 遞迴下去的結果
        # 符號由 (-1)^j 決定，因為 i 永遠是 0
        sign = 1 if j % 2 == 0 else -1
        element = matrix[0][j]
        
        # 3. 累加到總結果
        det += sign * element * calculate_determinant(minor)

    return det

# 測試範例
test_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = calculate_determinant(test_matrix)
print(f"行列式計算結果為: {result}")
