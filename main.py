import utils

words = {}

print("Проверим ваш уровень английского языка?")
ask_level = input("Выберите один из 3х уровней сложности:"
                  "\n-легкий\n-средний\n-тяжелый\n").strip().lower()

"""Получите у пользователя уровень сложности"""
if ask_level == "легкий":
    words = utils.words_easy
elif ask_level == "средний":
    words = utils.words_medium
elif ask_level == "тяжелый":
    words = utils.words_hard
else:
    words = utils.words_easy

answers = {}

"""Запустите цикл по пяти словам из словаря words."""
for key, value in words.items():
    print("Угадайте слово".center(40, "*"))
    asking = input(f"{key}, {len(value)} букв, начинается на "
                   f"{value[0]}...\n").strip().lower()

    if asking == value:
        answers[key] = True
        print(f"Верно, {key} — это {asking}.")
    else:
        answers[key] = False
        print(f"Неверно. {key} — это {value}.")

print()
correct_answers = 0
right_answers = []
wrong_answers = []

for k, v in answers.items():
    if v is True:
        right_answers.append(k)
        correct_answers += 1
    elif v is False:
        wrong_answers.append(k)

print("Правильно отвечены слова:")
for rights in right_answers:
    print(rights)
print()

print("Неправильно отвечены слова:")
for wrongs in wrong_answers:
    print(wrongs)
print()

print(f"Ваш ранг:\n{utils.levels.get(correct_answers)}")