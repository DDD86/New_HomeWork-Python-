# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2 
# 5 6 -> 2 3

s = int(input("Введите сумму x и y: "))
p = int(input("Введите произведение x и y: "))

found = False  # Флаг для обозначения, найдены ли значения x и y

for x in range(1, s):
    y = s - x
    if x * y == p:
        found = True
        break

if found:
    print(f"x и y равны: {x}, {y}")
else:
    print("Невозможно найти подходящие значения x и y.")
