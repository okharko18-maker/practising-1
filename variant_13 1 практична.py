"""
Практична робота: Базові типи даних та умовні конструкції.
Варіант 13. Аналізатор часу.
"""

def solve(time_str: str) -> str:
    if len(time_str) != 5 or time_str[2] != ":":
        return "Помилка: некоректний час"

    if not (time_str[:2].isdigit() and time_str[3:].isdigit()):
        return "Помилка: некоректний час"

    hours = int(time_str[:2])
    minutes = int(time_str[3:])

    if hours > 23 or minutes > 59:
        return "Помилка: некоректний час"

    if hours < 6:
        part = "Ніч"
    elif hours < 12:
        part = "Ранок"
    elif hours < 18:
        part = "День"
    else:
        part = "Вечір"

    minutes_to_midnight = 1440 - (hours * 60 + minutes)

    return f"Частина доби: {part}, Хвилин до півночі: {minutes_to_midnight}"


if __name__ == "__main__":
    time_str = input("Введіть час у форматі ГГ:ХХ: ")
    print(solve(time_str))
 

if __name__ == "__main__":
    t = input("Введіть час (ГГ:ХХ): ")
    print(solve(t))
