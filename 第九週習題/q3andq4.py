import numpy as np

def calculate_information_theory():
    P = np.array([0.8, 0.2])
    Q = np.array([0.4, 0.6]) # 與 P 不同的分佈
    
    epsilon = 1e-15
    P_safe = P + epsilon
    Q_safe = Q + epsilon

    entropy_P = -np.sum(P * np.log2(P_safe))
    
    cross_entropy_PQ = -np.sum(P * np.log2(Q_safe))
    
    kl_divergence = np.sum(P * np.log2(P_safe / Q_safe))
    
    cross_entropy_PP = -np.sum(P * np.log2(P_safe))

    print(f"【題三】指標計算結果：")
    print(f"      熵 H(P): {entropy_P:.4f}")
    print(f"      交叉熵 H(P, Q): {cross_entropy_PQ:.4f}")
    print(f"      KL 散度: {kl_divergence:.4f}")
    
    print(f"\n【題四】驗證 cross_entropy(p,q) > cross_entropy(p,p)：")
    print(f"      H(P, Q) = {cross_entropy_PQ:.4f}")
    print(f"      H(P, P) = {cross_entropy_PP:.4f}")
    print(f"      驗證結果: {cross_entropy_PQ > cross_entropy_PP}")

calculate_information_theory()
