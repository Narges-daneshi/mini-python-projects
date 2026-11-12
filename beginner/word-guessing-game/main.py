import random
words=["python","Banana","java","apple","kotlin"]
word=random.choice(words)
word=word.lower()

print("Welcome to Word Guessing Game!")
print("I have selected a word.")
print(f"The word has {len(word)} letters.")
print("Word: ",end="")

choices=["_" for char in word]
for choice in choices:
    print(choice,end=" ")
print()
right_choice=[]
wrong_choice=[]
guessed_letters=set()
all_guesses=[]

attempts=6
while attempts>0:
    attempt=input("Enter a letter: ")
    attempt=attempt.lower()


    # Validate user input
    if len(attempt)!=1 or not ("a"<= attempt <="z"):
        print("Your choice must be one English letter.")
        continue


    # Check for duplicate guesses
    if attempt in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(attempt)
    all_guesses.append(attempt)


    # Handle correct guesses
    if attempt in word:
        for index,char in enumerate(word):
            if char==attempt:
                choices[index] = attempt
        right_choice.append(attempt)
        print("Good guess!")
        print("Word: ", end="")
        for choice in choices:
            print(choice, end=" ")
        print()
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print()

    # Handle incorrect guesses
    else:
        attempts -= 1
        wrong_choice.append(attempt)
        print("Wrong guess!")
        print(f"Remaining attempts: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print()




    if "".join(choices) == word:
        break


# Display final results
if "".join(choices) == word:
    print("Congratulations! 🎉")
    print(f"You guessed the word: {word}")
    print(f"Total guesses: {len(all_guesses)}")


else:
    print("Game Over!")
    print(f"The correct word was: {word}")


print(f"Right guesses: {len(right_choice)}")
print(f"Wrong guesses: {len(wrong_choice)}")


