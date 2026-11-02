products = [
    {"name": "Нюдова помада", "price": 220.00, "quantity": 15},
    {"name": "Туш для вій", "price": 310.50, "quantity": 10},
    {"name": "Зволожувальний крем", "price": 450.00, "quantity": 8},
    {"name": "Сяючий блиск", "price": 190.00, "quantity": 12}
]
cart = {}
password = "6767"
price_format = lambda x: f"{x:.2f}грн"

def catalog():
    print("\n🌸 --- НАШІ ТОВАРИ --- 🌸")
    i = 1
    for p in products:
        print(f"{i}. {p['name']} — {price_format(p['price'])} (в наявності: {p['quantity']} шт.)")
        i = i + 1

def add():
    catalog()
    n = int(input("Оберіть номер товару: ")) - 1
    if 0 <= n < len(products):
        if n in cart:
            in_cart = cart[n]
        else:
            in_cart = 0
        if in_cart < products[n]["quantity"]:
            cart[n] = in_cart + 1
            print("Красу додано в кошик! ✨")
        else:
            print("На жаль, більше немає в наявності.")
    else:
        print("Ой, такого номера немає.")

def show_cart():
    if len(cart) == 0:
        print("\nВаш кошик поки що порожній 🛍️")
        return
    print("\n🛍️ --- ВАШ КОШИК --- 🛍️")
    total = 0
    for n in cart:
        qty = cart[n]
        cost = products[n]["price"] * qty
        total = total + cost
        print(f"{products[n]['name']} x{qty} — {price_format(cost)}")
    print("Сума замовлення:", price_format(total))

def remove():
    show_cart()
    if len(cart) > 0:
        n = int(input("Номер товару для видалення: ")) - 1
        if n in cart:
            del cart[n]
            print("Товар прибрано з кошика!")
        else:
            print("Цього товару немає у вашому кошику.")

def buy():
    if len(cart) == 0:
        print("\nКошик порожній, оберіть щось із товарів 💕")
        return
    show_cart()
    for n in cart:
        qty = cart[n]
        products[n]["quantity"] = products[n]["quantity"] - qty
    cart.clear()
    print("Дякуємо за замовлення! Оплата пройшла успішно 💖")

def admin():
    pwd = input("Введіть пароль: ")
    if pwd == password:
        print("\n🔐 --- КІЛЬКІСТЬ В НАЯВНОСТІ ---")
        for p in products:
            print(f"{p['name']} — залишилось {p['quantity']} шт.")
    else:
        print("Невірний пароль!")

def main():
    while True:
        print("\n✨ === ГОЛОВНЕ МЕНЮ === ✨")
        print("1. Переглянути каталог товарів")
        print("2. Додати товар в кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари з кошика")
        print("6. Увійти як адміністратор")
        print("0. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            catalog()
        elif choice == "2":
            add()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            remove()
        elif choice == "5":
            buy()
        elif choice == "6":
            admin()
        elif choice == "0":
            print("Гарного дня! Чекаємо вас знову 🌸")
            break
        else:
            print("Невірна команда, спробуйте ще раз.")

if __name__ == "__main__":
    main()
# Кінець