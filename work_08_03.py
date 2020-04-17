# Дан словарь, создать новый словарь, поменяв местам ключ и значение.


my_dict = {
    '0001': 1997,
    '0002': 1998,
    '0003': 1999,
}
new_dict = {value: key for key, value in my_dict.items()}
print(new_dict)
