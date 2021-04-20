name = input("Please input your name. ")
age = input("Please input your age as an integer. ")

while age.isnumeric() is False:
    print("This is an invalid age, please try again")
    age = input("Type your age as an integer.  ")

if age.isnumeric():
    if int(age) < 12:
        supervised = input("Are you alone?  ")
        if supervised.lower() == "yes":
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