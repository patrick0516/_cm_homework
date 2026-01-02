class FiniteFieldElement:
    def __init__(self, value: int, p: int):
        if p <= 1:
            raise ValueError("p must be a prime number > 1")
        self.p = p
        self.value = value % p

    def __repr__(self):
        return f"{self.value} (mod {self.p})"

    def _check(self, other):
        if not isinstance(other, FiniteFieldElement):
            raise TypeError("Operand must be FiniteFieldElement")
        if self.p != other.p:
            raise ValueError("Different finite fields")

    def __add__(self, other):
        self._check(other)
        return FiniteFieldElement(self.value + other.value, self.p)

    def __sub__(self, other):
        self._check(other)
        return FiniteFieldElement(self.value - other.value, self.p)

    def __mul__(self, other):
        self._check(other)
        return FiniteFieldElement(self.value * other.value, self.p)

    def __truediv__(self, other):
        self._check(other)
        if other.value == 0:
            raise ZeroDivisionError("Division by zero in finite field")
        inv = pow(other.value, self.p - 2, self.p)  # Fermat's little theorem
        return FiniteFieldElement(self.value * inv, self.p)


# Example usage in GF(7)
a = FiniteFieldElement(3, 7)
b = FiniteFieldElement(5, 7)
c = FiniteFieldElement(2, 7)

print(a + b)  # 1 (mod 7)
print(a / c)  # 5 (mod 7)
