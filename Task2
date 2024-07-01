
word = input("Введите слово из маленьких латинских букв: ")

# Гласные буквы
vowels = 'aeiou'


vowelcounter = 0
consonantcounter = 0

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Счет кол-ва
for letter in word:
    if letter in vowels:
        vowelcounter += 1
        if letter == 'a':
            a_count += 1
        elif letter == 'e':
            e_count += 1
        elif letter == 'i':
            i_count += 1
        elif letter == 'o':
            o_count += 1
        elif letter == 'u':
            u_count += 1
    else:
        consonantcounter += 1

# Ответ
print(f"Количество гласных букв: {vowelcounter}")
print(f"Количество согласных букв: {consonantcounter}")

# Проверка 
if a_count == 0 or e_count == 0 or i_count == 0 or o_count == 0 or u_count == 0:
    print(False)
else:
    print(f"Количество букв 'a': {a_count}")
    print(f"Количество букв 'e': {e_count}")
    print(f"Количество букв 'i': {i_count}")
    print(f"Количество букв 'o': {o_count}")
    print(f"Количество букв 'u': {u_count}")

