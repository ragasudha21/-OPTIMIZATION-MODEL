# Import libraries
from pulp import LpMaximize, LpProblem, LpVariable, value

# Create the LP problem
model = LpProblem("Maximize_Profit", LpMaximize)

# Define decision variables
P1 = LpVariable("P1", lowBound=0, cat='Continuous')
P2 = LpVariable("P2", lowBound=0, cat='Continuous')

# Objective function: Maximize profit
model += 40 * P1 + 50 * P2, "Total_Profit"

# Constraints
model += 2 * P1 + 1 * P2 <= 100, "Machine_M1_Time"
model += 1 * P1 + 3 * P2 <= 120, "Machine_M2_Time"

# Solve the problem
model.solve()

# Results
print("Status:", model.status)
print(f"Produce {P1.varValue:.2f} units of P1")
print(f"Produce {P2.varValue:.2f} units of P2")
print(f"Maximum Profit: ${value(model.objective):.2f}")