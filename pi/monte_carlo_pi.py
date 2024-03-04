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

# Estimate Pi using 1,000,000 points
print(monte_carlo_pi(1000000))