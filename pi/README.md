# PI calculation

### Leibniz formula



```bash
python3 leibniz_pi.py
```


```python
import math

def leibniz_pi(n: int) -> float:
    pi = 0
    for i in range(n):
        term = math.pow(-1, i) / (2 * i + 1)
        pi += term
    pi *= 4
    return pi

print(leibniz_pi(100000))
```

#

### Monte Carlo method


```bash
python3 monte_carlo_pi.py
```


```python
import random
import math

def monte_carlo_pi(n: int) -> float:
    circle_points = 0
    total_points = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            circle_points += 1

        total_points += 1

    return 4 * circle_points / total_points

print(monte_carlo_pi(1000000))
```

#

Also got with animation

<a href="./version0/README.md">Monte Carlo method</a>

<a href="./version1/README.md">Leibniz Formula</a>