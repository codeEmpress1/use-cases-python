# Document at least 3 use cases of generators

# 1.
# To FIBONACCI SEQUENCE (a sequence of number that starts with 0 and 1 and subsequent numbers are obtained by adding two consequtive numbers)
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

fib_list = [x for x in fibonacci(10)]
print(fib_list)


# 2.
# Using generator comprehension to generate a range of numbers(similar to list comprehension)
def generate(n):
    return(x**x for x in range(n))
mygen = [n for n in generate(10)]
print(mygen)

# 3.
# To read content of a file

def read_file(file_name):
    for row in open(file_name, 'r'):
        yield row

