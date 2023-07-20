def parseConvo(data):
    messages = data.split("<end>")
    for i, message in enumerate(messages):
        message = message.replace("User:", "")
        message = message.replace("AI:", "")
        message = message.replace("\n", "")
        messages[i] = message.strip()
    messages.pop()
    return messages

def reconstruct(data):
    prompt = ""

    for i, line in enumerate(data):
        if (i%2 == 0):
            prompt += f"User: {line} <end>\n"
        else:
            prompt += f"AI: {line} <end>\n"
    
    return prompt

if __name__ == "__main__":
    parseConvo('hi')