import numpy as np

step_size = 0.1 # in (0,1]; if more than 1, it will diverge
p_elasticity = 0.004
q_elasticity = 2

p = np.array([1, 1.5, 1, 3, 7])
n = np.array([20.1, 19.9, 10, 5, 5])
num_agents = n.sum()

recipe_init = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_low_ore = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 6, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_fire = [ [10.0, -3, -8, -8, -4], [-2, 1, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_feast = [ [15.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_famine = [ [8.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]

def step_along_curve(R, x, slope_sign) :
    extra = R.dot(x) # profit per agent or extra total goods
    percent_change = extra / R.diagonal() / x # scale by agent_prod
    slope = slope_sign * percent_change * step_size
    # equalize up and down to be same ratios and return
    return [1+y if y >= 0 else 1/(1-y) for y in slope]
    
def run(p, n, recipe, num_rounds) :
    R_n = np.array(recipe)
    R_p = R_n.copy().T
    
    for round in range(num_rounds):
        p = p * step_along_curve(R_n, n, -1)
        n = n * step_along_curve(R_p, p, +1)
        n = n / n.sum() * num_agents
        print("Num agents: ", n)
        print("Price:      ", p)
        print("-"*10)
        input("Round " + str(round) + " Press <Enter>\n")
        
    return p, n

p, n = run(p, n, recipe_init, 5)
print("\n------------ LOW ORE ------------")
p, n = run(p, n, recipe_low_ore, 100)
print("\n------------ INIT ------------")
p, n = run(p, n, recipe_init, 1000)
print("\n------------ FIRE ------------")      
p, n = run(p, n, recipe_fire, 30)
print("\n------------ FEAST ------------")
p, n = run(p, n, recipe_feast, 30)
print("\n------------ INIT ------------")
p, n = run(p, n, recipe_init, 1000)
print("\n------------ FAMINE ------------")
p, n = run(p, n, recipe_famine, 30)
print("\n------------ INIT ------------")
p, n = run(p, n, recipe_init, 1000)
