def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:  
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": age})
                else:
                    print(f"Пропущено некоректний рядок: {line.strip()}")
        return cats
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# cats_info = get_cats_info("cats_file.txt")
# print(cats_info)
