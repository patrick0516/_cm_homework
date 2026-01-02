import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x:.3f}, {self.y:.3f})"

    def dist_to(self, other):
        """計算兩點間距離"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Line:
    """使用一般式 ax + by + c = 0 定義直線"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_points(cls, p1, p2):
        """透過兩點建立直線"""
        a = p1.y - p2.y
        b = p2.x - p1.x
        c = p1.x * p2.y - p2.x * p1.y
        return cls(a, b, c)

class Circle:
    def __init__(self, center, r):
        self.center = center
        self.r = r

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def __repr__(self):
        return f"Triangle{self.points}"

# --- 核心運算函數 (對應作業 2, 3) ---

def intersect_lines(l1, l2):
    """計算兩直線交點 (Cramer's Rule)"""
    det = l1.a * l2.b - l2.a * l1.b
    if math.isclose(det, 0): return [] # 平行
    x = (l1.b * l2.c - l2.b * l1.c) / det
    y = (l1.c * l2.a - l2.c * l1.a) / det
    return [Point(x, y)]

def get_foot(p, l):
    """計算點 p 到直線 l 的垂足 (對應作業 3)"""
    # 公式: H = P - (a*x0 + b*y0 + c)/(a^2 + b^2) * (a, b)
    proj = (l.a * p.x + l.b * p.y + l.c) / (l.a**2 + l.b**2)
    return Point(p.x - l.a * proj, p.y - l.b * proj)

# --- 幾何變換邏輯 (對應作業 6) ---

def transform(obj, mode, **kwargs):
    """
    通用變換函數：支援 Point, Triangle
    mode: 'translate', 'rotate', 'scale'
    """
    if isinstance(obj, Triangle):
        return Triangle(*[transform(p, mode, **kwargs) for p in obj.points])
    
    x, y = obj.x, obj.y
    if mode == 'translate':
        return Point(x + kwargs.get('dx', 0), y + kwargs.get('dy', 0))
    
    elif mode == 'rotate':
        angle = math.radians(kwargs.get('angle', 0))
        cx, cy = kwargs.get('center', Point(0,0)).x, kwargs.get('center', Point(0,0)).y
        # 旋轉矩陣公式
        nx = (x - cx) * math.cos(angle) - (y - cy) * math.sin(angle) + cx
        ny = (x - cx) * math.sin(angle) + (y - cy) * math.cos(angle) + cy
        return Point(nx, ny)
    
    elif mode == 'scale':
        f = kwargs.get('factor', 1)
        cx, cy = kwargs.get('center', Point(0,0)).x, kwargs.get('center', Point(0,0)).y
        return Point(cx + (x - cx) * f, cy + (y - cy) * f)

# --- 驗證與示範 (對應作業 4, 5) ---

def run_homework_demo():
    print("=== 作業 3 & 4: 垂足與畢氏定理驗證 ===")
    l = Line.from_points(Point(0, 0), Point(10, 0)) # x軸
    p_off = Point(5, 5) # 線外一點
    foot = get_foot(p_off, l)
    on_line = Point(0, 0) # 直線上另一點
    
    # 計算邊長
    a = p_off.dist_to(foot)    # 垂直邊
    b = on_line.dist_to(foot)  # 底邊
    c = p_off.dist_to(on_line) # 斜邊
    
    print(f"線外點: {p_off}, 垂足: {foot}")
    print(f"驗證 a^2({a**2:.1f}) + b^2({b**2:.1f}) = c^2({c**2:.1f})")
    print(f"結果: {math.isclose(a**2 + b**2, c**2)}")

    print("\n=== 作業 5 & 6: 三角形變換示範 ===")
    tri = Triangle(Point(0,0), Point(2,0), Point(0,2))
    print(f"原始三角形: {tri}")
    
    # 旋轉 90 度並平移
    tri_rotated = transform(tri, 'rotate', angle=90, center=Point(0,0))
    tri_final = transform(tri_rotated, 'translate', dx=5, dy=5)
    print(f"旋轉90度並平移(+5,+5)後: {tri_final}")

if __name__ == "__main__":
    run_homework_demo()
