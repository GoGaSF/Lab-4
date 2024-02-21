def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
def main():
    try:
        a = int(input("Введите начальное число a: "))
        b = int(input("Введите конечное число b: "))
        if a > b:
            print("Ошибка: Начальное число должно быть меньше или равно конечному числу.")
            return
        print(f"Квадраты чисел от {a} до {b}:")
        for square in squares(a, b):
            print(square)
    except ValueError:
        print("Ошибка: Введите целые числа.")

if __name__ == "__main__":
    main()
