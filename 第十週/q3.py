import numpy as np
from scipy.linalg import lu, eig, svd

# 建立一個隨機方陣作為測試對象
np.set_printoptions(suppress=True, precision=4)
A = np.array([[4, 3, 2],
              [3, 2, 1],
              [2, 1, 3]], dtype=float)

print("--- 原始矩陣 A ---")
print(A)
print("\n" + "="*50 + "\n")

# 1. 驗證 LU 分解 (A = P @ L @ U)
P, L, U = lu(A)
A_reconstructed_lu = P @ L @ U
print("1. [LU 分解] 驗證結果 (P * L * U):")
print(A_reconstructed_lu)
print(f"重建誤差: {np.linalg.norm(A - A_reconstructed_lu):.2e}")
print("-" * 30)

# 2. 驗證特徵值分解 (A = V @ D @ V_inv)
eigenvalues, V = eig(A)
D = np.diag(eigenvalues)
V_inv = np.linalg.inv(V)
A_reconstructed_evd = V @ D @ V_inv
# 取實部，因為數值運算有時會產生極小的虛部
A_reconstructed_evd = np.real(A_reconstructed_evd)
print("2. [特徵值分解] 驗證結果 (V * D * V_inv):")
print(A_reconstructed_evd)
print(f"重建誤差: {np.linalg.norm(A - A_reconstructed_evd):.2e}")
print("-" * 30)

# 3. 驗證 SVD 分解 (A = U @ Sigma @ Vh)
U_svd, s, Vh = svd(A)
# s 是一維陣列，需要轉換為對角矩陣 Sigma
Sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(Sigma, s)
A_reconstructed_svd = U_svd @ Sigma @ Vh
print("3. [SVD 分解] 驗證結果 (U * Sigma * Vh):")
print(A_reconstructed_svd)
print(f"重建誤差: {np.linalg.norm(A - A_reconstructed_svd):.2e}")
