import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        print("Некоректні параметри. Повертаю пустий список.")
        return []

    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(minimum, maximum))

    result = sorted(list(unique_numbers))
    return result

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Лотерейні числа:", lottery_numbers)
