# Basic Chatbot
# CodeAlpha Python Programming Internship - Task 4

def chatbot():
    print("🤖 ChatBot: Hello! I am your simple Python chatbot.")
    print("🤖 ChatBot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("ChatBot: Hi! How are you? 😊")

        elif user_input == "how are you":
            print("ChatBot: I'm fine, thanks! How about you?")

        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a great day! 👋")
            break

        else:
            print("ChatBot: Sorry, I don't understand that.")


# Start the chatbot
chatbot()