def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input("Введите число n: "))
        if n < 0:
            print("Число должно быть неотрицательным.")
            return
        even_numbers = even_numbers_generator(n)
        print("Четные числа от 0 до", n, ":", end=" ")
        for num in even_numbers:
            print(num, end=", " if num < n - 1 else "\n")
    except ValueError:
        print("Ошибка: Введите целое число.")

if __name__ == "__main__":
    main()
