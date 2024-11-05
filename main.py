import numpy as np

p_elasticity = 0.004
q_elasticity = 2

p = np.array([1, 1.5, 1, 3, 7])
q = np.array([20.1, 19.9, 10, 5, 5])
_ = [ 10*10*1, 2*2*1.5, 8*8*1, 8*8*3, 4*4*7 ]
e_q_scale = np.array([ 1/_[i] for i in range(len(_)) ])
e_p_scale = np.array([ 1/10, 1.5/2, 1/8, 3/8, 7/4 ])

recipe_init = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_low_ore = [ [10.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 4, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_fire = [ [10.0, -3, -8, -8, -4], [-2, 1, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_feast = [ [15.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]
recipe_famine = [ [8.0, -3, -8, -8, -4], [-2, 2, 0, 0, 0], [0, 0, 8, -16, 0], [0, 0, 0, 8, -8], [-1, 0, 0, 0, 4.0] ]

def printVector(s, v):
    print(s, v)
    #v = v.copy().tolist()
    #v = [round(x[0],3) for x in v]
    #print(s, v)

def run(p, q, recipe, num_rounds) :
    R_q = np.array(recipe)
    R_p = R_q.copy().T
    
    for i in range(num_rounds):
        oversupply = R_q.dot(q)
        p = p - p_elasticity * oversupply * e_p_scale
        
        profit = R_p.dot(p)
        q = q + q_elasticity * profit * e_q_scale
        q = q / sum(q) * 60 # 60 agents
        printVector("Num agents: ", q)
        printVector("Price:      ", p)
        input("Round " + str(i) + " Press <Enter>\n")
        
    return p, q

p, q = run(p, q, recipe_init, 50)
print("\n------------ LOW ORE ------------")
p, q = run(p, q, recipe_low_ore, 30)
print("\n------------ INIT ------------")
p, q = run(p, q, recipe_init, 50)
print("\n------------ FIRE ------------")      
p, q = run(p, q, recipe_fire, 30)
print("\n------------ FEAST ------------")
p, q = run(p, q, recipe_feast, 30)
print("\n------------ INIT ------------")
p, q = run(p, q, recipe_init, 1000)
print("\n------------ FAMINE ------------")
p, q = run(p, q, recipe_famine, 30)
print("\n------------ INIT ------------")
p, q = run(p, q, recipe_init, 1000)
