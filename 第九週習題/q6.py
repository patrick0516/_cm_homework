def shannon_limit(bandwidth, snr_db):
    """
    計算夏農-哈特利定理的信道容量
    C = B * log2(1 + S/N)
    """
    # SNR(dB) 轉為 線性比例 S/N
    snr_linear = 10 ** (snr_db / 10)
    capacity = bandwidth * math.log2(1 + snr_linear)
    return capacity

print(f"\n【題六】夏農-哈特利定理應用：")
print(f"      在頻寬 3000Hz, 30dB SNR 下，信道極限容量為: {shannon_limit(3000, 30):.2f} bps")
