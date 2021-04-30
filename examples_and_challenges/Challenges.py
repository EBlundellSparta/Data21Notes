# ISOGRAM TASK
# isogram = input("Please choose a word:  ")
# empty_string = ""
#
# for letter in isogram:
#     if letter in [" ", "_", "-"]:
#         empty_string += letter
#     elif letter not in empty_string:
#         empty_string += letter
#     elif letter in empty_string and not in [" ", "_", "-"]:
#         print("Your word is not an isogram")

# FIZZ BUZZ TASK
# a = int(input("Please choose a number to go up to:  "))
#
# for number in range(a):
#     if number == 0:
#         print(number)
#     elif number % 5 == 0 and number % 3 == 0:
#         print('fizzbuzz')
#     elif number % 3 == 0:
#         print('fizz')
#     elif number % 5 == 0:
#         print('buzz')
#     else:
#         print(number)

# TURN ABOVE INTO FUNCTIONS

# Multiples of 3 and 5
# def sum_multiples_three_and_five(number_limit):
#     count = 0
#     for number in range(number_limit):
#         if number % 3 == 0 or number % 5 == 0:
#             count += number
#     return count

# Sum of even-numbered terms in the fib sequence
# def fib_sequence(number_limit):
#     first_term = 1
#     second_term = 2
#     fib_lst = [first_term, second_term]
#     for n in range(number_limit - 2):
#         if first_term + second_term >= 4000000:
#             break
#         else:
#             next_term = first_term + second_term
#             fib_lst.append(next_term)
#             first_term, second_term = second_term, next_term
#     even_terms = 0
#     for i in fib_lst:
#         if i % 2 == 0:
#             even_terms += i
#     print(fib_lst)
#     print(even_terms)

# Prime factors of number
# def prime(number):
#     prime = True
#     if number > 1:
#         for j in range(2, int(number ** 0.5) + 1):
#             if number % j == 0:
#                 prime = False
#                 break
#     return prime
#
#
# def prime_factor(number):
#     factor_lst = []
#     prime_lst = []
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             factor_lst.append(i)
#     for j in factor_lst:
#         if prime(j):
#             print(j)
#             prime_lst.append(j)
#     print(max(prime_lst))

# Palindrome number from 3 digit product
# def palindrome_number():
#     list_1 = [i + 1 for i in range(999)]
#     list_2 = [j + 1 for j in range(999)]
#     multiply_set = set()
#     for i in list_1:
#         for j in list_2:
#             multiply_set.add(i * j)
#     multiply_list = list(multiply_set)
#     palin_list = []
#     for i in multiply_list:
#         if str(i)[0:3] == str(i)[-1:2:-1]:
#             palin_list.append(i)
#     print(max(palin_list))

# Smallest multiple of a particular range
# def no_remainders(number_range):
#     all_multiples = set()
#     num_list = [i + 1 for i in range(number_range)]
#     divisor = [i + 1 for i in range(20)]
#     for i in num_list:
#         for j in divisor:
#             # if i % 2 == 0 and \
#             #     i % 3 == 0 and \
#             #     i % 4 == 0 and \
#             #     i % 5 == 0 and \
#             #     i % 6 == 0 and \
#             #     i % 7 == 0 and \
#             #     i % 8 == 0 and \
#             #     i % 9 == 0 and \
#             #     i % 10 == 0:
#             #     all_multiples.add(i)
#             if j == 20:
#                 all_multiples.add(i)
#             elif i % j == 0:
#                 continue
#             else:
#                 break
#
#     print(min(all_multiples))