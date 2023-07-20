import json

def reviewData(data):
    file = open("reviewPrompts.json", "w")
    file.write(json.dumps(data))
    file.close()
    print("Please manually review the 'reviewPrompts.json' file. Type continue after you have finished reviewing.")
    while (not input() == "continue"):
        pass
    with open('reviewPrompts.json', 'r') as f:
        data = json.load(f)
        return data
    
if __name__ == "__main__":
    reviewData({})