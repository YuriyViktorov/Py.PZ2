# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
print('Здравствуйте! Я, Катя сестра Пети.')
print('Я отгадю задуманные числа.')
S = abs(int(input('Введите сумму чисел: ')))
P = abs(int(input('Введите произведение чисел ')))

y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print('Задуманные числа:',x1,' и ',y1)