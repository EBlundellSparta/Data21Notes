def hidden_phrase(word: str):
    hid_phr = ""
    for letter in word:
        if letter != " ":
            hid_phr += "_"
        else:
            hid_phr += "/"
    return hid_phr


def letter_index(phrase, letter):
    indexes = []
    start = 0
    while True:
        i = phrase.find(letter, start)
        if i == -1:
            break
        else:
            indexes.append(i)
            start = i + 1
    return indexes


def replace_letter(phrase, replace, letter, hidden_word):
    whole_phr = phrase
    let_ind = letter_index(hidden_word, letter.lower())
    for n in let_ind:
        new_phr = whole_phr[:n] + letter + whole_phr[n+1:]
        whole_phr = new_phr
    return whole_phr


def play_a_game():
    player_1 = input("Whoever is deciding the phrase, please type in your name:  ")
    player_2 = input("Whoever is guessing, please type in your name:  ")
    sec_word = input(f"{player_1.capitalize()}, please type in your secret phrase:  ")
    sec_word_view = hidden_phrase(sec_word.lower())
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to hangman, here is the phrase/word "
          f"{player_1.capitalize()} has inputted\n{sec_word_view}")
    already_guessed = set()
    count = 0
    guess = input(f"{player_2.capitalize()}, please choose a letter to guess:  ")
    while count < 8:
        if guess.isalpha() is False:
            print(f"{player_2.capitalize()} this is an invalid character, please choose a letter:  ")
        else:
            if guess not in already_guessed:
                already_guessed.add(guess)
                print(already_guessed)
                if guess in sec_word:
                    sec_word_view = replace_letter(sec_word_view, '_', guess, sec_word)
                    print(sec_word_view)
                    if sec_word_view.replace('/', "") == sec_word.replace(" ", ""):
                        print(f"{player_2.capitalize()} has won and guessed the phrase, which is "
                              f"{sec_word.capitalize()}")
                        break
                    else:
                        guess = input(f"{player_2.capitalize()} please choose another letter to guess:  ")
                else:
                    count += 1
                    print("This is wrong, you have ", str(8 - count), " more guesses")
                    guess = input(f"{player_2.capitalize()} please choose another letter to guess:  ")
            else:
                guess = input("You've already guessed this, please choose another letter:  ")

    if count == 8:
        print(f"{player_1.capitalize()} has won, unfortunately {player_2.capitalize()} didn't guess "
              f"the word, which was '{sec_word.capitalize()}'")
    nxt_game = input("Do you want to play again (y/n):  ")
    if nxt_game.lower() == 'y':
        play_a_game()
    else:
        print("Hope you have a lovely day")


play_a_game()