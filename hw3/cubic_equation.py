import cmath

def root3(a, b, c, d):
    # 1. 定義中間變數 (照著維基百科公式定義，避免寫錯)
    # 這裡假設 a 不為 0
    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    
    # 2. 計算大 C (立方根部分)
    # 這裡要處理開根號內的數值，避免直接運算噴錯
    inner_sqrt = cmath.sqrt(delta1**2 - 4*delta0**3)
    C = ((delta1 + inner_sqrt) / 2)**(1/3)
    
    # 如果 C 是 0，換另一個根號解 (公式中的特殊情況處理)
    if C == 0:
        C = ((delta1 - inner_sqrt) / 2)**(1/3)
    
    # 3. 三次單位的旋轉因子 (u1 為 1, u2 和 u3 分別旋轉 120 度與 240 度)
    u = [1, cmath.exp(2j * cmath.pi / 3), cmath.exp(4j * cmath.pi / 3)]
    
    # 4. 求出三個根
    roots = []
    for i in range(3):
        r = -1/(3*a) * (b + u[i]*C + delta0/(u[i]*C if C != 0 else 1))
        roots.append(r)
    
    # 5. 驗證並印出結果
    print(f"三個根分別為：")
    for i, r in enumerate(roots):
        # 驗證 f(x) = ax^3 + bx^2 + cx + d 是否趨近於 0
        val = a*r**3 + b*r**2 + c*r + d
        is_correct = cmath.isclose(val, 0, abs_tol=1e-9)
        print(f"根 {i+1}: {r} (驗證結果: {is_correct})")
        
    return roots

# 測試範例
# x^3 - 6x^2 + 11x - 6 = 0 (根應該是 1, 2, 3)
root3(1, -6, 11, -6)
