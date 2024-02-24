'''  У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії.
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Наприклад:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
Вимоги до завдання:
Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
Рекомендації для виконання:
Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.
Критерії оцінювання:
Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.
Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
Очікуваний результат:
Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000   
'''
'''
 
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total_salary = 0

        for line in lines:
            name, salary_str = line.strip().split(',')
            salary = int(salary_str)
            total_salary += salary

        num_developers = len(lines)
        average_salary = total_salary / num_developers

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

# Приклад використання
total, average = total_salary("path/to/salary_file.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")   
'''

'''    Результат виконання програми: 
Помилка: Файл 'path/to/salary_file.txt' не знайдено.
Traceback (most recent call last):
  File "d:\Projects\Python-HW4\hw4-1.py", line 52, in <module>
    total, average = total_salary("path/to/salary_file.txt")  
TypeError: cannot unpack non-iterable NoneType object 

Важливо врахувати, що цей код передбачає, що дані у файлі завжди будуть коректними (прізвище та заробітна плата завжди вказані, розділені комою).
Якщо дані можуть бути некоректними, можливо, вам слід розглянути додаткову обробку винятків для неправильного формату рядків у файлі. '''


