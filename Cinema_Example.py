name = input("Please input your name: ")
age = input("Please input your age as an integer: ")

while name.isalpha() is False:
    name = input("This is an invalid name, please type again (for example Ed):  ")

while age.isnumeric() is False:
    age = input("This is an invalid age, please type your age as an integer (for example 20 "
                "if you're twenty year's old):  ")

if int(age) < 12:
    supervised = input("Are you alone?  ")
    yes = ['yes', 'y', 'yep', 'yess', 'indeed', 'yeah']
    no = ['no', 'nope', 'naa', 'n', 'noo']
    while supervised.lower() not in yes and supervised.lower() not in no:
        supervised = input("Please type yes or no:  ")
    if supervised.lower() in yes:
        print(f"Hello {name.capitalize()}, you can go and see any PG or U or 12A films "
            f"provided that's fine with whoever is supervising you.")
    else:
        print(f"Sorry {name.capitalize()}, you are too young and cannot see any films :(")
elif 12 <= int(age) < 15:
    print(f"Thank you {name.capitalize()}, you can only see films rated up to 12A")
elif 15 <= int(age) < 18:
    print(f"Thank you {name.capitalize()}, you can only see films rated up to 15")
else:
    print(f"Congratulations {name.capitalize()}, you are officially an adult, good luck! "
            f"But the good news is you can see whichever film you want!")
print("Hope you have a lovely day!")
