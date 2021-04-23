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
    for n in [letter_index(hidden_word, letter)]:
        new_phr = whole_phr[:n] + letter + whole_phr[n+1:]
        whole_phr = new_phr
        return whole_phr

test = "my name is ed"
print(letter_index(test, 'e'))
#print(replace_letter('__/____/__/__', '_', 'e', test))
#
# def play_a_game():
#     player_1 = input("Whoever is deciding the phrase, please type in your name:  ")
#     player_2 = input("Whoever is guessing, please type in your name:  ")
#     sec_word = input(f"{player_1.capitalize()}, please type in your secret phrase:  ")
#     sec_word_view = hidden_phrase(sec_word)
#     print(sec_word_view)
#     already_guessed = set()
#     count = 0
#     while count < 8:
#         guess = input(f"{player_2.capitalize()}, please choose a letter to guess:  ")
#         if sec_word_view.strip('/') == sec_word.strip(" "):
#             print(f"{player_2.capitalize()} has won and guessed the word, which is {sec_word}")
#             break
#         elif guess in already_guessed:
#             guess = input(print("You've already guessed this, please choose another letter:  "))
#         else:
#             already_guessed.add(guess)
#             print(already_guessed)
#             if guess in sec_word:
#                 sec_word_view = replace_letter(sec_word_view, '_', guess, sec_word)
#                 print(sec_word_view)
#             else:
#                 count += 1
#                 print("This is wrong, you have ", str(8 - count), " more guesses")
#     if count == 8:
#         print(f"{player_1.capitalize()} has won, unfortunately {player_2.capitalize()} didn't guess "
#               f"the word, which was {sec_word}")
#     nxt_game = input(print("Do you want to play again (y/n):  "))
#     if nxt_game.lower() == 'y':
#         play_a_game()
#     else:
#         print("Hope you have a lovely day")
#
# play_a_game()