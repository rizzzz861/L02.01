try:
    num = int(input("Введите число: "))
except ValueError:
    print("Это не число!")

try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!")
