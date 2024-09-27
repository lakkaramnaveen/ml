import numpy as np
import math
import pandas as pd  # It's good practice to import pandas with an alias

def gradient_descent(x, y):
    m_curr = b_curr = 0
    prev_cost = 0
    iterations = 1000000
    n = len(x)
    learning_rate = 0.0002
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * np.sum((y - y_predicted) ** 2)
        md = -(2/n) * np.sum(x * (y - y_predicted))
        bd = -(2/n) * np.sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f"m {m_curr}, b {b_curr}, cost {cost}, iteration {i}")
        if math.isclose(prev_cost, cost, rel_tol=1e-09, abs_tol=0.0):
            print(f"Converged at iteration {i}")
            breakf
        prev_cost = cost

# Read the CSV file using pandas
data = pd.read_csv("test_scores.csv")

# Convert columns to NumPy arrays
x = data['math'].values
y = data['cs'].values

gradient_descent(x, y)
