while True:
    expression = input("Введите арифметическое выражение (или 'exit' для выхода): ")
    if expression.lower() == "exit":
        break
    try:
        result = eval(expression)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
