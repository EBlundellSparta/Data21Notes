# Given a list of numbers and some value k, return true if any two numbers from the list add up to k
def problem_1(number_lst, k):
    result = False
    for i in number_lst:
        for j in number_lst:
            if i + j == k:
                result = True
    return result

# The sum of primes below 10 is 2+3+5+7 = 17. Find the sum of all primes below two million
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n < 20:
        ans = False
        for i in range (2, n):
            if n%i == 0:
                ans = False
                break
            else:
                ans = True
        return ans
    elif 20 < n < 100:
        ans = False
        for i in range (2, 20):
            if n%i == 0:
                ans = False
                break
            else:
                ans = True
        return ans
    else:
        ans = False
        for i in range(2, int(n**(1/2)) + 1):
            if n%i == 0:
                ans = False
                break
            else:
                ans = True
        return ans
def prime_list(number):
    lst = []
    for i in range(number + 1):
        if is_prime(i):
            lst.append(i)
    return sum(lst)

# Given an array of integers [n1, n2...] return a new array such that each element at index i 
# of the new array is the product of all the numbers in original array EXCEPT the one at i
def product_array(array: list):
    new_array = []
    for number in array:
        product = 1
        for other_number in array:
            if number == other_number:
                continue
            else:
                product *= other_number
        new_array.append(product)
    return new_array

# Find three Pythagorean numbers (a^2 + b^2 = c^2) such that a + b + c = 1000
def pythag_numbers():
    for a in range(2, 1000):
        for b in range(2, 1000):
            for c in range(2, 1000):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print(a * b * c)

# Given an array of numbers, find smallest positive integer NOT in the array!
def small_pos_int(array: list):
    for i in range(1, 1000000000000000000000000000):
        if i not in array:
            return i 
            break

# Given following constructor pair function, define car function which returns first integer
# and cdr which returns second integer
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair: tuple):
    def return_first(a,b):
        return a
    return pair(return_first)

def cdr(pair: tuple):
    def return_last(a,b):
        return b
    return pair(return_last)

# Given an array of numbers, return largest sum of two non-adjacent numbers i.e. [5,1,1,5] will return 10
def largest_non_adj_sum(array: list):
    previous, largest = 0, 0
    for amount in array:
        print(f"amount: {amount}; previous: {previous}; largest: {largest}")
        previous, largest = largest, max(largest, previous + amount)
        print(f"new_previous: {previous}; new_largest: {largest}")
    return largest

# The series 1^1 + 2^2 +...+10^10 = 10405071317. Find the last ten digits of sum 1^1 + 2^2 +...+ 1000^1000
def self_powers(array: list):
    sum = 0
    for i in array:
        sum += i ** i
    return sum

# Implement an autocomplete system such that given a string and a set of possible outcomes, it will return
# all cases i.e. string 'de' with set [Deer, Dog, Deal] will return [Deer, Dog, Deal]

def autocomplete_str(substring: str, set_words: list):
    emp_lst = []
    for word in set_words:
        if word.lower().startswith(substring.lower()):
            emp_lst.append(word)
    return emp_lst

# Triangle Numbers: 1/2n(n+1) is formula so 1,3,6,10... are all triangle numbers. Using this and text file
# work out how many words are triangle number (converting each letter to it's corresponding alphabetical
# position)

def is_triangle_number(number: int):
    n = 0
    confirmation = False
    while 0 <= n <= 250:
        if n * (n+1) == 2 * number:
            confirmation = True
            break
        else:
            n += 1
    return confirmation

def convert_word_number(word: str):
    num_value = {'"': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
    'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    value = 0
    for letter in word:
        value += num_value[letter.lower()]
    return value

# Find the first four consecutive integers to have four distinct prime factors each. What is the first number?

def prime_factors(number: int):
    number_lst = []
    if is_prime(number):
        number_lst.append(number)
    else:
        current_num = number
        while current_num != 1:
            if is_prime(int(current_num)):
                number_lst.append(int(current_num))
                break
            else:
                for i in range(2, int(current_num/2) + 1):
                    if current_num%i == 0:
                        current_num = current_num/i
                        number_lst.append(int(i))
                        break
    current_factor = 0
    new_lst = []
    for factor in number_lst:
        if current_factor == factor:
            continue
        else:
            current_factor = factor
            if number_lst.count(factor) == 1:
                new_lst.append(f"{factor}")
            else:
                new_lst.append(f"{factor}[{number_lst.count(factor)}]")
    return new_lst

def fib_sequence(n: int):
    x = 1
    y = 2
    fib_lst = [1]
    for i in range(n):
        fib_lst.append(y)
        z = x + y
        x, y = y, z
    return fib_lst[n]

# Given an unordered name list, sort these alphabetically and then return the total score each name will
# receive depending on its position. i.e. 'Colin' in 3rd place will receive a score of 53 * 3 = 159

def name_scores(name_lst: list):
    sorted_name_lst = sorted(name_lst)
    total = 0
    for index in enumerate(sorted_name_lst):
        total += (index[0] + 1) * convert_word_number(index[1])
    return total

def combin_nums(number: str):
    all_combs = []
    for index, digit in enumerate(number):
        if index == 0:
            all_combs.append(digit + number[index + 1:])
        else:
            all_combs.append(digit + number[index + 1:] + number[:index])
    return all_combs

def is_cyclic_number(number: str):
    all_combs = combin_nums(number)
    digit_len = len(number)
    for i in range(digit_len + 1):
        if str(int(number) * i) in all_combs:
            confirmation = True
        else:
            confirmation = False
    return confirmation

leftmost = '00000000137'
i = 0
while i >= 0:
    new_number = leftmost + str(i)
    if new_number.endswith('56789') is False:
        i += 1
    else:
        if is_cyclic_number(new_number):
            print(new_number)
            break
        else:
            i += 1
