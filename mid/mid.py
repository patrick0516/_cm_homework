import random
import math
import time

def basel_pi_estimation(n):
    """
    利用巴塞爾問題級數估算 PI
    公式: sum(1/n^2) = (pi^2) / 6
    """
    start_time = time.time()
    sum_val = 0
    for i in range(1, n + 1):
        sum_val += 1 / (i**2)
    
    estimate = math.sqrt(sum_val * 6)
    duration = time.time() - start_time
    return estimate, duration

def monte_carlo_pi_estimation(n):
    """
    利用蒙地卡羅法估算 PI
    原理: 單位圓與外切正方形的面積比
    """
    start_time = time.time()
    hits = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            hits += 1
            
    estimate = (hits / n) * 4
    duration = time.time() - start_time
    return estimate, duration

def run_experiment():
    # 測試規模：十萬次迭代
    iterations = 1000000
    
    print(f"--- 運算實驗開始 (迭代次數: {iterations}) ---")
    
    # 執行巴塞爾級數法
    pi_b, time_b = basel_pi_estimation(iterations)
    error_b = abs(pi_b - math.pi)
    
    # 執行蒙地卡羅法
    pi_m, time_m = monte_carlo_pi_estimation(iterations)
    error_m = abs(pi_m - math.pi)
    
    # 輸出結果
    print(f"{'演算法':<15} | {'估算值':<12} | {'絕對誤差':<12} | {'執行時間(s)':<10}")
    print("-" * 60)
    print(f"{'Basel Series':<15} | {pi_b:.10f} | {error_b:.10f} | {time_b:.4f}")
    print(f"{'Monte Carlo':<15} | {pi_m:.10f} | {error_m:.10f} | {time_m:.4f}")
    print("-" * 60)
    print(f"標準 Math.pi 值: {math.pi:.10f}")

if __name__ == "__main__":
    run_experiment()
