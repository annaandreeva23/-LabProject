import tabulate

def tabulate_used():  # Робить з даних гарну текстову таблицю
    return tabulate.tabulate([["Illia", 90], ["Oleh", 85]], headers=["name", "mark"])
