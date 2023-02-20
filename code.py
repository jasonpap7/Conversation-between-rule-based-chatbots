# Import necessary libraries
import random

# Define a list of default greetings that the chatbots can use
greetings = ["hello", 
             "hi", 
             "how are you", 
             "what's up", 
             "hey", 
             "good morning", 
             "good afternoon", 
             "good evening"]

# Define a list of default responses that the chatbots can use
responses = ["I'm good, thanks for asking.",
             "I'm fine, how are you?",
             "Not much, just hanging out here.",
             "I'm doing well, how about you?",
             "I'm not sure, what do you think?",
             "I can't really say for sure.",
             "I'm just a chatbot, I don't have feelings or opinions.",
             "Tell me a joke",
             "What's the weather like?",
             "What are your feelings?"]

# Define a list of goodbye messages that the chatbots can use
goodbyes = ["Bye",
            "bye",
            "goodbye",
            "Goodbye"]

# Define a list of default questions that the chatbots can ask
questions = ["What's your favorite color?",
             "What's your favorite food?",
             "What do you like to do in your free time?",
             "Do you have any hobbies?",
             "Do you have any pets?",
             "Do you have any siblings?",
             "Do you like to travel?",
             "What do you like to do for fun?"]

# Define a list of answers to questions that the chatbots can use
answers = ["My name is Chatbot",
           "I have no age I am a Bot",
           "I come from the Internet",
           "I like chatting",
           "My favorite color is red",
           "I don't have a favorite food, as I don't eat",
           "My hobby is chatting"]

# Define a function that responds to a user's message
def respond_to(message, bot_name):
    # If the message is a greeting, choose a random greeting from the list to respond with
    if message.lower() in greetings:
        # Should enter a counter and a clause for the first two lines of the conversation only
        return random.choice(greetings + responses) 
    # If the message is a goodbye, choose a random goodbye from the list to respond with
    elif message.lower() in goodbyes:
        return random.choice(goodbyes)
    # If the message is a question, choose a random answer from the list to respond with
    elif message.lower() in questions:
        return random.choice(answers)
    # If the message contains the word "feelings", respond with a default message about feelings
    elif "feelings" in message.lower():
        return "As a chatbot, I don't have those."
    # If the message contains the word "weather", respond with a default message about the weather
    elif "weather" in message.lower():
        return "I'm sorry, I don't have access to this information. I'm just a chatbot, not such a service."
    # If the message contains the word "joke", respond with a random joke from the list of jokes
    elif "joke" in message.lower():
        jokes = ["Why was the math book sad? Because it had too many problems.",
                 "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
                 "Why was the computer cold? Because it left its Windows open."]
        return random.choice(jokes)
    # If the message is not a greeting or a goodbye or doesn't contain any recognized keywords, 
    # choose a random response or question from the list to respond with
    else:
        return random.choice(responses + questions + goodbyes)

# Define the names of the two chatbots
bot1_name = "Chatbot1"
bot2_name = "Chatbot2"

# Define a function that simulates the conversation between two chatbots
def chatbot_conversation(bot1_name, bot2_name):
    # Print a welcome message
    #print("Wellcome this programm simulates a conversation. That conversation is betweem two chatbots.")
    print(f"Wellcome to a conversation between {bot1_name} and {bot2_name}.")
    print("Do you want the coversation to begin ? [1/0]")
    p = input()
    if p == "1" :
        print("\nThis is a conversation between two chatbots. Chatbot1 starts the conversation:\n")

        #bot2_response = random.choice(greetings + responses)
        bot2_response = random.choice(greetings)
        while True:
            
            # Respond to bot2's message with bot1
            bot1_response = respond_to(bot2_response, bot1_name)
            print(f"{bot1_name}: {bot1_response}")
            # Check if bot1's response is a goodbye message, and if so, end the conversation
            if bot1_response in goodbyes:
                bot2_goodbye = random.choice(goodbyes)
                print(f"{bot2_name}: {bot2_goodbye}")
                break
            # Respond to bot1's message with bot2
            bot2_response = respond_to(bot1_response, bot2_name)
            print(f"{bot2_name}: {bot2_response}")
            # Check if bot2's response is a goodbye message, and if so, end the conversation
            if bot2_response in goodbyes:
                bot1_goodbye = random.choice(goodbyes)
                print(f"{bot1_name}: {bot1_goodbye}")
                break
    
        # End of conversation
        print("\nEnd of Conversation.")

    elif p == "0" :
        print ("Okey, Goodbye!")
    else :
        print("Wrong typing. Run the programm again!")


# Start the chatbot conversation
chatbot_conversation("Chatbot1", "Chatbot2")


 