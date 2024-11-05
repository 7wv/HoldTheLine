import numpy as np

step_size = 0.1 # in (0,1]; if more than 1, it will diverge
p_elasticity = 0.004
q_elasticity = 2

p = np.array([1, 1.5, 1, 3, 7])
n = np.array([20.1, 19.9, 10, 5, 5])
num_agents = n.sum()
_ = [ 10*10*1, 2*2*1.5, 8*8*1, 8*8*3, 4*4*7 ]
e_q_scale = np.array([ 1/_[i] for i in range(len(_)) ])
e_p_scale = np.array([ 1/10, 1.5/2, 1/8, 3/8, 7/4 ])

recipe_init = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_low_ore = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 6, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_fire = [ [10.0, -3, -8, -8, -4], [-2, 1, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_feast = [ [15.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_famine = [ [8.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]

def run(p, n, recipe, num_rounds) :
    R_n = np.array(recipe)
    R_p = R_n.copy().T
    agent_prod = R_n.diagonal()
    
    for round in range(num_rounds):
        #print(R_n)
        #print(n)
        #print(R_n.dot(n))
        oversupply = R_n.dot(n)
        percent_change = oversupply / agent_prod / n
        # print('n', n)
        # print('p', p)
        print('oversupply', oversupply)
        #print('agent_prod', agent_prod)
        # print('percent_change', percent_change)
        #print('% * ss', percent_change * step_size)
        #print('1- % * ss', 1 - percent_change * step_size)
        p = p * (1 - percent_change * step_size)
        #####n = n * (1 + percent_change * step_size)
        #print('unnormal n', n)
        #####n = n / n.sum() * num_agents
        #print('n', n)
        #print('p', p)
        #print("-"*10)

        profit = R_p.dot(p)
        percent_change = profit / agent_prod / p
        #print('n', n)
        #print('p', p)
        print('profit', profit)
        #print('percent_change', percent_change)
        #print('% * ss', percent_change * step_size)
        #print('1- % * ss', 1 - percent_change * step_size)
        #####p = p * (1 - percent_change * step_size)
        n = n * (1 + percent_change * step_size)
        #print('unnormal n', n)
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
