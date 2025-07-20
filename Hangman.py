import random

class HangmanGame:
        
    def __init__(self):
       
        self.words = ["python", "codealpha", "internship", "hangman", "programming"]
        self.word = random.choice(self.words).lower()
        self.guessed_letters = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts
        self.game_over = False
        
    def display_current_state(self):
        
        display = [letter if letter in self.guessed_letters else '_' for letter in self.word]
        return ' '.join(display)
    
    def process_guess(self, letter):
        
        letter = letter.lower()
        
        if letter in self.guessed_letters:
            print(f"You've already guessed '{letter}'. Try a different letter.")
            return None
            
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            print(f"Correct! '{letter}' is in the word.")
            return True
        else:
            self.remaining_attempts -= 1
            print(f"Sorry, '{letter}' is not in the word. Attempts remaining: {self.remaining_attempts}")
            return False
    
    def check_win_condition(self):
        
        return all(letter in self.guessed_letters for letter in self.word)
    
    def play(self): 
        
        print("Welcome to Hangman!")
        print("Guess the word by entering one letter at a time.")
        print(f"You have {self.max_attempts} incorrect attempts allowed.\n")
        
        while not self.game_over and self.remaining_attempts > 0:
            print(f"\nWord: {self.display_current_state()}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
            
            try:
                guess = input("Enter your guess (a single letter): ").lower()
                
                if len(guess) != 1 or not guess.isalpha():
                    print("Please enter a single alphabetical character.")
                    continue
                    
                self.process_guess(guess)
                
                if self.check_win_condition():
                    print(f"\nCongratulations! You've guessed the word: {self.word}")
                    self.game_over = True
                    
            except KeyboardInterrupt:
                print("\nGame exited by user.")
                return
                
        if not self.game_over:
            print(f"\nGame over! The word was: {self.word}")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()