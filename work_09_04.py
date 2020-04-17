# Дан список имен, отфильтровать все имена, где есть буква k.


def main():
    name_list = ['Max', 'Jane', 'Kate', 'Nick']
    name_filter = list(filter(lambda name: 'k' in name, name_list))
    print(name_filter)


if __name__ == '__main__':
    main()
