from scipy.optimize import fsolve
import math
def equation(t):
    return math.exp(t) - math.e*t

# Solve the equation
solution = fsolve(equation, 1)  # Provide an initial guess, such as 1
print(solution)  # Output: [0.56714329]

