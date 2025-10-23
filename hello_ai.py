# hello_ai.py
# oliver omulando
# CSCI 130 - week 1 project
# Date:[10/23/2025]


import random

import datetime


def greetings_agent():

    ""

# get current time
current_hour= datetime.datetime.now().hour

# Determine time of day
if current_hour< 12:
    time_period = "morning"
elif current_hour< 17:
    time_period = "afternoon" 
else:
    time_period = "evening"

# Get user's name

name = input("what's your name?")

# Generate personalized greetings

greetings = [
    f"Good {time_period},{name}! welcome to AI class",
    f"Hello{name}! Hope you're having a great{time_period}!",
    f"Hi{name}! Ready to learn AI this {time_period}?"
]

#select and display random greetings

print(random.choice(greetings))

# simple conversation

mood = input("\n How are you feeling about learning AI?")

#Simple response based on keywords(reflex agents behavior)

if "excited" in mood.lower() or "good" in mood.lower():
    print("That's wonderfull! Your enthusiaasm will help you learn")
elif "nervous" in mood.lower() or "worried" in mood.lower():
    print("Dont worry! We'll take it step by step")
elif "unsure" in mood.lower() or "undecided" in mood.lower():
    print(" It's ok to be unsure its a lot to learn")
else:
    print("thanks for sharing! Let's make this a great learning experince")

# Display an AI fact

ai_facts= [
    "Did you know? The term 'Artificial Intellingence' was coined in 1956!",
    "Fun fact: your smartphone uses AI for face recorgnition",
    "AI insight: Netflix uses AI to recommend shows you might like!",
    "Did you know? AI helps doctors detect diseases earlier!",
    "AI can be trained to recognize emotions by analyzing facial expressions",
    "AI can contribute to human crerativity rather than replace it"
    
]

print(f"\n{random.choice(ai_facts)}")
print("\nLet's start our AI journey together")

# Run the program

if __name__ == "__main__": 

 print("=" * 50)
 print("welcome to CSCI 130: Introduction to AI")
 print("=" * 50)
 print()
 greetings_agent()