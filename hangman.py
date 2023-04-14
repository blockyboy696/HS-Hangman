import random


def draw_line(word: str, guess: str, letter: str) -> str:
    a = -1
    b = []
    guess = list(guess)
    for i in word:
        if i == letter:
            a += 1
            b.append(a)
        else:
            a += 1
    for i in b:
        guess[i] = letter
    guess = ''.join(guess)
    return guess


def game():
    global wins
    global loses
    all_words = ('python', 'java', 'swift', 'javascript')
    word = random.choice(all_words)
    attempts = 8
    guessed_word = '-' * len(word)
    guessed_letters = []
    while attempts != 0:
        if word == guessed_word:
            break
        guess_letter = input(f"\n{guessed_word}\nInput a letter:")
        true_letters = set(word)
        if len(guess_letter) != 1:
            print('Please, input a single letter')
        elif guess_letter.isalpha() is False or guess_letter.islower() is False:
            print('Please, enter a lowercase letter from the English alphabet.')
        elif guess_letter in guessed_letters:
            print('You\'ve already guessed this letter')
        elif guess_letter not in true_letters:
            attempts -= 1
            print('That letter doesn\'t appear in the word.')
        else:
            guessed_word = draw_line(word, guessed_word, guess_letter)
        guessed_letters.append(guess_letter)

    if word == guessed_word:
        print(f'You guessed the word {word}!\nYou survived!')
        wins += 1
        mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if mode == 'play':
            game()
        elif mode == 'results':
            print(f'You won: {wins} times, and how many games they lost, e.g. You lost: {loses} times')
            mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
            if mode == 'play':
                game()
            else:
                pass
        else:
            pass
    else:
        print('You lost!')
        loses +=1
        mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if mode == 'play':
            game()
        elif mode == 'results':
            print(f'You won: {wins} times, and how many games they lost, e.g. You lost: {loses} times')
            mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
            if mode == 'play':
                game()
            else:
                pass
        else:
            pass


print('H A N G M A N')
wins = 0
loses = 0
mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
if mode == 'play':
    game()
elif mode == 'results':
    print(f'You won: {wins} times, and how many games they lost, e.g. You lost: {loses} times')
    mode = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if mode == 'play':
        game()
    else:
        pass
else:
    pass