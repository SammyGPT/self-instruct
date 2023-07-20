from generate import generate_data
from review import readJSON, writeJSON, reviewData
import random

import os 

cwd = os.getcwd()
# task_pool = readJSON(f"{cwd}/task_pool.json")
generated_pool = []

turns = int(input("Enter the number of conversations you would like: "))

for i in range(turns):
    convo = generate_data(
        top_p=random.random()/2 + 0.5, 
        temperature=random.random()/2 + 1
    )

    parsed_convo = praser(convo)

    print(f"[ROUND {i}]: Generated conversation with {len(parsed_convo)} turns.")

    generated_pool.append(parsed_convo)

print(f"Successfully generated {turns} conversations... saving files ...")
writeJSON(f"{cwd}/pool.json")


