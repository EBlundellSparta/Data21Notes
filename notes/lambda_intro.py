# def addition(num1, num2):
#     return num1 + num2
#
# Instead of using a function, like above, we could use lambda i.e.
# add = lambda num1, num2: num1 + num2
#
# Both print statements below will give the same result
# print(addition(2, 3))
# print(add(2, 3))
#
# Example 1: Using lambda with lists
# savings = [234, 555, 674, 78]
# bonus = list(map(lambda x: x * 1.1, savings))
#
# Example 2:
# numbers = [i + 1 for i in range(10)]
# numbers_sqr = list(map(lambda x: x * x, numbers))
#
# Example 3: Using lambda with strings
# full_name = lambda first, last: f"Full name: {first.capitalize()} {last.capitalize()}"
# print(full_name("john", "smith"))
#
# Example 4: Lambda function inside a lambda function
# high_order_func = lambda x, func: x + func(x)
# print(high_order_func(2, lambda x: x * (x + 1))) -- Result is 8
