decimal_number = int(input("Введите десятичное число: "))

binary_number = bin(decimal_number)[2:]
octal_number = oct(decimal_number)[2:]

print(f"Двоичное представление: {binary_number}")
print(f"Восьмиричное представление: {octal_number}")
