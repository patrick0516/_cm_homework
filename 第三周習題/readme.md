# 數學原理說明書

## 1️⃣ 直線與圓交點的代數意義

- 直線方程式：  
  \[
  L: ax + by + c = 0
  \]
- 圓方程式：  
  \[
  C: (x-h)^2 + (y-k)^2 = r^2
  \]
- 求交點方法：
  1. 將直線方程代入圓方程，得到一個關於 \(x\) 或 \(y\) 的二次方程：
     \[
     A x^2 + B x + C = 0
     \]
  2. 計算判別式：
     \[
     D = B^2 - 4AC
     \]
  3. 判斷交點數量：
     - \(D > 0\)：兩個不同交點  
     - \(D = 0\)：一個交點（切線）  
     - \(D < 0\)：無交點  

- 代數意義：判別式 \(D\) 反映了直線與圓的相對位置，提供了快速判斷交點數量的方法。

---

## 2️⃣ 垂足與投影的幾何邏輯

- 定義：垂足是點 \(P\) 到直線 \(L\) 上距離最近的點 \(H\)。
- 方法一：向量點積（Dot Product）  
  - 設直線方向向量為 \(\vec{v}\)，則向量 \(\vec{PH}\) 與 \(\vec{v}\) 垂直：  
    \[
    (\vec{H}-\vec{P}) \cdot \vec{v} = 0
    \]
- 方法二：斜率垂直（Slope）  
  - 若直線斜率 \(m_1\)，垂線斜率 \(m_2\) 則滿足：  
    \[
    m_1 \cdot m_2 = -1
    \]
- 運算公式：
  - 若直線為 \(ax + by + c = 0\)，點為 \(P(x_0, y_0)\)，則垂足 \(H(x_h, y_h)\) 為：
    \[
    x_h = x_0 - a \frac{ax_0 + by_0 + c}{a^2 + b^2}, \quad
    y_h = y_0 - b \frac{ax_0 + by_0 + c}{a^2 + b^2}
    \]

---

## 3️⃣ 畢氏定理的驗證原理

- 定義：對直角三角形，三邊長 \(a, b, c\) 滿足：
  \[
  a^2 + b^2 = c^2
  \]
- 在電腦座標系驗證時：
  - 浮點數計算可能出現微小誤差
  - 直接使用 \(a^2 + b^2 == c^2\) 可能失敗
- 解決方法：
  - 設定容許誤差值 \( \varepsilon \)：
    \[
    |a^2 + b^2 - c^2| < \varepsilon
    \]
  - 例如 \(\varepsilon = 10^{-9}\)，即可正確驗證畢氏定理。

---

## 4️⃣ 座標轉換矩陣

### (1) 平移（Translation）

- 向量加法：
  \[
  (x, y) \to (x', y') = (x + dx, \; y + dy)
  \]

### (2) 縮放（Scaling）

- 相對於中心點 \(C(x_c, y_c)\)：
  \[
  (x, y) \to (x', y') = \big(x_c + s(x - x_c), \; y_c + s(y - y_c)\big)
  \]
- 若以原點為中心，則簡化為：
  \[
  (x, y) \to (s x, \; s y)
  \]

### (3) 旋轉（Rotation）

- 旋轉角度 \(\theta\)（逆時針，弧度制），相對中心點 \(C(x_c, y_c)\)：
  1. 平移至原點：
     \[
     x_0 = x - x_c, \quad y_0 = y - y_c
     \]
  2. 旋轉矩陣：
     \[
     \begin{bmatrix}
     x' \\
     y'
     \end{bmatrix}
     =
     \begin{bmatrix}
     \cos\theta & -\sin\theta \\
     \sin\theta & \cos\theta
     \end{bmatrix}
     \begin{bmatrix}
     x_0 \\
     y_0
     \end{bmatrix}
     =
     \begin{bmatrix}
     x_0 \cos\theta - y_0 \sin\theta \\
     x_0 \sin\theta + y_0 \cos\theta
     \end{bmatrix}
     \]
  3. 平移回中心：
     \[
     x' = x_{\text{rot}} + x_c, \quad y' = y_{\text{rot}} + y_c
     \]

- 代數公式可直接套用於點座標，進而應用於線、圓、三角形的幾何變換。

---

