import random


class EnhancedChatBot:
    def __init__(self):
        self.intent_patterns = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening'],
            'inquire_name': ['what is your name', 'who are you', 'your name'],
            'weather_query': ['what is the weather', 'how is the weather today', 'tell me the weather'],
            'farewell': ['goodbye', 'bye', 'see you later', 'take care'],
            'ask_time': ['what time is it', 'current time', 'tell me the time'],
            'ask_date': ['what is the date today', 'current date', 'tell me the date'],
            'ask_for_help': ['help', 'what can you do', 'commands'],
            'fallback': ['I don\'t understand', 'pardon', 'sorry, what', 'can you repeat', 'i didn\'t get that']
        }

        self.intent_responses = {
            'greeting': ['Hello! How can I assist you today?', 'Hi there! What can I do for you?',
                         'Hey! Need any help?'],
            'inquire_name': ['I am your friendly chatbot!', 'You can call me ChatBuddy.'],
            'weather_query': ['I wish I could tell you the weather, but I\'m not connected to the internet.',
                              'Weather is unpredictable without internet access!'],
            'farewell': ['Goodbye! Hope to talk to you soon.', 'Bye! Have a wonderful day!', 'See you later!'],
            'ask_time': ['I don\'t have a watch, but you can check your device!',
                         'Sorry, I don\'t have the ability to tell the time.'],
            'ask_date': ['I can\'t tell the date, but your device surely knows!', 'I\'m not aware of the date, sorry!'],
            'ask_for_help': [
                'You can ask me about the weather, time, date, or just have a chat!',
                'I can assist with basic questions like greetings, weather, and more. Try asking me!',
                'Feel free to ask about my name, the weather, or just chat with me.'
            ],
            'fallback': [
                'I\'m not sure I understood that. Could you try asking differently?',
                'Hmm, I didn\'t quite catch that. Could you rephrase?',
                'I\'m not quite sure what you mean. Can you clarify?',
                'I don\'t have an answer for that right now, but I\'m here to chat!'
            ]
        }

        self.user_name = None

    def generate_response(self, user_message):
        user_message = user_message.lower()

        if self.user_name is None and ('my name is' in user_message or 'i am' in user_message):
            self.user_name = user_message.split()[-1].capitalize()
            return f"Nice to meet you, {self.user_name}! How can I assist you today?"

        for intent, triggers in self.intent_patterns.items():
            if any(trigger in user_message for trigger in triggers):
                response = random.choice(self.intent_responses[intent])
                return response if self.user_name is None else response.replace('!', f', {self.user_name}!')

        return random.choice(self.intent_responses['fallback'])

    def start_chat(self):
        print(random.choice([
            "Welcome to ChatBot! How can I help you today?",
            "Hello there! Ready to chat with me?",
            "Hi! I'm here to assist you. Ask me anything!"
        ]))
        print("(Type 'exit' to end the conversation or 'help' to see what I can do.)")


if __name__ == "__main__":
    chatbot = EnhancedChatBot()
    chatbot.start_chat()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.generate_response(user_input)
        print("Chatbot:", response)
