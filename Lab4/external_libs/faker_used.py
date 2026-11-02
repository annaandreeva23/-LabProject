import faker

def faker_used():  # Генерує випадкове вигадане ім'я
    return faker.Faker().name()
