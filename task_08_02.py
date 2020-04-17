# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)
# [03-10.32]


def palindrome(word):
    return word == word[::-1]


def main():
    words = ['tikkit', 'max', 'anana', 'cat']
    for word in words:
        print(f'Is {word} palindrome? {palindrome(word)}')


if __name__ == '__main__':
    main()
