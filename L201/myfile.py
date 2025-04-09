with open("example.txt", "w") as file:
    file.write("Hello, File!")

with open("example.txt", "r") as file:
    print(file.read())

with open("example.txt", "a") as file:
    file.write("\nДобавленная строка.")
