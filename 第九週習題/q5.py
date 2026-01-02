def hamming_74():
    data = [1, 1, 0, 1]
    d1, d2, d3, d4 = data
    
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    encoded = [p1, p2, d1, p3, d2, d3, d4]
    print(f"\n【題五】7-4 漢明碼實作：")
    print(f"      原始資料: {data}")
    print(f"      編碼後結果: {encoded}")

    received = encoded.copy()
    error_index = 4 # 修改索引 4 (即第 5 位)
    received[error_index] ^= 1 
    print(f"      收到資料 (含錯): {received}")

    s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
    s3 = received[3] ^ received[4] ^ received[5] ^ received[6]
    
    error_pos = s1 * 1 + s2 * 2 + s3 * 4 
    
    if error_pos != 0:
        print(f"      偵測到錯誤！位置在第 {error_pos} 位，正在修正...")
        received[error_pos - 1] ^= 1 # 修正錯誤
        
    final_data = [received[2], received[4], received[5], received[6]]
    print(f"      糾錯後解碼結果: {final_data}")

hamming_74()
