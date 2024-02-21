def numbers_divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num
def main():
    try:
        n = int(input("Введите число n: "))
        if n < 0:
            print("Число должно быть неотрицательным.")
            return
        print("Числа, делящиеся на 3 и 4 от 0 до", n, ":", end=" ")
        for num in numbers_divisible_by_3_and_4(n):
            print(num, end=", " if num < n else "\n")
    except ValueError:
        print("Ошибка: Введите целое число.")

if __name__ == "__main__":
    main()
