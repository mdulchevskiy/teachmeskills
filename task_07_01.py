# Написать 12 функций по переводу. Функция принимает на вход число
# и возвращает конвертированное число.


# Дюймы в сантиметры.
def inches_to_cm(inches):
    cm = inches * 2.54
    return cm


# Сантиметры в дюймы.
def cm_to_inches(cm):
    inches = cm / 2.54
    return inches


# Мили в километры.
def miles_to_km(miles):
    km = miles * 1.61
    return km


# Километры в мили.
def km_to_miles(km):
    miles = km / 1.61
    return miles


# Фунты в килограммы.
def pounds_to_kg(pounds):
    kg = pounds * 0.454
    return kg


# Килограммы в фунты.
def kg_to_pounds(kg):
    pounds = kg / 0.454
    return pounds


# Унции в граммы.
def ounces_to_grams(ounces):
    grams = ounces * 28.35
    return grams


# Граммы в унции.
def grams_to_ounces(grams):
    ounces = grams / 28.35
    return ounces


# Галлон в литры.
def gallons_to_liters(gallons):
    liters = gallons * 4.55
    return liters


# Литры в галлоны.
def liters_to_gallons(liters):
    gallons = liters / 4.55
    return gallons


# Пинты в литры.
def pints_to_liters(pints):
    liters = pints * 0.568
    return liters


# Литры в пинты.
def liters_to_pints(liters):
    pints = liters / 0.568
    return pints


if __name__ == '__main__':
    num = 56
    print(f'1. {num} inches is {round(inches_to_cm(num), 1)} cm.')
    print(f'2. {num} cm is {round(cm_to_inches(num), 1)} inches.\n')
    print(f'3. {num} miles is {round(miles_to_km(num), 1)} km.')
    print(f'4. {num} km is {round(km_to_miles(num), 1)} miles.\n')
    print(f'5. {num} pounds is {round(pounds_to_kg(num), 1)} kg.')
    print(f'6. {num} kg is {round(kg_to_pounds(num), 1)} pounds.\n')
    print(f'7. {num} ounces is {round(ounces_to_grams(num), 1)} grams.')
    print(f'8. {num} grams is {round(grams_to_ounces(num), 1)} ounces.\n')
    print(f'9. {num} gallons is {round(gallons_to_liters(num), 1)} liters.')
    print(f'10. {num} liters is {round(liters_to_gallons(num), 1)} gallons.\n')
    print(f'11. {num} pints is {round(pints_to_liters(num), 1)} liters.')
    print(f'12. {num} liters is {round(liters_to_pints(num), 1)} pints.\n')
