def parseConvo():
    data = getFile()
    messages = data.split("<end>")
    for i, message in enumerate(messages):
        message = message.replace("User:", "")
        message = message.replace("AI:", "")
        message = message.replace("\n", "")
        messages[i] = message.strip()
    messages.pop()
    return messages
    
def getFile():
    with open("text.txt", 'r') as f:
        data = f.read()
        return str(data)
    
parseConvo()