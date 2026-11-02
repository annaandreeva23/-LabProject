import colorama

def colorama_used():  # Повертає текст, який у консолі виведеться зеленим кольором
    return colorama.Fore.GREEN + "Hello" + colorama.Style.RESET_ALL
