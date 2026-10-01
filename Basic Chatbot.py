import datetime

def start_chat():
    print("Hello! I am your friendly Python Chatbot.")
    print("You can ask me about the time, my name, or just say 'hi'.")
    print("Type 'quit' or 'bye' to exit the chat.")
    print("-" * 50)
    
    while True:
        # Get input from the user and convert to lowercase for easy matching
        user_input = input("You: ").lower().strip()
        
        # Check for exit commands
        if user_input in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        # Respond based on keywords in the user input
        elif 'hi' in user_input or 'hello' in user_input:
            print("Chatbot: Hi there! How can I help you today?")
            
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a computer program, but I'm doing great! How about you?")
            
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Chatbot: The current time is {current_time}.")
            
        elif 'date' in user_input:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Chatbot: Today's date is {current_date}.")
            
        elif 'name' in user_input:
            print("Chatbot: I am a basic chatbot created by you for the CodeAlpha internship!")
            
        elif 'help' in user_input:
            print("Chatbot: I can chat with you, tell you the time and date, or say hello. Try asking 'what is the time?'.")
            
        else:
            print("Chatbot: I'm sorry, I don't understand that yet. I am still learning!")

# Run the chatbot
if __name__ == "__main__":
    start_chat()