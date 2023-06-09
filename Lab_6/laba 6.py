import math

def calculate_task_score(a, m, b):
    E = (a + 4 * m + b) / 6
    SD = (b - a) / 6
    return E, SD

def calculate_project_interval(tasks):
    project_scores = []
    for task in tasks:
        E, SD = calculate_task_score(*task)
        project_scores.append(E)
    project_mean = sum(project_scores) / len(project_scores)
    project_SD = math.sqrt(sum(sd**2 for sd in project_scores)) / len(project_scores)
    lower_bound = project_mean - 2 * project_SD
    upper_bound = project_mean + 2 * project_SD
    return lower_bound, upper_bound

# Запитуємо користувача про завдання
num_tasks = int(input("Введіть кількість завдань: "))
tasks = []
for i in range(num_tasks):
    print(f"\nЗавдання {i+1}:")
    a = float(input("Оцінка a: "))
    m = float(input("Оцінка m: "))
    b = float(input("Оцінка b: "))
    tasks.append((a, m, b))

# Обчислюємо довірчий інтервал для проекту
lower_bound, upper_bound = calculate_project_interval(tasks)

# Виводимо результати
print(f"\nProject's 95% confidence interval: {lower_bound} ... {upper_bound} points")
