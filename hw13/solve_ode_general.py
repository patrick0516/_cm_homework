import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    """
    求解常係數齊次常微分方程：a_n*y^(n) + ... + a_1*y' + a_0*y = 0
    """
    # 1. 使用 numpy 求得特徵方程的所有根
    roots = np.roots(coefficients)
    
    # 2. 處理浮點數誤差並統計根的重數
    # 精度取到 6 位以確保重根能被正確分類
    rounded_roots = [complex(round(r.real, 6), round(r.imag, 6)) for r in roots]
    counts = Counter(rounded_roots)
    
    # 用來存放基礎解系的每一項
    terms = []
    # 用來標記已處理過的共軛複根
    processed = set()
    
    # 3. 遍歷唯一的根並根據數學規則生成解
    # 排序是為了讓輸出結果（C1, C2...）的順序相對穩定
    unique_roots = sorted(counts.keys(), key=lambda x: (x.real, x.imag))
    
    for r in unique_roots:
        if r in processed:
            continue
            
        alpha = r.real
        beta = r.imag
        m = counts[r]  # 該根的重數
        
        # 判斷是實根還是複根 (虛部極小視為實根)
        if abs(beta) < 1e-6:
            for k in range(m):
                x_pow = f"x^{k}" if k > 0 else ""
                exp_part = f"e^({alpha:g}x)" if alpha != 0 else ("1" if k == 0 else "")
                
                # 組合實根解
                if k == 0 and alpha == 0:
                    terms.append("1")
                elif alpha == 0:
                    terms.append(f"x^{k}")
                else:
                    term = f"{x_pow}{exp_part}" if x_pow else exp_part
                    terms.append(term)
            processed.add(r)
        else:
            # 處理複數共軛根對 alpha +/- beta*i
            for k in range(m):
                x_pow = f"x^{k}" if k > 0 else ""
                exp_part = f"e^({alpha:g}x)" if abs(alpha) > 1e-6 else ""
                
                # 組合 cos 和 sin 項
                prefix = f"{x_pow}{exp_part}" if (x_pow or exp_part) else ""
                terms.append(f"{prefix}cos({abs(beta):g}x)")
                terms.append(f"{prefix}sin({abs(beta):g}x)")
            
            # 將正負共軛根都標記為已處理
            processed.add(r)
            processed.add(complex(alpha, -beta))

    # 4. 格式化最終通解字串
    solution_parts = [f"C_{i+1}({term})" for i, term in enumerate(terms)]
    return "y(x) = " + " + ".join(solution_parts)


# --- 以下是測試主程式 ---

# 範例測試 (1): 實數單根
print("--- 實數單根範例 ---")
coeffs1 = [1, -3, 2]
print(f"方程係數: {coeffs1}")
print(solve_ode_general(coeffs1))

# 範例測試 (2): 實數重根
print("\n--- 實數重根範例 ---")
coeffs2 = [1, -4, 4]
print(f"方程係數: {coeffs2}")
print(solve_ode_general(coeffs2))

# 範例測試 (3): 複數共軛根
print("\n--- 複數共軛根範例 ---")
coeffs3 = [1, 0, 4]
print(f"方程係數: {coeffs3}")
print(solve_ode_general(coeffs3))

# 範例測試 (4): 複數重根 (二重)
print("\n--- 複數重根範例 ---")
coeffs4 = [1, 0, 2, 0, 1]
print(f"方程係數: {coeffs4}")
print(solve_ode_general(coeffs4))

# 範例測試 (5): 高階重根
print("\n--- 高階重根範例 ---")
coeffs5 = [1, -6, 12, -8]
print(f"方程係數: {coeffs5}")
print(solve_ode_general(coeffs5))
