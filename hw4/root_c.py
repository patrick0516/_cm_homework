import cmath
import random

def root2(a, b, c):
    d = b**2 - 4*a*c
    r1 = (-b + cmath.sqrt(d)) / (2*a)
    r2 = (-b - cmath.sqrt(d)) / (2*a)
    
    for r in [r1, r2]:
        val = a*r**2 + b*r + c
        print(f"Root: {r}, Valid: {cmath.isclose(val, 0, abs_tol=1e-9)}")
    return r1, r2

def root3(a, b, c, d):
    d0 = b**2 - 3*a*c
    d1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = ((d1 + cmath.sqrt(d1**2 - 4*d0**3)) / 2)**(1/3)
    if C == 0: C = ((d1 - cmath.sqrt(d1**2 - 4*d0**3)) / 2)**(1/3)
    
    u = [1, cmath.exp(2j * cmath.pi / 3), cmath.exp(4j * cmath.pi / 3)]
    roots = [-1/(3*a) * (b + ui*C + d0/(ui*C if C != 0 else 1)) for ui in u]
    
    for r in roots:
        val = a*r**3 + b*r**2 + c*r + d
        print(f"Root: {r}, Valid: {cmath.isclose(val, 0, abs_tol=1e-9)}")
    return roots

def root_n(coeffs):
    def f(x):
        return sum(c * (x**i) for i, c in enumerate(coeffs))

    curr = complex(random.uniform(-10, 10), random.uniform(-10, 10))
    step = 0.1
    for _ in range(100000):
        val = abs(f(curr))
        if val < 1e-10: break
        
        next_step = False
        for dx in [step, -step, step*1j, -step*1j]:
            if abs(f(curr + dx)) < val:
                curr += dx
                next_step = True
                break
        if not next_step: step *= 0.5
    
    print(f"Root: {curr}, Valid: {cmath.isclose(f(curr), 0, abs_tol=1e-9)}")
    return curr

print("--- Quadratic ---")
root2(1, 2, 5)
print("\n--- Cubic ---")
root3(1, -6, 11, -6)
print("\n--- Higher Order (Hill Climbing) ---")
root_n([1, 0, 0, 0, 0, 1]) # x^5 + 1 = 0
