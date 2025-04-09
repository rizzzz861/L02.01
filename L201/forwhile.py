for i in range(1, 11):
    print(i)

N = int(input("Введите число N: "))
for i in range(1, N + 1):
    print(i)

sum_numbers = 0
i = 1
while i <= 100:
    sum_numbers += i
    i += 1
print(f"Сумма чисел от 1 до 100: {sum_numbers}")
