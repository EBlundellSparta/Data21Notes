# OPENING FILES
def open_and_print_file(file="order.txt"):
    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print("There has been an error opening this file!")
        print(errmsg)
    finally:
        print("Done!")
#
#
# open_and_print_file("order.txt")

# APPENDING TO FILES
def write_to_file(order_item, file="order.txt"):
    try:
        with open(file, "a") as opened_file:
                [opened_file.write(item + "\n") for item in order_item]
    except FileNotFoundError:
        print("File can't be found")
    except FileExistsError:
        print("File already exists")
    except ValueError:
        print("Cannot update file")


write_to_file(["Cheese", "Yoghurt", "Apples", "Grapes"])
open_and_print_file()