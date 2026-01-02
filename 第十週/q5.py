import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. 建立模擬數據 (5 個樣本, 3 個特徵)
X = np.array([
    [2.5, 2.4, 0.5],
    [0.5, 0.7, 0.2],
    [2.2, 2.9, 0.8],
    [1.9, 2.2, 0.4],
    [3.1, 3.0, 0.9]
])

def manual_pca(X, n_components=2):
    # A. 中心化數據 (很重要，否則第一主成分會指向數據平均值)
    X_mean = np.mean(X, axis=0)
    X_centered = X - X_mean
    
    # B. 進行 SVD 分解
    # X_centered = U * Sigma * V^T
    U, s, Vt = np.linalg.svd(X_centered, full_matrices=False)
    
    # C. 取得主成分 (Vt 的前 k 行)
    components = Vt[:n_components]
    
    # D. 將數據投影到主成分空間
    # Project: X_new = X_centered @ V (即 Vt.T)
    X_pca = X_centered @ components.T
    
    # E. 計算解釋變異量 (Explained Variance)
    # 變異量與奇異值的平方成正比
    explained_variance = (s**2) / (X.shape[0] - 1)
    explained_variance_ratio = explained_variance / np.sum(explained_variance)
    
    return X_pca, components, explained_variance_ratio[:n_components]

# --- 執行手寫 PCA ---
n_comp = 2
X_pca_manual, components_manual, ratio_manual = manual_pca(X, n_components=n_comp)

# --- 執行 Sklearn PCA 驗證 ---
# 注意：Sklearn 預設只做中心化不做標準化，若要一致則不使用 StandardScaler
pca_sk = PCA(n_components=n_comp)
X_pca_sk = pca_sk.fit_transform(X)

print("--- PCA 降維結果 (前 2 維) ---")
print("手寫結果:\n", X_pca_manual)
print("\nSklearn 結果:\n", X_pca_sk)

print(f"\n手寫解釋變異比率: {ratio_manual}")
print(f"Sklearn 解釋變異比率: {pca_sk.explained_variance_ratio_}")

# 驗證結果是否一致 (考慮到符號可能相反)
print(f"\n結果一致性檢查 (絕對值誤差): {np.allclose(np.abs(X_pca_manual), np.abs(X_pca_sk))}")
