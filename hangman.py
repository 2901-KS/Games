import random

def hangman():
    word_list = ['python', 'java', 'javascript', 'html', 'css', 'ruby', 'cplusplus']
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6
    word_display = ['_'] * len(word)

    print("Welcome to Hangman!")
    
    while attempts > 0 and '_' in word_display:
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Using try-except to handle invalid inputs
        try:
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue
            
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue
            
            guessed_letters.append(guess)

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_display[i] = guess
                print(f"Good guess!")
            else:
                attempts -= 1
                print(f"Wrong guess! The letter {guess} is not in the word.")
        
        except Exception as e:
            print(f"Error: {e}")
            continue

    if '_' not in word_display:
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

# Call the hangman function to play the game
hangman()
