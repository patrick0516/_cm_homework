import cmath

def root2(a, b, c):
    # 1. 計算判別式 (b^2 - 4ac)
    discriminant = (b**2) - (4*a*c)
    
    # 2. 帶入公式求解，cmath.sqrt 會自動處理複數
    sol1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    sol2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    # 3. 驗證 (把根代回方程式 f(x) = ax^2 + bx + c)
    # 驗證第一個根
    f_sol1 = a*(sol1**2) + b*sol1 + c
    # 驗證第二個根
    f_sol2 = a*(sol2**2) + b*sol2 + c
    
    # 使用 cmath.isclose 檢查是否接近 0
    # 我們判斷 f_sol1 是否接近 0j (複數的零)
    check1 = cmath.isclose(f_sol1, 0j, abs_tol=1e-9)
    check2 = cmath.isclose(f_sol2, 0j, abs_tol=1e-9)
    
    print(f"根為: {sol1} 與 {sol2}")
    print(f"驗證結果: 根1是否正確? {check1}, 根2是否正確? {check2}")
    
    return sol1, sol2

# 測試範例：x^2 + 2x + 5 = 0 (這會產生複數根)
root2(1, 2, 5)
