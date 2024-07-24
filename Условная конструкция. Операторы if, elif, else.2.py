first = input('Ведите первое число')
second = input('Ведите второе число')
third = input('Ведите третье число')
if first == second == third:
    print(3)
if first == second or second == third or first == third:
    print(2)
else:
    print(0)
