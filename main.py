from generate import generate_data
from review import readJSON, writeJSON, reviewData
from converstionParser import parseConvo, reconstruct
import random
import time
import os 

cwd = os.getcwd()
turns = int(input("Enter the number of conversations you would like: "))
reference_option = "y" == input("Would you like to use references? y/n").lower()
generated_pool = readJSON(f"{cwd}/pool.json")

if (reference_option):
    references_raw = readJSON(f"{cwd}/reference.json")
    references = []

    for convo in references_raw:
        references.append(reconstruct(convo))

for i in range(turns):

    start = time.time()
    print(f"[ROUND {i+1}/{turns}]: Generating conversation ... ",end="", flush=True)

    example = None

    if (reference_option):
        example = references[random.randint(0, len(references)-1)]

    convo = generate_data(
        top_p=random.random()/2 + 0.5, 
        temperature=random.random()/2 + 1,
        reference=example
    )

    parsed_convo = parseConvo(convo)

    elasped_time = round(time.time() - start, 3)
    print(f"Done in {elasped_time}s", flush=True)

    generated_pool.append(parsed_convo)
    writeJSON(f"{cwd}/pool.json", generated_pool)

print(f"Successfully generated {turns} conversations, saving files")
writeJSON(f"{cwd}/pool.json", generated_pool)


