from .greetings import greet_user
from .user_input import get_user_input
from .number_converter import convert_number_to_words

def main():
    greet_user()
    num = get_user_input()
    words = convert_number_to_words(num)
    print(words)

if __name__ == '__main__':
    main()
