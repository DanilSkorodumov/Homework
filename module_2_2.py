first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and second == third :
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)