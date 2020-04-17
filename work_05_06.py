# Создать список учеников подобной структуры. Определить средний балл оценок по всем предметам,
# и вывести сведения о студентах, средний балл которых больше 4.
# [02-7.3-BL-02]


pupils = [
    {
        'firstname': 'Masha',
        'group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Alex',
        'group': 43,
        'physics': 8,
        'informatics': 8,
        'history': 6,
    },
    {
        'firstname': 'Max',
        'group': 44,
        'physics': 3,
        'informatics': 4,
        'history': 3,
    }
]
b_mean = 0
for card in pupils:
    b_mean = (card['physics'] + card['informatics'] + card['history']) / 3
    if b_mean > 4:
        print(f"Firstname: {card['firstname']}\nGroup: {card['group']}\n")
