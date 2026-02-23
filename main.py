def main():
    print("--- Програма для видалення дублікатів зі списку ---")

    try:
        # 1. Введення початкових даних
        user_input = input("Введіть числа через пробіл (наприклад: 1 5 2 1 3 5): ")

        # Перетворюємо введений рядок у список цілих чисел
        my_list = [int(item) for item in user_input.split()]
        print(f"\nПочатковий список: {my_list}")

        # Списки для результатів
        unique_list = []
        removed_duplicates = []  # Список для додаткового завдання

        # 2. Обчислення результату
        for item in my_list:
            if item not in unique_list:
                unique_list.append(item)
            else:
                # ДОДАТКОВЕ ЗАВДАННЯ: якщо елемент вже є, додаємо його до списку дублікатів
                removed_duplicates.append(item)

        # 3. Виведення результату
        print(f"Список без повторень: {unique_list}")

        # Виведення результатів додаткового завдання
        print("\n--- Додаткова статистика ---")
        if len(removed_duplicates) > 0:
            print(f"Усього знайдено та видалено дублікатів: {len(removed_duplicates)}")
            print(f"Видалені елементи: {removed_duplicates}")
        else:
            print("У введеному списку дублікатів не виявлено (всі елементи унікальні).")

    except ValueError:
        print("\nПомилка введення: будь ласка, вводьте лише числа через пробіл.")


if __name__ == "__main__":
    main()