# Функція для відкриття файлу
def open_file(filename):
    try:
        file = open(filename, "w")
        print("Файл відкрито")
        return file
    except Exception as e:
        print(f"Не вдалося відкрити файл")
        return None

# Функція для запису рядків у файл
def write_to_file(file):
    file = open_file(filename)
    if file is not None:
        try:

            # (Глумний Тимур КН-33.2)
            file.write("Глумний Тимур КН-33.2\n")
            file.write("Питання 1: Що робити якщо хочеш вивести текст на екран у Python?\n")

