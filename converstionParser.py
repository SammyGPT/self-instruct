def parseConvo(data):
    messages = data.split("<end>")
    for i, message in enumerate(messages):
        message = message.replace("User:", "")
        message = message.replace("AI:", "")
        message = message.replace("\n", "")
        messages[i] = message.strip()
    messages.pop()
    return messages
    
if __name__ == "__main__":
    parseConvo('hi')