# 實驗報告：有限體 (Finite Field) 的實作與驗證

本計畫旨在透過 Python 程式語言實作抽象代數中的「有限體」概念，並驗證其是否符合群公理（Group Axioms）與體公理（Field Axioms）。

## 1. AI 對話紀錄分享
在開始實作前，我與 AI 進行了關於有限體定義的探討，包含其數學性質與運算規則。
* **對話連結：** https://chatgpt.com/share/6957106f-0f88-8009-824e-be4ce97162c7

---

## 2. 有限體概念說明

有限體（Finite Field，又稱 Galois Field，記作 $GF(p)$）是一個包含有限個元素的集合，並定義了加法與乘法。一個質數階層的有限體 $GF(p)$ 必須滿足以下特性：

* **加法群 (Additive Group)：** 集合元素在模 $p$ 加法下形成一個交換群，單位元為 $0$。
* **乘法群 (Multiplicative Group)：** 集合中非零元素在模 $p$ 乘法下形成一個交換群，單位元為 $1$。
* **分配律 (Distributivity)：** 乘法對加法符合 $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$。

---

## 3. 程式實作與架構

本實作參考了老師提供的 `field_rational.py` 架構，將邏輯拆解為群運算與物件包裝。

### 核心類別說明
1.  **FiniteFieldAddGroup**: 實作模 $p$ 加法。
2.  **FiniteFieldMulGroup**: 實作模 $p$ 乘法，並利用「費馬小定理」計算乘法反元素：$a^{p-2} \equiv a^{-1} \pmod p$。
3.  **FiniteFieldElement**: 透過 Python 運算子重載（Operator Overloading），讓我們能用 `+`, `-`, `*`, `/` 直接操作有限體元素。

### 驗證過程
* 通過 `group_axioms.py` 檢驗加法與乘法的封閉性、結合律、單位元與反元素。
* 透過 `field_axioms.py` 中的 `check_distributivity()` 函式驗證分配律。

---

## 4. 程式碼範例

```python
# 假設質數 p = 7
a = FiniteFieldElement(3, 7)
b = FiniteFieldElement(5, 7)

print(f"加法: {a} + {b} = {a + b}")  # (3+5) mod 7 = 1
print(f"乘法: {a} * {b} = {a * b}")  # (3*5) mod 7 = 1
print(f"除法: {a} / {b} = {a / b}")  # 3 * (5的逆元) mod 7
