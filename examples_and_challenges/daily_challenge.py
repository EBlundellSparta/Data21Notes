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

# If p is the perimeter of a right angle triangle with lengths {a,b,c} there are exactly 3 solutions
# for p = 120. For which value of p <= 1000 is the number maximised?

def num_solutions_int_rt(perimeter: int):
    num_sols = 0
    for c in range(int((3*perimeter)/5)):
        for b in range(c):
            for a in range(b):
                if a**2 + b**2 == c**2 and a + b + c == perimeter:
                    num_sols += 1
    return num_sols

p = 0 
number_solutions = 0
for i in range(499, 1001):
    if i%2!=0:
        continue
    else:
        print(i)
        if num_solutions_int_rt(i) >= number_solutions:
            number_solutions = num_solutions_int_rt(i)
            p = i
            print(p, number_solutions)
