import numpy as np

def manual_svd_via_evd(A):
    # 轉換為浮點數矩陣
    A = np.array(A, dtype=float)
    m, n = A.shape
    
    # 1. 通過 A.T @ A 求出 V 和 奇異值的平方
    # A.T @ A 是 n x n 的對稱矩陣
    ata = A.T @ A
    eigenvalues_v, V = np.linalg.eig(ata)
    
    # 將特徵值由大到小排序，並取得對應的特徵向量索引
    idx = eigenvalues_v.argsort()[::-1]
    eigenvalues_v = eigenvalues_v[idx]
    V = V[:, idx]
    
    # 奇異值是特徵值的平方根（過濾掉極小的負值，避免浮點誤差）
    singular_values = np.sqrt(np.maximum(eigenvalues_v, 0))
    
    # 2. 構造 Sigma 矩陣 (m x n)
    Sigma = np.zeros((m, n))
    k = min(m, n)
    np.fill_diagonal(Sigma, singular_values[:k])
    
    # 3. 通過 u_i = A * v_i / sigma_i 求出 U
    # 這樣可以確保 U 和 V 的符號是一致的
    U = np.zeros((m, m))
    # 為了補齊 U 的基底（當 m > n 時），我們需要更複雜的處理，這裡先處理主要部分
    for i in range(min(m, n)):
        if singular_values[i] > 1e-10:
            U[:, i] = (A @ V[:, i]) / singular_values[i]
            
    # 如果 m > n，剩餘的 U 向量可以透過正交化補足（此處簡化處理）
    # 在實際應用中，通常 A @ V 就足夠重建原始矩陣
    
    return U, singular_values, V.T

# --- 測試驗證 ---
A = np.array([[1, 2], 
              [3, 4], 
              [5, 6]])

U, s, Vh = manual_svd_via_evd(A)

# 重建矩陣
# 重新構造 Sigma 矩陣用於乘法
Sigma_mat = np.zeros(A.shape)
np.fill_diagonal(Sigma_mat, s)
A_reconstructed = U @ Sigma_mat @ Vh

print("--- 原始矩陣 A ---")
print(A)
print("\n--- 手動 SVD 重建結果 ---")
print(np.round(A_reconstructed, 4))
print(f"\n重建誤差: {np.linalg.norm(A - A_reconstructed):.2e}")

# 比較官方 SVD 結果
u_official, s_official, vh_official = np.linalg.svd(A)
print(f"\n官方奇異值: {s_official}")
print(f"手動奇異值: {s[:len(s_official)]}")
