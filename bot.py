import re

def chatbot():
  while True:
    user_input = input("User: ")

    # Greeting
    greeting_pattern = re.compile(r'^(hi|hello|hey)$', re.I)
    if greeting_pattern.match(user_input):
      print("Bot: Hello! How can I help you today?")
      continue

    # Farewell
    farewell_pattern = re.compile(r'^(bye|goodbye|see ya)$', re.I)
    if farewell_pattern.match(user_input):
      print("Bot: Good bye! Have a great day.")
      break

    # How are you
    how_are_you_pattern = re.compile(r'^(how are you|how are ya)$', re.I)
    if how_are_you_pattern.match(user_input):
      print("Bot: I'm doing well, thank you! How are you?")
      continue

    # What is your name
    name_pattern = re.compile(r'^(what is your name|what\'s your name)$', re.I)
    if name_pattern.match(user_input):
      print("Bot: My name is Chatbot. What's your name?")
      continue

    # How old are you
    age_pattern = re.compile(r'^(how old are you|what is your age)$', re.I)
    if age_pattern.match(user_input):
      print("Bot: I am an artificial intelligence and do not have an age. I was created by OpenAI.")
      continue

    # Default response
    print("Bot: I'm sorry, I didn't understand your input. Could you please rephrase your question or statement?")

chatbot()

"""This chatbot will now respond to the user asking "what is your name" or "what's your name" with a message saying its name is Chatbot and asking the user for their name. It will also respond to the user asking "how old are you" or "what is your age" with a message saying it is an artificial intelligence and does not have an age.""""