from generate import generate_data
from review import readJSON, writeJSON, reviewData
from converstionParser import parseConvo
import random
import time
import os 

cwd = os.getcwd()
generated_pool = readJSON(f"{cwd}/pool.json")

turns = int(input("Enter the number of conversations you would like: "))

for i in range(turns):

    start = time.time()
    print(f"[ROUND {i+1}/{turns}]: Generating conversation ... ",end="", flush=True)

    convo = generate_data(
        top_p=random.random()/2 + 0.5, 
        temperature=random.random()/2 + 1
    )

    parsed_convo = parseConvo(convo)

    elasped_time = round(time.time() - start, 3)
    print(f"Done in {elasped_time}s", flush=True)

    generated_pool.append(parsed_convo)

print(f"Successfully generated {turns} conversations, saving files")
writeJSON(f"{cwd}/pool.json", generated_pool)


