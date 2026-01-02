import numpy as np

def lu_determinant(A):
    # 將輸入轉換為浮點數矩陣，避免整數除法錯誤
    n = len(A)
    U = np.array(A, dtype=float)
    L = np.eye(n)
    sign = 1  # 用來記錄列交換導致的正負號變化

    for i in range(n):
        # 1. 局部主元搜索 (Partial Pivoting)
        # 找到當前行以下絕對值最大的元素，並進行交換
        pivot_row = i + np.argmax(np.abs(U[i:, i]))
        if i != pivot_row:
            U[[i, pivot_row]] = U[[pivot_row, i]]
            # 注意：如果 L 也要完整記錄，這裡也要交換 L 的部分列（但在算行列式時可忽略）
            sign *= -1  # 每交換一次，符號反轉

        # 如果主元為 0，代表矩陣奇異（Singular），行列式必為 0
        if abs(U[i, i]) < 1e-12:
            return 0

        # 2. 進行高斯消去法，將下方的元素變為 0
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            # factor 實際上就是 L 矩陣的元素，但算行列式我們只需要 U
            U[j, i:] -= factor * U[i, i:]

    # 3. 計算 U 矩陣對角線乘積
    det_u = np.prod(np.diag(U))
    
    return sign * det_u

# 測試範例
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 預期結果應為 0 (因為此矩陣列線性相關)
result = lu_determinant(A)
print(f"透過 LU 分解計算的行列式為: {result:.2f}")

# 換一個可逆矩陣測試
B = [
    [3, 2, 1],
    [1, 2, 3],
    [0, 1, 4]
]
print(f"矩陣 B 的行列式為: {lu_determinant(B):.2f}")
