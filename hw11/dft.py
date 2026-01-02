import numpy as np

def dft(f):
    """
    實作離散傅立葉正轉換 (Forward DFT)
    X[k] = sum_{n=0}^{N-1} f[n] * exp(-i * 2 * pi * k * n / N)
    """
    N = len(f)
    F = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            # 根據歐拉公式實作指數部分
            angle = -2j * np.pi * k * n / N
            F[k] += f[n] * np.exp(angle)
    return F

def idft(F):
    """
    實作離散傅立葉逆轉換 (Inverse DFT)
    f[n] = (1/N) * sum_{k=0}^{N-1} F[k] * exp(i * 2 * pi * k * n / N)
    註：圖片中連續公式係數為 1/2pi，離散實作慣例通常使用 1/N
    """
    N = len(F)
    f = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            angle = 2j * np.pi * k * n / N
            f[n] += F[k] * np.exp(angle)
    return f / N

# --- 3. 驗證某函數 f ---

# 建立一個測試訊號：例如 f(x) = sin(x) + cos(2x)
x = np.linspace(0, 2*np.pi, 10, endpoint=False)
f_original = np.sin(x) + 0.5 * np.cos(2*x)

# 執行正轉換
F_freq = dft(f_original)

# 執行逆轉換
f_reconstructed = idft(F_freq)

# 驗證結果
print("原始訊號:", np.round(f_original, 4))
print("逆轉換後的訊號:", np.round(f_reconstructed.real, 4))

# 檢查兩者是否足夠接近
is_same = np.allclose(f_original, f_reconstructed.real)
print(f"\n驗證結果：{'成功' if is_same else '失敗'}")
