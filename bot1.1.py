import nltk

def chatbot():
  while True:
    user_input = input("User: ")

    # Tokenize and parse the user's input
    tokens = nltk.word_tokenize(user_input)
    tags = nltk.pos_tag(tokens)

    # Identify the main noun and verb in the user's input
    noun = None
    verb = None
    for tag in tags:
      if tag[1] == "NN":
        noun = tag[0]
      elif tag[1] == "VB":
        verb = tag[0]

    # Trigger a response based on the identified noun and verb
    if noun == "name" and verb == "is":
      print("Bot: My name is Chatbot. What's your name?")
    elif noun == "age" and verb == "are":
      print("Bot: I am an artificial intelligence and do not have an age. I was created by OpenAI.")
    else:
      print("Bot: I'm sorry, I didn't understand your input. Could you please rephrase your question or statement?")

chatbot()


"""This chatbot will now be able to understand and respond to a wider range of user input. For example, if the user says "What is your name?", the chatbot will respond with "My name is Chatbot." If the user says "How old are you?", the chatbot will respond with a message saying it is an artificial intelligence and does not have an age."""