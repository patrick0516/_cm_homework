import math

# 題一
p = 0.5
n = 10000
try:
    direct_result = p ** n
    print(f"【題一】直接計算 0.5^10000: {direct_result}") 
    # 在大多數環境下會輸出 0.0，因為數值太小超出浮點數限制
except OverflowError:
    print("【題一】數值過小，發生下溢 (Underflow)")

# 題二
log_p_n = n * math.log10(p)
print(f"【題二】使用對數計算 log10(0.5^10000): {log_p_n:.4f}")

# 數值 = 10^(log_result) = 10^(整數部分 + 小數部分)
mantissa = 10**(log_p_n - math.floor(log_p_n))
exponent = math.floor(log_p_n)
print(f"      => 實際機率約為: {mantissa:.2f} * 10^{exponent}")
