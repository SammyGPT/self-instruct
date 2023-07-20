from generate import generate_data
from review import readJSON, reviewData
import random

import os 

cwd = os.getcwd()
task_pool = readJSON(f"{cwd}/task_pool.json")

turns = int(input("Enter the number of conversations you would like: "))

for i in range(turns):
    convo = generate_data(
        top_p=random.random()/2 + 0.5, 
        temperature=random.random()/2 + 1
    )
    

