# Ввод данных
X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Введите сумму Майкла: "))
B = int(input("Введите сумму Ивана : "))

# Логика определения возможности инвестирования
if A >= X and B >= X:
  # Оба могут инвестировать
    print(2)  
  # Только Майкл может инвестировать
elif A >= X:
    print("Mike")  
  # Только Иван может инвестировать
elif B >= X:
    print("Ivan")  
elif A + B >= X:
  # Вместе могут инвестировать
    print(1)  
else:
    print(0)  
# Никто не может инвестировать
