print("Починає гру")

count_actions = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0
}

dics_of_actions = {
    "1": "Вибрати інвентар",
    "2": "Вибрати випадковий предмет",
    "4": "Змінити налаштування випадкового предмета",
    "3": "Переглянути налаштування",
    "0": "Вийти з гри"
}

name = input("Введіть своє ім'я: ")

print(f"{name}, тобі доступні наступні дії:")
for key, value in dics_of_actions.items():
    print(f"{key}: {value}")


while True:
    action = input("Виберіть дію зі списку: ")
    print(f"{name}, Ви обрали дію: {action}")
    if action == "0":
        break

    if action not in dics_of_actions.keys():
        print("Ви обрали неправильну дію, спробуйте ще раз")
        continue

    if action == "1":
        print(f"{name}, Ви обрали інвентар")
        count_actions["1"] += 1
    elif action == "2":
        print(f"{name}, Ви обрали випадковий предмет")
        count_actions["2"] += 1
    elif action == "3":
        print(f"{name}, Ви обрали переглянути налаштування")
        count_actions["3"] += 1
    elif action == "4":
        print(f"{name}, Ви обрали змінити налаштування випадкового предмета")
        count_actions["4"] += 1

    print("Статистика дій:")
    for key, value in count_actions.items():
        print(f"Дія {key}: {value} разів")

print("Гра завершена")
