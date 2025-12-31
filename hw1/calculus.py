def df(f, x, h=0.00001):
    return (f(x + h) - f(x - h)) / (2 * h)

def integral(f, a, b, n=1000):
    h = (b - a) / n
    area = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        area += f(a + i * h)
    return area * h

def theorem1(f, x):
    g = lambda x_val: integral(f, 0, x_val)
    
    derivative_of_integral = df(g, x)
    
    target_value = f(x)
    
    print(f"G'({x}) = {derivative_of_integral:.6f}")
    print(f"f({x})  = {target_value:.6f}")
    
    assert abs(derivative_of_integral - target_value) < 0.001
    print("驗證成功！")

test_f = lambda x: x**2
theorem1(test_f, 3)
