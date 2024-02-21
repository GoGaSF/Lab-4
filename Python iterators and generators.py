
def square_generator(N):
    for i in range(N):
        yield i ** 2

def print_even_numbers(n):
    even_numbers = (str(i) for i in range(n + 1) if i % 2 == 0)
    print(','.join(even_numbers))
def divisible_by_3_and_4(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

if __name__ == "__main__":
    print("Squares up to 10:")
    for square in square_generator(10):
        print(square)

    n = int(input("Enter a number: "))
    print("Even numbers up to", n, "are:")
    print_even_numbers(n)

    start = 0
    end = int(input("Enter the end range: "))
    print("Numbers divisible by 3 and 4 between", start, "and", end, "are:")
    for num in divisible_by_3_and_4(start, end):
        print(num)

    a = 3
    b = 8
    print("Squares from", a, "to", b, "are:")
    for sq in squares(a, b):
        print(sq)

    n = int(input("Enter a number for countdown: "))
    print("Countdown from", n, "to 0:")
    for num in countdown(n):
        print(num, end=' ')
