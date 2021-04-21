example = "My phrase is this"


def hidden_phrase(word: str):
    hid_phr = ""
    for letter in word:
        if letter != " ":
            hid_phr += "_"
        else:
            hid_phr += "/"
    return hid_phr


def letter_index(letter: str):
    if example.count(letter) > 1:
        j = 0
        for i in range(example.count(letter)):
            pos_i = example.find(letter, j, -1)
            j = pos_i + 1
            return pos_i
    else:
        position = example.find(letter)
        return position


def replace_letter(letter: str):
    new_phr = hidden_phrase(example)[1].replace("_", letter)
    return


def check_letter(letter: str):
    count = 0
    if letter in example:
        letter_index(letter)
    else:
        count += 1

print(replace_letter('y'))