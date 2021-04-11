def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


print(even_or_odd(-15))


# another variation in the code
# number % 2 will return 0 for even numbers and 1 for odd ones.
# 0 evaluates to False and 1 to True, so we can do it with one line

"""return 'odd' if number % 2 else 'even'"""

# another variation in the code

"""return ["even","odd"][number % 2]"""