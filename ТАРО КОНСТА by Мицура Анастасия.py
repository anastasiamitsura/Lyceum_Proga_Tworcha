import random
import os
import time
import sys

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR = True
except:
    COLOR = False



# утилы

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow(text, delay=0.02):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def glitch_text(text): # психологический хорорр
    symbols = ['@', '#', '$', '%', '&', '?', '▓', '▒']
    result = ""
    for ch in text:
        if random.random() < 0.08:
            result += random.choice(symbols)
        else:
            result += ch
    return result



# Арканы

arcana = {
    "Маг": {
        "power": 2,
        "art": r"""
┌────────────────────┐
│        МАГ         │
│        ✨           │
│     \  |  /        │
│      \ | /         │
│    ---  *  ---      │
│      / | \         │
│     /  |  \        │
└────────────────────┘
"""
    },

    "Солнце": {
        "power": 3,
        "art": r"""
┌────────────────────┐
│      СОЛНЦЕ ☀      │
│     \  |  /        │
│   --   ☼   --      │
│     /  |  \        │
│                    │
│   Ты шаришь        │
└────────────────────┘
"""
    },

    "Башня": {
        "power": -2,
        "art": r"""
┌────────────────────┐
│       БАШНЯ        │
│        /\          │
│       /  \         │
│      |    | ⚡      │
│      |    |         │
│      |____|         │
└────────────────────┘
"""
    },

    "Дьявол": {
        "power": -3,
        "art": r"""
┌────────────────────┐
│       ДЬЯВОЛ       │
│      ( ͡° ͜ʖ ͡°)    │
│        /|\          │
│        / \          │
│     3 часа сна     │
└────────────────────┘
"""
    },

    "Отшельник": {
        "power": -1,
        "art": r"""
┌────────────────────┐
│     ОТШЕЛЬНИК      │
│        🚶          │
│       /|\          │
│       / \          │
│  АЭАЭАЭАЭАЭААЭ     │
└────────────────────┘
"""
    },

    "Мир": {
        "power": 3,
        "art": r"""
┌────────────────────┐
│        МИР         │
│     \  🌍  /       │
│      \     /        │
│       \   /         │
│      Это прайм      │
└────────────────────┘
"""
    }
}



# логика

def draw_spread():
    chosen = random.sample(list(arcana.keys()), 3)
    result = []

    for name in chosen:
        reversed_card = random.choice([True, False])
        power = arcana[name]["power"]
        if reversed_card:
            power = -power

        result.append({
            "name": name,
            "power": power,
            "reversed": reversed_card,
            "art": arcana[name]["art"]
        })

    return result


def calculate_score(cards):
    base = 3
    total = base + sum(c["power"] for c in cards)
    chaos = random.randint(-1, 1)
    total += chaos

    return max(0, min(5, total))


def glitch_effect():
    for _ in range(8):
        clear()
        print(glitch_text("!!! СИСТЕМА ОБНАРУЖИЛА 3 ПЛОХИХ АРКАНА !!!"))
        time.sleep(0.15)



# игра


def game():
    clear()
    slow("Карты пробуждаются...")
    time.sleep(1)

    cards = draw_spread()

    bad_cards = 0

    for card in cards:
        print()
        art = card["art"]

        if card["reversed"]:
            art = art[::-1]  # переворот карты

        print(art)

        if card["power"] < 0:
            bad_cards += 1

        time.sleep(1)

    if bad_cards == 3:
        glitch_effect()
        slow(glitch_text("ЗАЧЕМ ТЫ СПИСЫВАЛ"), 0.03)

    score = calculate_score(cards)

    print("\nВычисление судьбы...")
    time.sleep(2)

    if bad_cards == 3:
        score = max(0, score - 1)

    print("\n★ ИТОГОВАЯ ОЦЕНКА:", score, "★")

    if score == 5:
        print("ДААААААААА")
    elif score == 4:
        print("Мог бы и лучше, позор")
    elif score == 3:
        print("Ну ты как всегда")
    elif score == 2:
        print("Пересдача так пересдача")
    elif score == 1:
        print("А ведь ты готовился...")
    else:
        print("☠ Система сломалась.")

    print("\nEnter — снова | exit — выйти")
    return input("> ").strip().lower() != "exit"


def main():
    while game():
        pass
    clear()
    print("Сессия завершена.")


if __name__ == "__main__":
    main()