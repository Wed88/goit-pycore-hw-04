def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0)  

        average = total / count  
        return (total, average)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)
    except ValueError:
        print("Файл містить некоректні дані.")
        return (0, 0)

# total, average = total_salary("salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
