# This is a chat program using Furhat empowered by chatgpt
# Prerequisite
# 1. pip install furhat_remote_api
# 2. pip install openai
# 3. Enable remote API on the furhat head
# 4. copy and paste your openai api key in between the quotation marks in line 28
# 5. run this command: python main.py
# 6. Press Enter to continue
# 7. Say "mission complete" to stop the program after running it
# Notice: wait until the robot finishes the word, then press Enter to continue and talk


import os
from openai import OpenAI
import openai

from furhat_remote_api import FurhatRemoteAPI

def query_chatgpt(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo", # you can change the model to use here
    messages=[{"role": "user", "content": prompt}])

    return completion

if __name__ == "__main__":
    # initialize the openai envvironment

    openai_api_key = "" # paste open api key here
    client = OpenAI(api_key=openai_api_key)

    # Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
    # furhat = FurhatRemoteAPI("localhost")
    furhat = FurhatRemoteAPI("192.168.2.164")

    # Get the voices on the robot
    voices = furhat.get_voices()

    # Set the voice of the robot
    furhat.set_voice(name='Matthew')

    # Say "Hi there!"
    furhat.say(text="Hi there! I am your chatbot enhanced by ChatGPT. How can I help you? Please press Enter to continue.")
    input("Press Enter to continue...")
    # TODO: make a function that the loop will not repeat until furhat finishes its speech

    # Start chat
    while True:
        print("Furhat is listening...")
        result = furhat.listen()
        if result.message == "mission complete":
            furhat.say(text="See you next time!")
            break
        if result.message == "":
            continue

        print("I am saying:", result.message)

        PROMPT = result.message

        response = query_chatgpt(PROMPT)

        reply_chatgpt = response.choices[0].message.content
        print("ChatGPT:", reply_chatgpt)
        furhat.say(text=reply_chatgpt)

        input("Press Enter to continue...")
        # TODO: make a function that the loop will not repeat until furhat finishes its speech