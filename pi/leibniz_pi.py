import math

def leibniz_pi(n: int) -> float:
    pi = 0
    for i in range(n):
        term = math.pow(-1, i) / (2 * i + 1)
        pi += term
    pi *= 4
    return pi

# Calculate Pi up to 100,000 terms
print(leibniz_pi(100000))