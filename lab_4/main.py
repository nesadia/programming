while True:
    file_path = input("Введіть шлях до файлу: ")

    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_lines = len(lines)
        empty_lines = 0
        lines_with_z = 0
        total_z_count = 0
        lines_with_and = 0

        for line in lines:
            line = line.strip()
            if not line:
                empty_lines += 1
            else:
                if 'z' in line.lower():
                    lines_with_z += 1
                    total_z_count += line.lower().count('z')

                if 'and' in line.lower():
                    lines_with_and += 1

        print("Кількість рядків: ", total_lines)
        print("Кількість порожніх рядків: ", empty_lines)
        print("Кількість рядків з літерою 'z': ", lines_with_z)
        print("Кількість літер 'z' у файлі: ", total_z_count)
        print("Кількість рядків з групою символів 'and': ", lines_with_and)

    another_file = input("Хочете проаналізувати ще один файл? (Так/Ні): ")
    if another_file.lower() != 'так':
        break
