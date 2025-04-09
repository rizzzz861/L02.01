numbers = [1, 2, 3, 4, 5]
print(f"Сумма чисел в списке: {sum(numbers)}")

max_number = max(numbers)
print(f"Максимальное число в списке: {max_number}")

numbers_with_duplicates = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Список без дубликатов: {unique_numbers}")
