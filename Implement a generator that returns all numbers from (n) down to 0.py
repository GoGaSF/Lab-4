def countdown(n):
    while n >= 0:
        yield n
        n -= 1
def main():
    try:
        n = int(input("Введите число n: "))
        print(f"Числа от {n} до 0:")
        for number in countdown(n):
            print(number, end=" ")
    except ValueError:
        print("Ошибка: Введите целое число.")

if __name__ == "__main__":
    main()
