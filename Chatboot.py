import random
from datetime import datetime
from typing import Dict, List, Optional

class ProfessionalChatbot:
    """
    A professional chatbot implementation with conversation context,
    response templates, and natural language processing capabilities.
    """
    
    def __init__(self):
        self.greetings = ["Hi there!", "Hello!", "Greetings!", "Nice to meet you!"]
        self.farewells = ["Goodbye!", "See you later!", "Have a great day!", "Bye bye!"]
        self.unknown_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more.",
            "I'm still learning. Could you ask me something else?"
        ]
        self.context = {}
        
        # Knowledge base of responses
        self.response_map = {
            "greetings": {
                "triggers": ["hello", "hi", "hey"],
                "responses": self.greetings
            },
            "farewell": {
                "triggers": ["bye", "goodbye", "see you"],
                "responses": self.farewells
            },
            "mood": {
                "triggers": ["how are you", "how's it going"],
                "responses": ["I'm doing well, thanks!", "All systems operational!"]
            },
            "time": {
                "triggers": ["what time is it", "current time"],
                "responses": [f"The current time is {datetime.now().strftime('%H:%M')}"]
            }
        }

    def _get_response_type(self, user_input: str) -> Optional[str]:
        """Determine the type of response needed based on user input."""
        for response_type, data in self.response_map.items():
            if any(trigger in user_input for trigger in data["triggers"]):
                return response_type
        return None

    def _generate_response(self, response_type: str) -> str:
        """Generate an appropriate response based on the determined type."""
        if response_type in self.response_map:
            return random.choice(self.response_map[response_type]["responses"])
        return random.choice(self.unknown_responses)

    def _handle_context(self, user_input: str) -> None:
        """Update conversation context based on user input."""
        # Simple context tracking - could be enhanced with NLP
        if "name" in user_input and "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip()
            self.context["user_name"] = name

    def start_conversation(self):
        """Main conversation loop with the user."""
        print("\n" + "="*50)
        print("Professional Assistant Bot".center(50))
        print("Type 'exit' at any time to end the conversation".center(50))
        print("="*50 + "\n")
        print("Bot: " + random.choice(self.greetings) + " How can I help you today?")

        while True:
            try:
                user_input = input("You: ").strip().lower()
                
                if not user_input:
                    continue
                    
                if "exit" in user_input or "quit" in user_input:
                    print("Bot: " + random.choice(self.farewells))
                    break

                self._handle_context(user_input)
                response_type = self._get_response_type(user_input)
                response = self._generate_response(response_type)
                
                # Personalize response if we know the user's name
                if "user_name" in self.context:
                    response = response.replace("you", self.context["user_name"])
                
                print("Bot:", response)

            except KeyboardInterrupt:
                print("\nBot: " + random.choice(self.farewells))
                break
            except Exception as e:
                print("Bot: I encountered an error. Let's try again.")
                # In production, you would log this error
                continue

if __name__ == "__main__":
    bot = ProfessionalChatbot()
    bot.start_conversation()