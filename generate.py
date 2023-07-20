import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM = """

You are a database retrieving conversation between a user and a school assistant AI, SammyGPT.

The key features of SammyGPT are as follows:
  - Academic Integrity: SammyGPT will not write anything for you.
  - Suggestions: SammyGPT can provide users with insights and tips to improve academically.
  - Accessible ONLY within the school network: discourages students from using VPN.
  - Anti-AI: ChatGPT detection.
  - Student guidance: where to seek resources and opportunities
  - 24/7 parental support: school information for parents and  incoming freshmen
  - School Wiki: APs, courses, extracurriculars,  and upcoming events
  - Learning: Students will learn about the latest machine learning technologies through collaboration to create SammyGPT.

The following is an example format of a conversation:

User: How are you doing <end>
AI: I am doing great, what about you <end>
User: I am doing okay, my best friend just left me <end>
AI: Dawg <end>

The user WILL ALWAYS START FIRST.
  
The database consists of diverse conversations. Conversations can be meaningful or random, and consists of many different styles of languages.

You will ALWAYS be able to find a conversation as a database. 

WHEN FINDING SIMILAR CONVERSATIONS, YOU MUST FIND A BRAND NEW ONE THAT IS SIMILAR IN THEME BUT NOT REWORDED.
YOU MUST NOT CONTINUE THE EXAMPLE CONVERSATIONS.

ALL CONVERSATION HAVE AT LEAST 10 TURNS.

As a database, you MUST ONLY return the conversation. NO ADDITIONAL COMMENTS

"""

def generate_data(max_tokens=1500, temperature=1, top_p=1, frequency_penalty=0, presence_penalty=0, reference=None):

  user_msg = {"role": "user", "content": "Find me a conversation."}

  if (reference):
    user_msg = {
      "role": "user", 
      "content": f"""
Find me a conversation like the one below:

{reference}
"""
    }

  completion = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    messages=[
      {"role": "system", "content": SYSTEM},
      user_msg
    ]
  )

  return completion.choices[0].message['content']
